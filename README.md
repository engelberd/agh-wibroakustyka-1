# Szablon sprawozdania AGH

Kompaktowy szablon LaTeX do sprawozdań laboratoryjnych i raportów technicznych:
Akademia Górniczo-Hutnicza im. Stanisława Staszica w Krakowie,
Wydział Inżynierii Mechanicznej i Robotyki, Inżynieria Akustyczna.
Jest to propozycja użytkowa, a nie oficjalny wzór wydziałowy.

Projekt opiera się na [inscrive-io/latex-report-template](https://github.com/inscrive-io/latex-report-template).
Zachowano oryginalną [licencję MIT](LICENSE) i informację o autorze.

## Struktura

- `main.tex` -- metadane, kolejność treści i opcjonalne elementy raportu.
- `style/universityreport.sty` -- pakiety, typografia, polonizacja i nagłówek tytułowy.
- `content/01-cel.tex` do `content/07-wnioski.tex` -- kolejne sekcje sprawozdania.
- `content/00-abstract.tex`, `content/appendix-a.tex` -- opcjonalne streszczenie i załącznik.
- `data/measurements.csv` -- demonstracyjne dane wspólne dla tabeli i wykresu.
- `references.bib` -- bibliografia BibLaTeX.
- `figures/` -- logo i własne ilustracje.
- `latexmkrc` -- konfiguracja kompilacji lokalnej i Overleaf.

Domyślny układ: `article`, 11 pt, A4, marginesy boczne 25 mm,
tytuł na pierwszej stronie, ciągła numeracja stron. Nie ma osobnej okładki,
abstraktu ani spisu treści. Opcjonalne elementy włącza się w `main.tex`.

## Metadane

Edytuj wywołania w `main.tex`:

| Polecenie | Znaczenie |
|---|---|
| `\reportinstitution{...}` | Uczelnia |
| `\reportfaculty{...}` | Wydział |
| `\reportprogramme{...}` | Kierunek |
| `\reportcourse{...}` | Przedmiot |
| `\reporttitle{...}` | Temat sprawozdania |
| `\reportlabnumber{...}` | Numer ćwiczenia |
| `\reportauthor{...}` | Autorzy, oddzieleni przecinkami |
| `\reportgroup{...}` | Grupa |
| `\reportinstructor{...}` | Prowadzący |
| `\reportdate{...}` | Data ćwiczenia lub oddania; domyślnie `\today` |
| `\reportlogo{...}` | Ścieżka do logo; `{}` wyłącza obraz |
| `\reporttype{...}` | Rodzaj dokumentu |
| `\reportsubtitle{...}` | Opcjonalny podtytuł |
| `\reportsemester{...}` | Opcjonalny semestr |
| `\reportmeta{...}` | Opcjonalne dodatkowe informacje |

Puste pola tabeli metadanych są pomijane. Tytuł i autorzy trafiają też do
właściwości PDF; używaj w nich zwykłego tekstu. Długie wartości w tabeli
metadanych są zawijane. Wymień pola przykładowe przed oddaniem raportu.

## Pisanie raportu

Pliki zapisuj w UTF-8. Używaj `\section` i `\subsection`, zamiast `\chapter`.
Dodaj sekcję przez utworzenie pliku w `content/` i dodanie `\input` w `main.tex`.
W raporcie technicznym ustaw `\reporttype{Raport techniczny}` w `main.tex`.

- Matematyka: `amsmath`, `mathtools`, `amsthm`, `libertinust1math`.
  Nie dodawaj `amssymb`: symbole AMS zapewnia font matematyczny.
- Jednostki: `\qty{1.25}{\metre}`, liczby: `\num{1.25}`;
  wejściowa kropka jest prezentowana jako przecinek.
- Tabele: `booktabs`, `tabularx`, kolumny `S` pakietu `siunitx`.
- Wykresy: TikZ, PGFPlots (`compat=1.18`), `pgfplotstable`.
  CSV używa przecinka między kolumnami i kropki dziesiętnej w danych.
- Odwołania: `\label{...}`, `\cref{...}` i `\Cref{...}` z polskimi nazwami.
- Cytowania: `\autocite{klucz}` lub `\textcite{klucz}`; styl `numeric-comp`,
  sortowanie nazwisko--rok--tytuł z polską lokalizacją.
- Kod: `listings`, z mapowaniem polskich liter w listingach.
- Dostępne ramki: `keybox`, `examplebox`, `alertbox`.
- Dla zgodności pozostały `widefigure` (obecnie szerokość tekstu)
  i `\sidenote{...}` (obecnie przypis dolny).

Dane i analiza akustyczna są wyłącznie demonstracją. Zastąp je rzeczywistymi
wynikami, budżetem niepewności i literaturą związaną z ćwiczeniem.
Bibliografia zawiera przykłady techniczne, nie bibliografię z akustyki.
Logo można zastąpić plikiem PDF, PNG lub JPG.

## Kompilacja lokalna

Wymagane: pdfLaTeX, Biber, latexmk i zgodny zestaw pakietów z TeX Live/MacTeX
lub MiKTeX. Zalecana pełna instalacja dystrybucji; instalacje minimalne
mogą wymagać doinstalowania pakietów. Potrzebne są polskie wzorce dzielenia
(`babel-polish` i konfiguracja języka polskiego), fonty Libertinus, Fira Sans,
Fira Mono oraz pakiety wymienione w `style/universityreport.sty`.
Wymagane `siunitx` 3 (polecenie `\qty`) i PGFPlots co najmniej 1.18.
Biber i BibLaTeX powinny pochodzić z tej samej, spójnej dystrybucji.

W katalogu głównym repozytorium:

```bash
latexmk -pdf main.tex
```

Wynik: `.output/main.pdf`. PDF i pliki pomocnicze trafiają domyślnie do
`.output/` dzięki konfiguracji `latexmkrc`. `latexmk` automatycznie uruchamia Biber i powtarza
pdfLaTeX do ustabilizowania odwołań. Nie wymaga `shell-escape`.

Można również wskazać katalog wynikowy jawnie:

```bash
latexmk -pdf -outdir=.output main.tex
```

Równoważna sekwencja ręczna (uruchamiana z katalogu głównego):

```bash
mkdir -p .output
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=.output main.tex
biber --input-directory=.output --output-directory=.output main
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=.output main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=.output main.tex
```

Usuwanie plików pomocniczych: `latexmk -c main.tex`.

## VS Code / LaTeX Workshop

Konfiguracja w `.vscode/settings.json` uruchamia pdfLaTeX + Biber przez
`latexmk` i zapisuje wyniki do `.output/`. Na macOS szuka narzędzi najpierw
w standardowym katalogu MacTeX `/Library/TeX/texbin`, następnie w lokalnej
instalacji `.output/texlive/bin/universal-darwin` oraz standardowym `PATH`.

Na tym komputerze przygotowano lokalną instalację w `.output/texlive`.
Jest ignorowana przez Git i nie jest częścią repozytorium ani archiwum
szablonu. Na innym komputerze zainstaluj dystrybucję TeX zgodnie z opisem
powyżej. Nie usuwaj całego `.output/`, jeżeli korzystasz z tej instalacji.
Po zmianie ustawień w VS Code wykonaj **Developer: Reload Window**,
a następnie **LaTeX Workshop: Build LaTeX project**.

Błąd `spawn latexmk ENOENT` oznacza, że edytor nie znajduje programu
`latexmk`; występuje przed rozpoczęciem kompilacji źródeł LaTeX.

## Overleaf

1. Zaimportuj ZIP repozytorium z zachowaniem struktury katalogów.
2. Ustaw główny dokument na `main.tex`, a kompilator na **pdfLaTeX**.
3. Wybierz aktualną dostępną wersję TeX Live i uruchom kompilację.

Plik `latexmkrc` pozostaw w katalogu głównym. Backend Biber jest określony
w stylu; nie należy przestawiać bibliografii na BibTeX.
Po zmianie wersji TeX Live lub backendu wykonaj kompilację od zera
(„Recompile from scratch”). Nie przesyłaj lokalnych plików pomocniczych.

## Licencja

Kod szablonu jest dostępny na [licencji MIT](LICENSE),
Copyright (c) 2026 Inscrive ApS. Informację o autorze i tekst licencji
należy zachować przy dalszej dystrybucji. Pliki logo AGH nie stanowią
przyznania praw do znaku uczelni.
