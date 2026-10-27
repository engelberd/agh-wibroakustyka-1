#!/usr/bin/env python3
"""Generate exercise tables from original SVL files; all 10 samples retained."""
import csv
import json
import math
from pathlib import Path
from export_svl import read
ROOT=Path(__file__).resolve().parents[1]

def mean(levels):
    return 10*math.log10(sum(10**(x/10) for x in levels)/len(levels))
def required(r):
    for upper,n in ((1,3),(1.5,4),(2,5),(2.5,6),(3,7)):
        if r<=upper+1e-10:return n
    return None

def pl(x):return f'{x:.2f}'.replace('.',',')

def main():
    station_names=[f'P{i:02}' for i in range(4,9)]
    background_names=[f'P{i:02}' for i in range(10,15)]
    rows={name:read(ROOT/'data/raw'/f'{name}.SVL')[0] for name in station_names+background_names}
    station=[rows[n]['LAeq_dB'] for n in station_names]
    background=[rows[n]['LAeq_dB'] for n in background_names]
    lm,lt=mean(station),mean(background)
    corrected=10*math.log10(10**(lm/10)-10**(lt/10))
    summary=dict(station_mean_dB=lm,background_mean_dB=lt,difference_dB=lm-lt,
                 corrected_dB=corrected,station_range_dB=max(station)-min(station),
                 background_range_dB=max(background)-min(background),
                 station_n=5,background_n=5,
                 station_required_n=required(max(station)-min(station)),
                 background_required_n=required(max(background)-min(background)))
    generated=ROOT/'generated';processed=ROOT/'data/processed'
    generated.mkdir(exist_ok=True);processed.mkdir(parents=True,exist_ok=True)
    with (processed/'report-series.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['sample','station_file','station','background_file','background'])
        for i,(a,b) in enumerate(zip(station_names,background_names),1):
            w.writerow([i,a,rows[a]['LAeq_dB'],b,rows[b]['LAeq_dB']])
    (processed/'report-results.json').write_text(json.dumps(summary,indent=2)+'\n')
    (generated/'probki-rows.tex').write_text('\n'.join(
        f'{a} & {pl(rows[a]["LAeq_dB"])} & {b} & {pl(rows[b]["LAeq_dB"])} '+r'\\'
        for a,b in zip(station_names,background_names))+'\n')
    lines=[f'Średnia energetyczna [dB] & {pl(lm)} & {pl(lt)}',
           f'Rozstęp $R$ [dB] & {pl(summary["station_range_dB"])} & {pl(summary["background_range_dB"])}',
           r'Liczba wykonanych próbek & 5 & 5',
           f'Wymagana liczba próbek & {summary["station_required_n"]} & {summary["background_required_n"]}',
           r'Kryterium liczby próbek & spełnione & niespełnione']
    (generated/'podsumowanie-rows.tex').write_text('\n'.join(s+' '+r'\\' for s in lines)+'\n')
    (generated/'korekcja-wynik.tex').write_text(
        f'Różnica średnich poziomów wyniosła $\\Delta L={pl(lm-lt)}\\,\\mathrm{{dB}}$.\n'
        f'Po podstawieniu do wzoru~\\eqref{{eq:korekcja-tla}} otrzymano\n'
        f'\\begin{{equation}}\n L_{{Aek}}={pl(corrected)}\\,\\mathrm{{dB}}.\n\\end{{equation}}\n')
    tables={
        'probki-rows.tex': (r'\begin{tabular}{@{}lrlr@{}}',r'Plik: stacja & $L_{Aeq,10s}$ [dB] & Plik: tło & $L_{Aeq,10s}$ [dB]'),
        'podsumowanie-rows.tex': (r'\begin{tabular}{@{}lrr@{}}',r'Wielkość & Przy stacji & Tło')}
    for name,(begin,header) in tables.items():
        p=generated/name
        body=p.read_text()
        p.write_text(begin+'\n'+r'\toprule'+'\n'+header+' '+r'\\'+'\n'+r'\midrule'+'\n'+body+r'\bottomrule'+'\n'+r'\end{tabular}'+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
