# Bezpieczeństwo komputerowe - [lab2](sec-lab2.pdf)

## Zadanie 1

1. **Łamanie hasła atakiem brute-force: hasło składające się z samych cyfr**

    > Generowanie hasha w terminalu:
    > * MD5: `echo -n <password> | md5sum`
    > * SHA256: `echo -n <password> | sha256sum`

    **Hasło:** `314159`

    **MD5 Hash:** `819cf1304065c4ae95f2babaf8a03fd7`

    **SHA256 Hash:** `c5b389beb081fe1e43ae92e895deca086b4eed5cf9efc7b78eebbbc9dc75c3f0`

    Atak z użyciem programu `hashcat`:

    ```bash
    hashcat <hash-file> <mask> -m <hash-type> -a <attack-mode>  -o <output_file>
    ```

    Użyte opcje:
    * Maska = wzorzec hasła : (cyfra = `?d`)
    * `-m` = `--hash-type` : (MD5 = 0) (SHA256 = 1400)
    * `-a` = `--attack-mode` : (brute-force = 3)
    * `-o` = `--outfile`

    Opcjonalnie:

    ```bash
    hashcat <hash-file> <mask> -i --increment-min=<min> --increment-max=<max> -m <hash-type> -a <attack-mode>  -o <output_file>
    ```

    > Tutaj: `<min> <= <mask-length> <= <max>`


    TODO: --increment

<br />

2. **Łamanie hasła atakiem brute-force: hasło składające się z cyfr oraz małych liter**

    **Hasło:** `start123`

    **MD5 Hash:** `a3b9c163f6c520407ff34cfdb83ca5c6`

    **SHA256 Hash:** `2c4779e28ec964baa2afdeb862be4b9776562866443cfcf22f37950c20ed0af2`

    Użyte opcje:
    * Jak w pkt 1
    * Maska dla znaków [0-9a-z]: `hashcat <hash-file> -1 ?l?d <mask> <args>`, gdzie maska korzysta z symbolu `?1`

<br />

3. **Łamanie hasła atakiem słownikowym**

    **Hasło:** `qwerty123!`

    **MD5 Hash:** `6651b15eeb730854d66b654f00778425`

    **SHA256 Hash:** `9c781a9a01bcad170381302ba11629a1af2ca0f8734b1acb43aa88888cf4356a`

    Wywołanie programu hashcat:

    ```bash
    hashcat <hash-file> <dictionary-path> <mask> -m <hash-type> -a 6 -o <output_file>
    ```

    > Tutaj: `<mask-length> = <full-length> - <original-length>`
    >
    > Maska dla znaków specjalnych to: `?s` zatem pełna maska dla `qwerty123!` to `-1 ?d?s ?1?1?1?1`

<br />

4. **Łamanie hasła bez znajomości typu hasha**

    Nie znając typu hasha możemy zawęzić zbiór poszukiwań analizując długość i/lub strukturę hasha (niektóre hashe posiadają słowa kluczowe lub znaki specjalne w odpowiednich miejscach).

    Można także skorzystać z programu, który robi to automatycznie, jak np. `hashid`:

    ```bash
    hashid -m <hash>
    ```

    Dane dla kolegi:
    * **Hasło:** `porsche911!`
    * **GOST Hash:** `e80062c994267523d097b274b4f1cfd4e2d72bbe6d86bc0cd439feee08fd9aeb`

    Dane od kolegi:
    * **Hash:** `3eb3a40ba425f7e6e8a332f65e834e21`
    * [Wynik programu hashid](ex1.4/hashid.txt)
    * **Złamane hasło:** `bitch@221` (Typ hasha: `MD4`)

<br/>
<br/>
<br/>

## Zadanie 2

1. **Filtrowanie zebrenych danych:**

    W programie Wireshark można filtrować dane na podstawie parametrów takich jak:

    * Protokół (HTTP, HTTPS, FTP)
    * Adres IP (źródłowy/docelowy): `ip.src == 192.168.1.1`, `ip.dst == 8.8.8.8`
    * Adres MAC: np. `eth.addr == 00:11:22:33:44:55`
    * Port (źródłowy/docelowy): np. `tcp.port == 80` , `udp.port == 53`
    * Zawartość danych: np. `http.request.uri contains "login"`
    * Czas: np. `frame.time_relative > 5`
    * Inne

<br/>

2. **Rodzaje przesyłanych danych:**

    **Przeglądanie stron internetowych (HTTP/HTTPS):** W przypadku przeglądania stron internetowych za pomocą HTTP, dane przesyłane obejmują żądania i odpowiedzi HTTP, które mogą zawierać tekst, obrazy, multimedia, pliki CSS, JavaScript itp. W przypadku HTTPS, dane są szyfrowane, więc zawartość jest nieczytelna bez deszyfrowania SSL/TLS.

    **Transfer plików za pomocą SFTP:** W przypadku transferu plików za pomocą SFTP, dane przesyłane obejmują zawartość plików przesyłanych przez użytkownika, które są szyfrowane w celu zapewnienia poufności.

<br/>

3. **Wektory ataku:**

    Program Wireshark może być używany przy takich atakach jak:

    * **Ataki typu Man-in-the-Middle (MITM):** Wireshark może pomóc w wykryciu ataków typu MITM, w których cyberprzestępca przechwytuje i modyfikuje komunikację między dwoma stronami, niepostrzeżenie dla nich. Analiza ruchu sieciowego za pomocą Wiresharka może pomóc w identyfikacji nieoczekiwanych zmian w przesyłanych danych oraz podejrzanych wzorców, co może wskazywać na obecność ataku MITM.

    * **Ataki typu DoS (Denial of Service):** Wireshark może być użyteczny przy wykrywaniu ataków typu DoS, w których cyberprzestępca próbuje zablokować lub znacząco utrudnić dostęp do usług sieciowych poprzez nadmierną liczbę żądań lub inne techniki. Analiza ruchu sieciowego za pomocą Wiresharka może pomóc w identyfikacji dużego natężenia ruchu lub nietypowych wzorców zachowania, co może wskazywać na atak DoS.

    * **Ataki związane z wykorzystaniem luk w zabezpieczeniach (exploits):** Wireshark może pomóc w identyfikacji ataków wykorzystujących luki w zabezpieczeniach, np. ataków typu buffer overflow, SQL injection, czy też ataków XSS (Cross-Site Scripting). Analiza ruchu sieciowego może pomóc w zidentyfikowaniu nieprawidłowych lub nieoczekiwanych żądań HTTP, nietypowych zachowań klienta lub serwera, co może wskazywać na potencjalne wykorzystanie exploitów.

    * **Ataki typu Phishing:** Wireshark może pomóc w identyfikacji ataków phishingowych, w których cyberprzestępcy próbują wyłudzić poufne informacje poprzez podszywanie się pod zaufane strony lub serwis. Analiza ruchu sieciowego za pomocą Wiresharka może pomóc w identyfikacji nieautoryzowanych prób logowania się, przekierowań na podejrzane strony internetowe lub nietypowych wzorców aktywności użytkownika.

    * **Ataki na protokoły kryptograficzne:** Wireshark może być przydatny w identyfikacji ataków na protokoły kryptograficzne, takie jak SSL/TLS. Analiza ruchu sieciowego może pomóc w wykryciu prób złamania szyfrowania lub ataków typu downgrade, w których cyberprzestępca próbuje zmusić komunikację do użycia słabszej wersji protokołu kryptograficznego.

<br/>

4. **Informacje przeczhwytywane przy protokołach HTTP oraz HTTPS**

    **Protokół HTTP:**

    * Metadane żądania i odpowiedzi: Z ruchu sieciowego HTTP można odczytać metadane żądania i odpowiedzi, takie jak adresy URL, metody HTTP (GET, POST, itp.), nagłówki żądania i odpowiedzi (User-Agent, Cookies, itp.).

    * Zawartość przesyłanych danych: W przypadku ruchu HTTP, dane przesyłane między klientem a serwerem są przesyłane w formie niezaszyfrowanej, co oznacza, że można odczytać ich zawartość. Oznacza to, że potencjalnie wrażliwe informacje, takie jak hasła lub dane osobowe, mogą być odczytane przez osobę podsłuchującą.

    <br/>

    **Protokół HTTPS:**

    * Szyfrowane dane: W przypadku ruchu HTTPS, dane są przesyłane w sposób zaszyfrowany, co oznacza, że nie można bezpośrednio odczytać ich zawartości. Większość informacji w nagłówkach nadal jest dostępna, ale treść przesyłanych danych jest zabezpieczona przed odczytem przez osobę trzecią.

    * Metadane połączenia SSL/TLS: Mimo że zawartość jest zaszyfrowana, nadal można uzyskać dostęp do metadanych związanych z połączeniem SSL/TLS, takich jak adresy IP i domeny serwerów, używane protokoły (np. TLS 1.2), długość sesji, itp.

    <br/>

    **Czy można na podstawie zebranych informacji dowiedzieć się, jakie strony internetowe/domeny były odwiedzane?**

    **Protokół HTTP:** Tak, jest to możliwe, ponieważ adresy URL są przesyłane jako część żądań HTTP w formie tekstowej, co pozwala na odczytanie odwiedzanych stron internetowych.

    **Protokół HTTPS:** Pomimo że treść jest zaszyfrowana, nadal można odczytać metadane połączenia SSL/TLS, w tym adresy IP i domeny serwerów, co może dać wgląd w odwiedzane strony internetowe. Jednakże, bez dostępu do klucza prywatnego serwera, treść żądań i odpowiedzi pozostaje nieczytelna dla osoby podsłuchującej.
