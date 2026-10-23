# Wibroakustyka w Technice i Środowisku 1

Sprawozdania laboratoryjne z przedmiotu na AGH, Wydział Inżynierii
Mechanicznej i Robotyki, kierunek Inżynieria Akustyczna.
Repozytorium utworzono z [agh-report-template](https://github.com/engelberd/agh-report-template),
opartego na [inscrive-io/latex-report-template](https://github.com/inscrive-io/latex-report-template).
Oryginalna [licencja MIT](LICENSE) pozostaje bez zmian.

## Układ repozytorium

```text
shared/style/universityreport.sty   wspólny wygląd wszystkich raportów
figures/                          wspólne logo i ilustracje
template/                         pliki startowe nowego ćwiczenia
cwiczenia/
  01-pomiar-poziomu-cisnienia/     pierwsze ćwiczenie (na razie demonstracja)
    main.tex                      metadane i kolejność sekcji
    latexmkrc                     odwołanie do wspólnej konfiguracji
    references.bib                bibliografia danego raportu
    content/                      tekst sprawozdania
    data/raw/                     oryginalne pomiary
    data/processed/               dane po obliczeniach
    analysis/                     Python lub Quarto, opcjonalnie
    figures/                      zdjęcia i ilustracje ćwiczenia
    generated/                    tabele, wykresy i wyniki analizy
    .output/                      wynikowy PDF i pliki pomocnicze
scripts/report.py                 tworzenie, kompilacja i eksport
latexmkrc                         wspólna konfiguracja pdfLaTeX + Biber
.output/                          lokalne narzędzia i archiwa eksportowe
```

Nie ma już `main.tex` w katalogu głównym. Każde ćwiczenie jest osobnym
raportem, ma własne metadane i własny PDF. Zmiany wspólnego stylu wpływają
na wszystkie raporty przy ponownej kompilacji.

Pierwszy raport zachowuje przykład z szablonu. Nie reprezentuje jeszcze
rzeczywistych pomiarów ani zatwierdzonego tematu pierwszego laboratorium.
Przed oddaniem zastąp dane demonstracyjne i uzupełnij metadane.

## Nowe ćwiczenie

W katalogu głównym repozytorium:

```bash
python3 scripts/report.py new 02-drgania-swobodne --number 2 --title "Drgania swobodne"
```

Polecenie kopiuje `template/`, wpisuje tytuł i numer oraz odmawia nadpisania
istniejącego katalogu. Następnie uzupełnij autorów, grupę, prowadzącego i datę
w nowym `main.tex`. Przedmiot jest już ustawiony na
**Wibroakustyka w Technice i Środowisku 1**.

Szablon zawiera dane i treści demonstracyjne do zastąpienia. W `content/`
używaj `\section` i `\subsection`; dodawaj sekcje przez `\input` w `main.tex`.
Opcjonalne streszczenie, spis treści i załącznik są wyłączone domyślnie.

## Kompilacja

Potrzebne są pdfLaTeX, Biber, latexmk i pakiety używane przez wspólny styl.
Zalecana dystrybucja TeX Live / MacTeX lub MiKTeX z polskimi wzorcami dzielenia,
fontami Libertinus i Fira, `siunitx` 3 oraz PGFPlots co najmniej 1.18.

Z katalogu głównego:

```bash
python3 scripts/report.py build 01-pomiar-poziomu-cisnienia
```

Lub przy narzędziach TeX dostępnych w `PATH`:

```bash
latexmk -pdf cwiczenia/01-pomiar-poziomu-cisnienia/main.tex
```

Można też wejść do katalogu ćwiczenia i uruchomić `latexmk -pdf main.tex`.
Wspólna konfiguracja automatycznie ustawia wyszukiwanie stylu i uruchamianie
Biber. Budowanie z katalogu głównego przechodzi do katalogu danego raportu.

Wynik zawsze znajduje się przy ćwiczeniu:
`cwiczenia/01-pomiar-poziomu-cisnienia/.output/main.pdf`.
Do lokalnej kompilacji używaj latexmk, aby załadować wspólną konfigurację.

### VS Code

Otwórz całe repozytorium, potem `main.tex` wybranego ćwiczenia i uruchom
**LaTeX Workshop: Build LaTeX project**. Receptura pracuje w katalogu
wybranego raportu i zapisuje wyniki do jego `.output/`.
Po zmianie ustawień wykonaj **Developer: Reload Window**.
Jeśli otwierasz pojedynczy plik sekcji, zacznij od otwarcia odpowiedniego
`main.tex`, aby rozszerzenie rozpoznało dokument główny.

Na tym komputerze lokalny TeX jest w głównym `.output/texlive`.
Nie jest śledzony przez Git. Na innym komputerze zainstaluj własną dystrybucję;
konfiguracja obsługuje standardową ścieżkę MacTeX i typowe katalogi systemowe.
Nie usuwaj całego głównego `.output/`, jeżeli korzystasz z lokalnego TeX.
Pliki pomocnicze pojedynczego raportu można czyścić poleceniem
`latexmk -c main.tex` uruchomionym w jego katalogu.

## Dane i analiza

- `data/raw/`: zachowuj oryginalne pliki z aparatury bez ręcznych poprawek.
- `analysis/`: umieść skrypty Python lub dokumenty Quarto.
- `data/processed/`: zapisuj przeliczone dane.
- `generated/`: zapisuj wygenerowane tabele `.tex`, wykresy `.pdf` i wartości
  używane w tekście. Dołączaj je przez `\input` i `\includegraphics`.
- `figures/`: przechowuj ilustracje danego ćwiczenia.

Na razie nie dodano zależności Python ani Quarto. Istniejąca tabela i wykres
nadal pobierają dane bezpośrednio z `data/raw/measurements.csv`.
Wygenerowane materiały potrzebne do kompilacji można zapisywać w Git;
pliki tymczasowe i wynikowe PDF raportów pozostają w ignorowanych `.output/`.

## Overleaf / przekazanie pojedynczego raportu

```bash
python3 scripts/report.py export 01-pomiar-poziomu-cisnienia
```

Powstaje `.output/exports/01-pomiar-poziomu-cisnienia.zip`.
Archiwum zawiera źródła ćwiczenia, dane, pliki analizy, własne ilustracje,
wspólny styl, domyślne logo i licencję. Nie zawiera lokalnego TeX,
plików ukrytych ani artefaktów kompilacji. Przy zmianie logo na inne wspólne
lub dodaniu zewnętrznych zależności należy je również dołączyć do eksportu.

Zaimportuj ZIP jako osobny projekt Overleaf, wybierz `main.tex`
i kompilator **pdfLaTeX**. Eksport jest samodzielny: styl i logo znajdują
się w katalogu głównym archiwum, a lokalne odwołania do repozytorium nie są
potrzebne. Po zmianie danych ponownie wygeneruj materiały analizy i eksport.
Nie edytuj wyeksportowanej kopii równolegle bez przeniesienia zmian do repo.

## Pochodzenie i licencja

Zachowano MIT, Copyright (c) 2026 Inscrive ApS. Układ nie jest oficjalnym
wzorem wydziałowym. Logo AGH nie stanowi przyznania praw do znaku uczelni.
