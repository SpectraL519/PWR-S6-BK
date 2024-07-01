from rc4 import RC4
from bank_account import BankAccount, BANK_CODES

from copy import deepcopy
from typing import Callable
import time


def measure_time(func: Callable):
    def _wrap(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f}s")
        return result
    return _wrap


# Constants
ACCOUNT_LEN = 28
NON_BANK_ID_DIGIT_INDICES = list(range(2, 4)) + list(range(12, 28))
NO_DATAGRAMS = 0

DIGIT_CHARACTER_RANGE = range(ord('0'), ord('9') + 1)

IntegerList1D = list[int]
IntegerList2D = list[IntegerList1D]


def generate_xor_combinations() -> dict[int, set[int]]:
    """
    Returns a dictionary of {xor: set[int]} pairs, where for each xor (key) in
    the dictionary the integers in the value set correspond to the integer values
    of digit characters which can be used to obtain the given xor
    """

    xor_combinations = {}
    for i in DIGIT_CHARACTER_RANGE:
        for j in range(i, ord('9') + 1):
            xored = i ^ j
            if xored not in xor_combinations:
                xor_combinations[xored] = set()
            xor_combinations[xored].add(i)
            xor_combinations[xored].add(j)
    return xor_combinations


def xor_lists(m1: IntegerList1D, m2: IntegerList1D) -> IntegerList1D:
    assert len(m1) == len(m2), "messages must have matching lengths"
    return [c1 ^ c2 for c1, c2 in zip(m1, m2)]


def generate_valid_character_lists(account_datagrams: IntegerList2D) -> IntegerList2D:
    """
    Parameters:
    - accounst: list of account numbers in a integer list representation

    Returns:
    - A list of length ACCOUNT_LEN, where the ith element in this list
      is a list of characters which are valid for the ith position of an account number
      based on the xored accounts
    """

    xor_combinations = generate_xor_combinations()

    # Initialize valid_character_lists with all possible characters for each position
    valid_character_lists = [set(DIGIT_CHARACTER_RANGE) for _ in range(ACCOUNT_LEN)]

    for i in range(1, NO_DATAGRAMS):
        xored_account_datagrams = xor_lists(account_datagrams[0], account_datagrams[i])
        assert len(xored_account_datagrams) == ACCOUNT_LEN, "invalid length of xored datagram list"

        for ix in range(ACCOUNT_LEN):
            valid_chars = xor_combinations.get(xored_account_datagrams[ix], set())
            valid_character_lists[ix] &= valid_chars

    return [sorted(list(chars)) for chars in valid_character_lists]


def no_possible_account_numbers(valid_character_lists: IntegerList2D) -> int:
    no = 1
    for i in NON_BANK_ID_DIGIT_INDICES:
        no *= max(len(valid_character_lists[i]), 1)
    return no * len(BANK_CODES)


def validate_control_sum(bank_account: BankAccount) -> bool:
    zero_ord = ord('0')

    control_sum_elements = [ord(c) for c in bank_account.bank_code + bank_account.account_number]
    control_sum_elements.extend([ord(c) - ord('A') + 10 for c in bank_account.country_code])
    control_sum_elements.extend([ord(c) for c in str(bank_account.control_sum)])

    control_sum = 0
    for elem in control_sum_elements:
        control_sum = (control_sum * 10 + (elem - zero_ord)) % 97

    return control_sum == 1


def verify_bank_account(
    account_datagram: IntegerList1D,
    bank_account_datagrams: IntegerList2D
) -> bool:
    for i in range(1, NO_DATAGRAMS):
        decrypted_account = xor_lists(account_datagram, bank_account_datagrams[i])
        if not validate_control_sum(BankAccount.from_list(decrypted_account)):
            return False
    return True


def attack_impl(
    bank_account: BankAccount,
    depth: int,
    bank_account_datagrams: IntegerList2D,
    valid_character_lists: IntegerList2D
) -> list[BankAccount]:
    found_bank_accounts = []

    if depth < len(NON_BANK_ID_DIGIT_INDICES):
        digit_idx = NON_BANK_ID_DIGIT_INDICES[depth]
        for i in range(len(valid_character_lists[digit_idx])):
            bank_account[digit_idx] = chr(valid_character_lists[digit_idx][i])
            found_bank_accounts += attack_impl(
                bank_account,
                depth + 1,
                bank_account_datagrams,
                valid_character_lists
            )
        return found_bank_accounts

    for bank_code in BANK_CODES:
        bank_account.bank_code = bank_code
        if not validate_control_sum(bank_account):
            continue
        xored_bank_accounts = xor_lists(bank_account_datagrams[0], bank_account.to_list())
        if verify_bank_account(xored_bank_accounts, bank_account_datagrams):
            found_bank_accounts.append(deepcopy(bank_account))

    return found_bank_accounts


@measure_time
def attack(
    bank_account_datagrams: IntegerList2D,
    valid_character_lists: IntegerList2D
) -> list[BankAccount]:
    print("Running brute force attack:")

    bank_account = BankAccount()

    for digit_idx in NON_BANK_ID_DIGIT_INDICES:
        bank_account[digit_idx] = chr(valid_character_lists[digit_idx][0])

    print(f"\tInitital bank account: {bank_account}")
    found_bank_accounts = attack_impl(bank_account, 0, bank_account_datagrams, valid_character_lists)
    print(f"\tFinal bank account: {bank_account}")

    return found_bank_accounts


def main():
    global NO_DATAGRAMS
    NO_DATAGRAMS = int(input("Enter number of datagrams: "))

    rc4_key = "bank_account_rc4_encryption_key"

    bank_accounts = [str(BankAccount.random()) for _ in range(NO_DATAGRAMS)]
    bank_account_datagrams = [RC4.encrypt(rc4_key, account) for account in bank_accounts]

    valid_character_lists = generate_valid_character_lists(bank_account_datagrams)
    print(f"Number of possible account numbers: {no_possible_account_numbers(valid_character_lists)}")

    found_bank_accounts = attack(bank_account_datagrams, valid_character_lists)

    print(f"Found {len(found_bank_accounts)} bank accounts:")
    for account in found_bank_accounts:
        print(f"\t-> {account}, correctly cracked = {str(account) in bank_accounts}")


if __name__ == "__main__":
    main()

"""
Example program executions:

-----
> python12 bank_attack.py
Enter number of datagrams: 20
Number of possible account numbers: 1310720
Running brute force attack:
        Initital bank account: PL40000000004682228208886462
        Final bank account: PL51114011405793339319997573
Execution time of attack: 3.0499s
Found 1 bank accounts:
        -> PL41101016744692238218887473, correctly cracked = True
-----
> python12 bank_attack.py
Enter number of datagrams: 10
Number of possible account numbers: 20971520
Running brute force attack:
        Initital bank account: PL06000000000262220042282604
        Final bank account: PL77114011407373331153393715
Execution time of attack: 49.0158s
Found 1 bank accounts:
        -> PL47105004484362321052392715, correctly cracked = True
-----
"""
