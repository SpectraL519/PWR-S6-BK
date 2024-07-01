# Bezpieczeństwo komputerowe - [lab4](sec-lab4.pdf)

## Zadanie 2

2. **Podipis zaufany** - podpis elektroniczny, którego autentyczność i integralność są zapewniane przy użyciu pieczęci elektronicznej ministra właściwego do spraw informatyzacji, zawierający

    Z podpisu zaufanego może korzystać każdy, kto ma numer PESEL oraz pełną lub ograniczoną zdolność do czynności prawnych.

    Podpis zaufany może być użyty w relacjach z podmiotami administracji publicznej (pdopisywanie plików, umów, formularzy, itp w serwisach elektronicznych). Jest on równoważny pod względem skutków prawnych z podpisem własnoręcznym.

3. **Format podpisu zaufanego**

    * `PAdES` - podpisywanie plików PDF - podpis dodawany w tym samym pliku-
    * `XAdES` - podpisywanie plików w innych formatach:
        - XML: podpis dodawany do pliku
        - Inne formaty: treść dokumentu kodowana w Base64 i konwertowana do XML, następnie podpis jest dodawany w tym samym pliku lub w osobnym pliku XML

4. **Weryfikacja podpisu**

    * Przez: Centrum Kwalifikowane EuroCert
    * CRL: certyfikat nie znajduje się na tej liście.
        > CRL to lista unieważnionych certyfikatów/podpisów przed planowanym czasem wygaśnięcia
    * Ścieżka certyfikacji: 
        * Narodowe Centrum Certyfikacji
        * Centrum Kwalifikowane EuroCent
        * Minister do spraw informatyzacji - pieczęć podpisu zaufanego

5. **Modyfikacja zakodowanej treści**

    Integralność: Niezachowana - podpisane dane prawdopodobnie zostały zmodyfikowane po ich uwierzytelnieniu elektronicznym

6. **Niezaufany wystawca certyfikatu**

    Jeśli wystawca certyfikatu jest niezaufany, to "Certyfikat nie znajduje się na liście OCSP"

    > OCSP - Online Certificate Status Protocol: Status wycofania certyfikatu sprawdzony za pomocą protokołu OCSP zawiera informacje bliższe stanowi faktycznemu niż te dostępne na listach wycofania certyfikatów.

7. **Dostęp**

    * Zaufany - ważny jednynie w sprawach urzędowych, możliwość podpisu zdalnego, podpis cyfrowy
    * Osobisty - równoważny podpisowi odręcznemu, potrzebny jest czynik nfc oraz dowód, podpis elektroniczny
    * Kwalifikowany - ważność europejska, automatycznie weryfikowany, certyfikacji udziela firma trzecia będąca na jakiejś tam liście
