# Bezpieczeństwo komputerowe - [lab1](sec-lab1.pdf)

### Pkt 1

* SSH (Secure Shell protocol)
    * Kryptograficzny protokół sieciowy umożliwiający bezpieczne działanie usług sieciowych w niezabezpieczonej sieci
    * SSH jest zwykle używany do zdalnego logowania z komputerem i wykonywania poleceń. Pozwala także na przesyłanie plików (np. przy użyciu protokołu SCP - Secure Copy)

* Co daje powiązanie kluczy ssh z kontem (GitHub)?
    * Powiązanie kluczy SSH z kontem umożliwia uwierzytelnianie i autoryzację Twojego komputera do wykonywania operacji na Twoim koncie bez konieczności wprowadzania nazwy użytkownika i hasła za każdym razem. Daje to większe bezpieczeństwo i wygodę w korzystaniu z usług platformy:
        * **Bezpieczeństwo:** Klucze SSH zapewniają bardziej bezpieczne uwierzytelnianie niż tradycyjne hasła. Klucze są generowane lokalnie i nie są przesyłane przez sieć, co zmniejsza ryzyko przechwycenia przez niepowołane osoby.
        * **Wygodne uwierzytelnianie:** Po skonfigurowaniu kluczy SSH, GitHub automatycznie rozpoznaje Twój komputer, co eliminuje potrzebę wprowadzania hasła za każdym razem, gdy wykonujesz operacje na GitHub przez terminal lub innego klienta Git.
        * **Automatyczne uwierzytelnianie:** Gdy klucze SSH są powiązane z kontem GitHub, umożliwia to automatyczne uwierzytelnianie podczas wykonywania operacji, takich jak git push, git pull itp.
        * **Łatwe zarządzanie dostępem:** Możesz zarządzać kluczami SSH z poziomu swojego konta GitHub, co ułatwia ich dodawanie, usuwanie lub wygenerowanie nowych kluczy.

* Przesyłanie danych prywatnego repozytorium bez użycia protokołu SSH:
    * Dane są przesyłane po uwierzytelnieniu za pomocą loginu i hasła
    * Protokół HTTPS zapewnia szyfrowanie przesyłanych danych, jednak login i hasło są wysyłane w postaci zakodowanej (zwykle Base64) i mogą być odkodowane przez atakującego

* Wspierane typy kluczy(GitHub):
    * SSH
    * GPG (GNU Privacy Guard)

* Wygenerowany klucz SSH:
    * Typ: RSA
    * Długość: 3072b (ssh-keygen -l -f \<key-file-path\>)
    * Powód: Są to domyślne parametry kluczy generowanych na systemie Ubuntu

<br />
<br />

### Pkt 2

* Metody 2FA (GitHub):
    * Authentication App (np. Microsoft Authenticator) - generowanie jednorazowych oraz czasowych kodów dostępu
    * SMS - wysyłanie wiadomości z jednorazowym kodem dostępu
    * Security Keys - fizyczne klucze bezpieczeństwa
    * Aplikacja GitHub Mobile - przypisanie aplikacji do konta

* Wektory ataków eliminowane przez 2FA:
    * Phishing (potencjalnie, o ile właściciel konta się zorientuje, że prośba o weryfikację dostępu jest tego typu atakiem)
    * Ataki typu *brute force*
    * Ataki oparte na wyciekach danych
    * Ataki na sesję
    * Ataki na hasła wielokrotnego uzytku (wyciek hasła z jednego serwisu, które jest używane także poza tym serwisem uniemożliwi dostanie się do tych innych serwisów)
