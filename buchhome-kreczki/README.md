# Rezydencja w Kręczkach — prototyp strony

Statyczna strona (jeden plik `index.html` + `assets/`) dla inwestycji BUCHHOME sp. z o.o. przy ul. Żyznej w Kręczkach.
Dane pochodzą z projektu budowlanego (PZT 01A z 08.2026, PAB etap I i II z 09.2026, tomcat.arch.design).

Podgląd lokalny: `python3 -m http.server` w tym katalogu, potem http://localhost:8000.

## Do uzupełnienia przed publikacją
W bloku `DANE (edytuj tutaj)` w `index.html`:
- `STATUS_OVERRIDES` — statusy i ceny domów (domyślnie wszystkie „Dostępny”, „Zapytaj o cenę”),
- `DEST` — odległości i czasy dojazdu (obecnie szacunkowe),
- telefon i e-mail w sekcji Kontakt, daty w Harmonogramie, powierzchnie ogrodów,
- podłączenie formularza kontaktowego (teraz tylko pokazuje komunikat).
