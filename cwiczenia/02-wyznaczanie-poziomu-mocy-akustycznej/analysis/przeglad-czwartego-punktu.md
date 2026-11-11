# Przegląd rejestracji: czwarty punkt przy ścianie

Nie dodano niepotwierdzonego pliku do serii P53–P55.
Pełny przegląd: `data/processed/svl-audit.csv`, odtwarzany przez `audit_svl.py`.

- P53: 12:56, LAeq 85,01 dB, 15 s.
- P54: 12:57, LAeq 84,00 dB, 15 s.
- P55: 12:58, LAeq 84,23 dB, 15 s.
- P56: 15:16, LAeq 57,39 dB, 12 s przy zadanym czasie 15 s.
  Przebieg sekundowy zmienny (około 47–62 dB). Ten plik nie stanowi
  udokumentowanego czwartego punktu serii przy ścianie.
- P57 i kolejne: od 15:30; samo podobieństwo poziomów w późniejszych
  plikach nie pozwala przypisać ich do wcześniejszego ustawienia.
- P43–P49: przed serią rogu P50–P52, bez opisu lokalizacji.
  Chronologia nie dowodzi przynależności do ustawienia przy ścianie.

Pliki SVL określają wskaźnik, profile, czas i wyniki, lecz w odczytanych
metadanych nie ma współrzędnych punktów ani opisu ustawienia źródła.
Potrzebny jest protokół/notatka albo potwierdzenie osoby wykonującej pomiary.
Nie zastępować brakującego punktu powtórzeniem istniejącej wartości ani
plikiem dobranym do oczekiwanego wyniku.

Parser dopuszcza poprawnie zapisany pomiar krótszy od zadanego, ale nadal
weryfikuje zgodność rzeczywistego czasu, liczby rekordów, średnich A/C/Z
oraz LAE. Odczyt P56 nie wymagał pomijania kontroli spójności.
