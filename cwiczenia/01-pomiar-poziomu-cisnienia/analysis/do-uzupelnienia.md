# Ćwiczenie 1 — stan sprawozdania na 25.10.2026

Sprawdzono wymagania konspektu (s. 2–5). Główny tekst LaTeX zawiera już rzeczywiste próbki, metodę obliczeń, kontrolę liczby próbek, korekcję tła oraz wnioski. Wersja robocza nie deklaruje pełnej zgodności pomiarów z procedurą.

## Potwierdzone i wykorzystane

- P04–P08: pomiary przy stacji; P10–P14: tło.
- Zespół realizował wariant laboratoryjny z próbkami 10 s. Nie potwierdzono terenowego uzasadnienia skrócenia czasu z 60 s do 10 s, przewidzianego w konspekcie.
- Mikrofon miał osłonę przeciwwietrzną.
- Kalibratora nie udostępniono; zespół nie wykonał sprawdzenia przed sesją ani po niej.
- Dostępnych jest tylko pięć próbek tła; nie ma dodatkowych pomiarów.
- Do obliczeń wykorzystano równoważne poziomy dźwięku A zarejestrowane miernikiem dla próbek 10 s. Raport nie omawia ręcznych odczytów ani konwersji LAE.
- Średnia przy stacji: 52,74 dB; tło: 48,08 dB; po korekcji: 50,92 dB (roboczo 50,9 dB).
- Liczebność: przy stacji wymagane 4, wykonane 5; tło wymagane 7, wykonane 5. Nie odrzucano żadnej próbki.

## Dane, które trzeba ustalić albo jawnie uznać za niedostępne

| Informacja z konspektu | Co jeszcze ustalić |
|---|---|
| Data i godziny ćwiczenia | Miernik wskazuje 15.10.2026, przy stacji 12:13–12:16, tło 12:22–12:25. Potwierdzić rzeczywistą datę i zgodność zegara; strona tytułowa nadal używa daty kompilacji. |
| Warunki meteorologiczne | Czy mierzono/zapisano temperaturę, wilgotność, ciśnienie, prędkość i kierunek wiatru? Jeśli nie, pozostawić informację o braku danych. Pogoda z odległej stacji nie jest równoważna pomiarowi na stanowisku. |
| Mikrofon i dokumentacja zestawu | Model/numer mikrofonu, numer świadectwa wzorcowania i termin. Nr miernika 40452 pochodzi z notatki zespołu; plik zawiera zgodne dolne słowo numeru. |
| Dokładne położenie punktów | Od czego mierzono 1,5 m: ściana obudowy, ogrodzenie czy granica działki? Współrzędne, jeśli dostępne. |
| Porównywalność punktu tła | Osłonięcie od stacji, odległości i ekspozycja na ulice, słyszalność stacji w punkcie tła. |
| Obiekt i źródła | Pełna identyfikacja/adres operatora i obiektu, zaobserwowane źródła oraz czas pracy. Nie dopisywać niepotwierdzonych urządzeń wewnątrz stacji. |
| Przeznaczenie terenu i kryterium oceny | Dane z MPZP/decyzji, jeśli dostępne; bez nich nie wybierać arbitralnego limitu. Wynik przy stacji nie jest automatycznie wynikiem na terenie chronionym. |
| Materiały graficzne | Potwierdzić źródło każdej mapy, datę dostępu; wskazać północ, skalę i obiekty odbijające/osłaniające, jeśli nie są czytelne na mapach. |
| Protokół i podpisy | Czy jest karta terenowa? Podpisy wykonujących; nie tworzyć fikcyjnego podpisu przedstawiciela operatora. Konspekt wiąże obligatoryjny podpis przedstawiciela z pomiarami kontrolnymi. |

## Co jest ograniczeniem pomiaru, a nie pustym polem do uzupełnienia

Braku kalibratora i dwóch próbek tła nie da się naprawić przez redakcję raportu. Należy je opisać, jak zrobiono w wersji roboczej. Jeżeli prowadzący zaakceptował uproszczony wariant ćwiczenia, można wskazać ten zakres dydaktyczny, ale nie twierdzić, że zrealizowano wszystkie wymagania metodyki referencyjnej.

Na życzenie autora pominięto rozdział o niepewności z powodu braku danych o przyrządach. W części konspektu zatytułowanej „DANE REJESTROWANE W PROTOKOŁACH I SPRAWOZDANIACH Z BADAŃ” nie ma osobnego wymagania rozdziału ani budżetu niepewności. Nadal pozostają wymagania identyfikacji aparatury i dokumentacji wzorcowania. Liczba cyfr w tabelach służy odtworzeniu obliczeń, a nie deklaracji dokładności 0,01 dB.

## Odtworzenie obliczeń i PDF

Z katalogu ćwiczenia:

```bash
python3 analysis/prepare_report.py
```

Z katalogu repozytorium:

```bash
python3 scripts/report.py build 01-pomiar-poziomu-cisnienia
```

Skrypt obliczeń czyta oryginalne SVL, generuje `data/processed/report-series.csv`, `report-results.json` i tabele w `generated/`. Demonstracyjny `measurements.csv` zachowano jako wcześniejszy plik, ale raport już go nie wykorzystuje.

## Wynik ponownego sprawdzenia wymagań

**Nie spełniamy jeszcze wszystkich wymagań konspektu.** Są cel, obiekt i otoczenie, mapa obu punktów, wysokość mikrofonu, metoda, nastawy A/Fast, czas próbek, komplet dostępnych wyników obu serii i ich opracowanie. Niepewność nie jest osobną pozycją listy zawartości konspektu.

Braki w samym raporcie: data i czas badań, dane meteorologiczne, pełna identyfikacja i dokumentacja aparatury, dane operatora/adresu i źródeł oraz ich czasu pracy (tp/T), przeznaczenie terenu i poziomy dopuszczalne, podpisy. Przeznaczenie z MPZP i współrzędne konspekt uzależnia od dostępności danych; podpis przedstawiciela operatora jest obligatoryjny przy pomiarach kontrolnych.

Braki realizacji procedury: nie wykonano sprawdzenia kalibratorem; liczba próbek tła wynosi 5 zamiast wymaganych 7; uzasadnienie próbek 10 s wskazuje przydział wariantu laboratoryjnego, lecz nie potwierdza warunku okresowych zakłóceń z konspektu. Porównywalność punktu tła wymaga uzasadnienia.
