# Przegląd sprawozdania: hałas obiektu przemysłowego

Stan przeglądu: 24.10.2026. Przeczytano wszystkie 5 stron konspektu i rozdziały LaTeX. Sprawdzono wizualnie wszystkie strony konspektu, w tym wzory i tabelę liczby próbek. Odczytano 10 plików SVL bez SvanPC++ i bez modyfikowania oryginałów.

## Najważniejsze ustalenia

Masz właściwy ogólny układ rozdziałów. Najwięcej pracy wymaga udokumentowanie warunków i opracowanie rzeczywistych danych, a nie rozbudowywanie teorii. W rozdziałach 5–6 oraz measurements.csv nadal są dane demonstracyjne. Nie stanowią wyników tego ćwiczenia. Bibliografia również pochodzi z szablonu i nie dotyczy akustyki.

Przypisanie P04–P08 do pomiaru zasadniczego i P10–P14 do tła jest **niepotwierdzone**. Użytkownik uznał drugą serię za prawdopodobne tło i zapowiedział późniejszą weryfikację. Wszystkie obliczenia łączące serie poniżej są warunkowe.

## 1. Co konkretnie wymaga prowadzący

Źródło: lokalny konspekt, s. 2–5. Instrukcja odwołuje się do rozporządzenia z 2014 r.; przy opisie wykonania ćwiczenia należy ją wskazać jako bezpośrednią podstawę. Dodatkowo zweryfikowano treść metodyki w oficjalnym tekście jednolitym z 2023 r. Nie należy przepisywać starych oznaczeń norm z konspektu jako potwierdzenia ich aktualności.

| Wymaganie konspektu | Stan szkicu i sposób uzupełnienia |
|---|---|
| Identyfikacja obiektu i prowadzącego instalację | Numer stacji i lokalizacja są; dopisać dane operatora i adres na podstawie oznaczenia obiektu lub dokumentów. |
| Data i godziny badań, skład zespołu | Autorzy są; brakuje daty i przedziału godzin. Data z miernika: 15.10.2026, do potwierdzenia. `\\today` oznacza datę kompilacji, nie pomiaru. |
| Rodzaje źródeł i czas ich pracy | Brak potwierdzonego wykazu i harmonogramu. Oddzielić zaobserwowane dźwięki od hipotez o urządzeniach wewnątrz stacji. |
| Opis terenu, jego przeznaczenie i właściwe poziomy dopuszczalne | Opis jest częściowy. Nie utożsamiać możliwości zabudowy z ustalonym przeznaczeniem terenu w MPZP. |
| Lokalizacja punktu, wysokość, współrzędne jeśli dostępne | Wysokość i odległość podano; dopisać odniesienie odległości: obudowa, ogrodzenie czy granica działki. |
| Metoda próbkowania | Wskazana; brakuje zasad doboru czasu, liczby próbek i obliczeń. |
| Aparatura: model, numery, dokumenty, nastawy i kontrole toru | SVL wskazuje SVAN 971. Nagłówek starej wersji formatu zawiera dolne słowo numeru 40452; pełny numer potwierdzić z obudowy/dokumentów. Profil A/Fast potwierdzony. |
| Meteorologia | Brak temperatury, wilgotności, ciśnienia, prędkości i kierunku wiatru. Brak danych trzeba wskazać, a nie zastępować wymyśloną pogodą. |
| Wszystkie próbki i pomiary tła, t0, tp, czas pracy źródeł | Eksport SVL dostarczył próbki 10 s. Brakuje potwierdzonego tp i harmonogramu pracy. |
| Plan z obiektem, punktami i elementami wpływającymi na propagację | Mapy są; warto dodać oznaczenia P i T, kierunek północy, skalę i opis przeszkód/ulic. |
| Podpis wykonujących; podpis przedstawiciela zakładu przy pomiarach kontrolnych | Nie dopisywać fikcyjnego przedstawiciela. To sprawozdanie z ćwiczenia, nie udokumentowana kontrola zakładu. |

## 2. Uwagi do Twoich rozdziałów 1–4

### Cel

Zamiast równoważnika „Wykonanie pomiarów…” użyj: „Celem ćwiczenia było wyznaczenie poziomu dźwięku A związanego z pracą stacji gazowej nr 08/3159 w wybranym punkcie jej otoczenia, metodą próbkowania, z uwzględnieniem tła akustycznego”. Ocenę względem limitu zapowiadaj tylko w zakresie, na jaki pozwolą dane o terenie i czasie pracy.

Sformułowanie „zgodnie z metodyką referencyjną” jest obecnie zbyt mocne. Przy braku kontroli toru oraz niepełnej dokumentacji bezpieczniej: „Pomiary wykonano metodą próbkowania opisaną w instrukcji laboratoryjnej; ograniczenia realizacji procedury omówiono w dalszej części”.

### Obiekt i teren

Nie ma podstaw, aby nazywać ten obiekt jednocześnie stacją gazową, przepompownią i maszynownią. Ujednolić na „stacja gazowa”. Nie stwierdzać obecności sprężarek, pomp ani reduktorów bez identyfikacji wyposażenia. Opis funkcji redukcji/rozdziału wymaga potwierdzenia rodzaju stacji. Potencjalne mechanizmy hałasu można przedstawić jako hipotezy, nie jako wyniki oględzin wnętrza.

Pomiar 1,5 m od obiektu nie jest automatycznie pomiarem na terenie przyszłej zabudowy mieszkaniowej. Możesz napisać: „Punkt zlokalizowano po północnej stronie stacji, w kierunku rozpatrywanego terenu”. Wniosek o hałasie w innym miejscu wymaga pomiaru w tym miejscu lub odpowiedniego modelu propagacji.

W opisie tła samo „porównywalne miejsce” nie wystarcza do oceny jakości korekcji: opisz odległości od ulic, ekspozycję na ruch, przesłanianie stacji i możliwość jej słyszalności. Tło ma reprezentować dźwięki niezwiązane z badanym obiektem. Pomiar krótko po serii jest informacją istotną, lecz nie dowodzi sam w sobie porównywalności miejsc.

Dwa rysunki mają identyczny `\\label{fig:placeholder}`. Nadaj im odrębne etykiety. Dla map podaj pochodzenie i datę dostępu. Zapis jednostek ujednolić na `1,5 m` / `\\qty{1.5}{\\metre}`.

### Aparatura i warunki

Uzupełnij pełny model, mikrofon, osłonę przeciwwietrzną, statyw, dokumentację wzorcowania, kontrolę przed/po i pogodę. Nie utożsamiaj świadectwa wzorcowania z terenowym sprawdzeniem kalibratorem.

W SVL profil 1: A/Fast, profil 2: C/Impulse, profil 3: Z/Fast; Leq jest całkowane liniowo. Do tego ćwiczenia podstawową wielkością jest LAeq. Fast opisuje detektor poziomów chwilowych/minimum/maksimum; nie oznacza, że LAeq należy odczytywać jako LAFmax.

Pliki przechowują poprzednią kalibrację typu „by measurement”, z datą 14.10.2026, współczynnikiem 2,37 dB. To **nie jest odczyt poziomu kalibratora** ani dowód sprawdzenia przed sesją 15.10. W polu po pomiarze zapisano 65535, oznaczające brak wykonanej kalibracji. Zweryfikować z notatkami; ograniczenie opisać w rozdziale 3 i wnioskach.

Tabela aparatury deklaruje trzy kolumny `L L L`, a zawiera dwie; zmień na `L L`.

### Metodyka

Obecne cztery punkty to plan czynności. Uzupełnij: wielkość mierzoną, nastawy, t0, liczbę próbek, ocenę rozstępu, sposób wyznaczenia tła i wzory. Osobny plik `metodyka-propozycja.tex` zawiera propozycję do włączenia po rozstrzygnięciu uwag.

Próbki 10 s wymagają w konspekcie konkretnego uzasadnienia: stabilny hałas obiektu, zakłócenia okresowe i brak możliwości zmieszczenia próbki 60 s między nimi. Nie dopisuj, że tak było, jeśli tego nie obserwowano.

## 3. Eksport SVL na macOS i sprawdzenie poprawności

Uruchomienie z dowolnego katalogu:

```sh
python3 analysis/export_svl.py
```

Powyższe polecenie zakłada wejście do katalogu ćwiczenia. Skrypt nie wymaga bibliotek zewnętrznych. Eksportuje podsumowania, przebiegi 1 s i metadane do `data/processed/`. Jest celowo ograniczony do napotkanego SVAN 971, formatu 1.07 i konfiguracji; odrzuca inne konfiguracje zamiast zgadywać. Nie jest uniwersalnym zamiennikiem SvanPC++.

Walidacja: zgodność granic wszystkich ramek, długości bufora, 10 rekordów, czasu 10 s, brak pominiętych rekordów, zgodność Leq profili z wartościami TOTAL widma do 0,01 dB, brak flag ostrzegawczych w rekordach i brak bitu przeciążenia w wynikach. Średnia energetyczna dziesięciu rekordów 1 s odtwarza podsumowanie z maksymalną różnicą 0,00475 dB. To mocne sprawdzenie wewnętrzne, lecz nie porównanie z eksportem producenta; taki eksport warto później porównać.

Zachowano surowy kod godziny. W instrukcji B.4 występuje niejednoznaczna formuła sekund (`time % 30`); nie nadano eksportowi fałszywej precyzji czasu bez porównania z SvanPC++. Data i godzina/minuta są odczytane z zegara miernika, bez potwierdzenia jego poprawności i strefy.

## 4. Wyniki odczytu i obliczenia warunkowe

| Plik | LAeq dla 10 s [dB] |
|---|---:|
| P04 | 52,54 |
| P05 | 52,27 |
| P06 | 51,96 |
| P07 | 53,31 |
| P08 | 53,42 |
| P10 | 48,05 |
| P11 | 47,72 |
| P12 | 49,77 |
| P13 | 47,08 |
| P14 | 47,20 |

Jeśli P04–P08 to hałas całkowity w punkcie, a P10–P14 to tło:

- Średnia energetyczna pierwszej serii: 52,738 dB; R = 1,46 dB, konspekt wymaga 4 próbek, dostępnych 5.
- Średnia energetyczna drugiej serii: 48,080 dB; R = 2,69 dB, konspekt wymaga 7 próbek, dostępnych 5. Sprawdź, czy są jeszcze pliki z pomiarem tła. Nie usuwaj P12 wyłącznie dlatego, że podnosi rozstęp. Ewentualne odrzucenie wymaga udokumentowanego zakłócenia.
- Różnica średnich: 4,658 dB. Korekcja tła jest potrzebna. Wynik odejmowania energetycznego: 50,919 dB, czyli roboczo 50,92 dB(A). Nie jest to jeszcze końcowy wynik zgodny z pełną procedurą.

Dziesięć rekordów 1 s wewnątrz pliku to nie dziesięć niezależnych próbek 10 s. Nie można nimi sztucznie zwiększyć liczby próbek w tabeli konspektu.

Nie oznaczaj wyniku jako LAeqD lub LAeqN bez uzasadnienia reprezentatywności i czasu pracy źródeł. Nie porównuj krótkiego pomiaru przy stacji bezpośrednio z limitem dla niepotwierdzonego terenu mieszkaniowego.

## 5. Jak dokończyć wyniki, niepewność i wnioski

W rozdziale 5 zamień demonstrację na tabelę powyżej, uzupełnioną o potwierdzone przypisanie, czas i uwagi terenowe. Pokaż osobno rozstęp, dobór n, średnie energetyczne oraz korekcję tła. Wykres kolejnych próbek jest pomocny; nie jest potrzebna mapa hałasu interpolowana z jednego punktu.

W rozdziale 6 nie przenoś automatycznie niepewności arytmetycznej średniej z szablonu na wynik po korekcji. Model wyniku obejmuje średnie energetyczne dwóch serii i ich różnicę energetyczną. Dla `Ls = 10 log10(10^(Lm/10) - 10^(Lt/10))` współczynniki wrażliwości wynoszą `cm = 10^(Lm/10)/(10^(Lm/10)-10^(Lt/10))` oraz `ct = -10^(Lt/10)/(10^(Lm/10)-10^(Lt/10))`. Uwzględnij zależności składników wspólnych przyrządu, jeśli są znane. Budżet musi mieć źródła wartości typu B; brak kontroli toru nie pozwala po prostu przyjąć zerowej niepewności kalibracji. Bez danych nie wpisuj liczbowego U.

Wnioski mają odpowiadać na cel: jaki poziom wyznaczono, jak silne było tło, czy seria spełnia kryterium n i jakie ograniczenia mają dane. Brak kalibracji to jeden z elementów oceny, nie cały wniosek.

## 6. Zweryfikowane źródła i ich zastosowanie

1. **Instrukcja J. Piechowicza, „Hałas obiektu przemysłowego – pomiary w środowisku”**, lokalny PDF. Podstawa wymagań prowadzącego: s. 3 – t0, n, średnia; s. 4 – tło, korekcja; s. 4–5 – dokumentacja. To główne źródło metodyki tego sprawozdania.
2. **Oficjalny tekst metodyki, załącznik 7, Dz.U. 2023 poz. 1706**: https://eli.gov.pl/api/acts/DU/2023/1706/text.html . Sprawdzono m.in. zasady próbkowania i wyznaczania tła. To dokument normatywny, nie publikacja naukowa. Nie wydano tu opinii o zgodności prawnej badania.
3. **Lokhande S.K. i in., “Evaluation of Practical Framework for Industrial Noise Mapping: A Case Study”, Noise & Health, 21(102), 194–199; DOI 10.4103/nah.NAH_7_17.** Pełny tekst: https://pmc.ncbi.nlm.nih.gov/articles/PMC7650851/ . Wydanie oznaczone 2019, publikacja online 2020. Przykład opisu zakładu, punktów i porównania modelu z pomiarem. Pokazuje potrzebę rozdzielenia źródeł przemysłowych i transportowych. Nie przenosić indyjskich limitów ani wymagań aparaturowych do polskiego ćwiczenia. W tekście są rozbieżności wartości R² między fragmentami; nie ma potrzeby ich cytować.
4. **Durán del Amor M.M., Baeza Caracena A., Llorens M., Esquembre F. (2022), “Tools for evaluation and prediction of industrial noise sources. Application to a wastewater treatment plant”, Journal of Environmental Management 319, 115725; DOI 10.1016/j.jenvman.2022.115725.** https://doi.org/10.1016/j.jenvman.2022.115725 ; kopia w repozytorium uczelni: https://digitum.um.es/bitstreams/f9026b6e-4950-465f-b22c-fb7ca1c31065/download . Zweryfikowano metadane i abstrakt; bezpośredni pełny tekst podczas przeglądu zwracał 403. Przydatny przykład identyfikowania wkładu źródeł, wykorzystania widm i walidacji pomiarowej. Nie przypisano mu szczegółów procedury niewidocznych w abstrakcie.
5. **Asselineau M., “Noise radiated by a piece of industrial equipment: case study”**, publikacja konferencyjna udostępniona przez Institute of Acoustics: https://www.ioa.org.uk/system/files/proceedings/m_asselineau_noise_radiated_by_a_piece_of_industrial_equipment_case_study.pdf . Przeczytano pełny tekst. Szczególnie przydatny do opisu otoczenia, inwentaryzacji źródeł i zdarzeń zakłócających. Dotyczy zakładu chemicznego we Francji; francuskich kryteriów oceny nie stosować w tym ćwiczeniu. Rok i konferencja niepotwierdzone w samym PDF.
6. **SVANTEK, “SVAN 971 User Manual”, v.3.1, 2020**, Appendix B: https://svantek.com/wp-content/uploads/2020/08/svan_971_man_en_v.3.1_2020-09-03.pdf . Podstawa odczytu struktury SVL. Sprawdzono lokalnie pełne tabele. Instrukcja opisuje nowszą rewizję formatu niż dane; odczyt ograniczono do zgodnych, zweryfikowanych pól i zapisano surowe kody czasu.

Do bibliografii sprawozdania wystarczy instrukcja, rzeczywiście użyta podstawa metodyczna i dokumentacja miernika; artykuły warto przywołać tylko przy konkretnym stwierdzeniu, które wspierają. Nie ma potrzeby budować rozbudowanego przeglądu literatury do krótkiego ćwiczenia.

## 7. Dane do rozstrzygnięcia

1. Potwierdzenie przypisania obu serii oraz kompletności plików (brakuje P09, ale sam brak numeru nie dowodzi braku próbki tła).
2. Faktyczna data i godziny sesji, zgodność zegara miernika.
3. Przyczyna użycia 10 s i notatki o zakłóceniach.
4. Położenie i porównywalność punktu tła.
5. Pogoda, osłona, mikrofon, numer przyrządu i dokumentacja wzorcowania.
6. Czas pracy stacji i przeznaczenie terenu, jeśli oczekiwana jest ocena względem poziomów dopuszczalnych.
