# Wyznaczanie poziomu mocy akustycznej

Ćwiczenie 2: jeden raport łączący kwalifikację pomieszczenia i pomiar mocy
akustycznej metodą orientacyjną. To szkielet do uzupełnienia, bez wyników.
Autorzy, grupa i prowadzący pochodzą z ćwiczenia 1; datę ustal w `main.tex`.

## Materiały i katalogi

- `konspekty/`: obie oryginalne instrukcje, wymienione w bibliografii.
- `content/`: cel, teoria, obiekt i aparatura, metodyka obu części, wyniki,
  niepewność oraz wnioski. Pola do uzupełnienia oznaczono `\todo{...}`.
- `data/raw/`: oryginalne rejestracje, czasy pogłosu i protokoły pomiarowe.
- `data/processed/`: uporządkowane dane i wyniki obliczeń.
- `analysis/`: skrypty analizy.
- `figures/`: szkic pomieszczenia, powierzchnie i punkty pomiarowe, zdjęcia.
- `generated/`: wygenerowane tabele i wykresy do raportu.

Najpierw uzupełnij geometrię pomieszczenia i źródła, pomiary pogłosu,
poziomy źródła z tłem i samego tła dla trzech położeń źródła. Zachowaj
rozróżnienie pasm oktawowych pogłosu i tercjowych pomiarów źródła.
Kwalifikację przygotuj dla powierzchni prostopadłościennej i półsferycznej.
Konspekty zawierają rozbieżne zakresy odległości pomiarowej; udokumentuj
faktycznie zastosowany wariant. Wyniki i kryteria opracuj według materiałów
zajęciowych, odnotowując ewentualne uzgodnienia z prowadzącym.

## Kompilacja i eksport (z katalogu głównego)

```bash
python3 scripts/report.py build 02-wyznaczanie-poziomu-mocy-akustycznej
python3 scripts/report.py export 02-wyznaczanie-poziomu-mocy-akustycznej
```
