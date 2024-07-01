import random

# Bank account information
BANK_CODES = [
    "10101674",  # NBP Wroclaw
    "10205226",  # PKO BP SA Wroclaw
    "12406784",  # Pekao SA Wroclaw
    "10500448",  # ING Bank Slaski SA Wroclaw
    "11401140"   # mBank SA Wroclaw
]

class BankAccount:
    def __init__(
        self,
        bank_code: str = "00000000",
        account_number: str = "0000000000000000",
        control_sum: str = None
    ):
        self.country_code = "PL"
        self.bank_code = bank_code
        self.account_number = account_number
        self.control_sum = "{:0>{width}}".format(
            self.calculate_control_sum() if control_sum is None else control_sum, width=2
        )

        # print(self.control_sum, type(self.control_sum))

    def __str__(self):
        return self.country_code + self.control_sum + self.bank_code + self.account_number

    def __setitem__(self, index: int, value: chr):
        if index < 2:
            self.country_code = self.country_code[:index] + value + self.country_code[index+1:]
        elif index < 4:
            i = index - 2
            self.control_sum = self.control_sum[:i] + value + self.control_sum[i+1:]
        elif index < 12:
            i = index - 4
            self.bank_code = self.bank_code[:i] + value + self.bank_code[i+1:]
        else:
            i = index - 12
            self.account_number = self.account_number[:i] + value + self.account_number[i+1:]

    def calculate_control_sum(self) -> int:
        zero_ord = ord('0')

        control_sum_elements = [ord(c) for c in self.bank_code + self.account_number]
        control_sum_elements.extend([ord(c) - ord('A') + 10 for c in self.country_code])
        control_sum_elements.extend([zero_ord, zero_ord])

        control_sum = 0
        for elem in control_sum_elements:
            control_sum = (control_sum * 10 + (elem - zero_ord)) % 97
        return 98 - control_sum

    def to_list(self) -> list[int]:
        return [ord(c) for c in self.__str__()]

    @staticmethod
    def from_list(lst: list[int]):
        bank_account = BankAccount()
        bank_account.country_code = ''.join([chr(v) for v in lst[:2]])
        bank_account.control_sum = ''.join([chr(v) for v in lst[2:4]])
        bank_account.bank_code = ''.join([chr(v) for v in lst[4:12]])
        bank_account.account_number = ''.join([chr(v) for v in lst[12:]])
        return bank_account

    @staticmethod
    def random():
        return BankAccount(
            bank_code=random.choice(BANK_CODES),
            account_number=str(random.randint(1000000000000000, 9999999999999999))
        )
