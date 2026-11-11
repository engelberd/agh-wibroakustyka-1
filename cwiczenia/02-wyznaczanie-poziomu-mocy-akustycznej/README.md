# Wyznaczanie poziomu mocy akustycznej

Raport ma dwie numerowane części: kwalifikację pomieszczenia metodą
przybliżoną (alfa=0,15) oraz oszacowanie mocy dla środka, ściany i rogu.
Treść edytuj w `content/02-kwalifikacja.tex` i `content/04-moc.tex`.

Notatki z przypisaniem plików: `data/raw/notatki-pomiarowe.csv`.
Oryginalne rejestracje: `data/raw/29_10/`. Pozostałe SVL są nieprzypisane.
Inwentaryzacja z SHA256: `data/processed/svl-inventory.csv`.
Wyniki obliczeń: `data/processed/report-results.json`; tabele i wartości
LaTeX: `generated/`. Nie edytuj ich ręcznie, uruchom ponownie analizę.
Lista brakujących ustaleń: `analysis/do-uzupelnienia.md`.

```bash
python3 cwiczenia/02-wyznaczanie-poziomu-mocy-akustycznej/analysis/export_svl.py
python3 cwiczenia/02-wyznaczanie-poziomu-mocy-akustycznej/analysis/prepare_report.py
python3 scripts/report.py build 02-wyznaczanie-poziomu-mocy-akustycznej
```

Poziomy w tabelach pochodzą z przypisanych plików SVL (LAeq).
Notatki służą wyłącznie do przypisania punktów; ich poziomy odpowiadają LAE
z dokładnością do zaokrąglenia. Profile A/C/Z i czas 15 s potwierdzono w nagłówkach.
Eksport obejmuje `svl_summary.csv`, `svl_logger_1s.csv` i `svl_metadata.json`.
Parser kontroluje granice bloków, długości danych, konfigurację profili, flagi
przeciążenia, liczbę rekordów i zgodność średnich A/C/Z oraz LAE z czasem.
Wyniki: około 90,11 dB (środek), 90,10 dB (ściana), 90,33 dB (róg).
Model: d=1 m, źródło dosunięte do przegród, dłuższy bok przy ścianie,
równe wagi punktów i wspólne tło P38. Przy ścianie są trzy potwierdzone
punkty; nie dopisywano czwartego. Nie potwierdzono pełnej zgodności normowej.
Pełny przegląd plików: `analysis/audit_svl.py` i `data/processed/svl-audit.csv`.
