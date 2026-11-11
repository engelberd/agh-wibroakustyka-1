"""Compare Sabine qualification (T20) with alpha-based qualification.
Only the 1 kHz third-octave T20 estimates are analysed.
Series z1/z2 interpreted per user's two-microphone / six-source description.
"""
from pathlib import Path
from statistics import mean, stdev
import csv, json, math, hashlib
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'data/raw/grupa 1 Wibro tech 11 30'
bs=chr(92)
def num(v):return bs+'num{'+f'{v:.3f}'+'}'
def table(name,rows):
    (ROOT/'generated'/name).write_text('\n'.join(' & '.join(row)+' '+bs*2 for row in rows)+'\n'+bs+'bottomrule\n')
records=[]; provenance=[]
for p in sorted(SOURCE.glob('*.txt')):
    lines=[line.split('\t') for line in p.read_text(encoding='utf-8-sig').splitlines()]
    freqs=[float(x.replace(',','.')) for x in lines[0][2:] if x]
    assert len(freqs)==30 and len(set(freqs))==30, p
    keys={'T20 [s]','T20 cc [-]'}
    data={line[0]:line[2:2+len(freqs)] for line in lines[1:] if line[0] in keys}
    assert all(len(v)==len(freqs) for v in data.values()),p
    assert all(k in data for k in ['T20 [s]','T20 cc [-]'])
    provenance.append(dict(file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    i=freqs.index(1000.)
    row=dict(file=p.name,series=p.stem[:2],source_index=int(p.stem[-1]),frequency_Hz=1000.)
    for key in ('T20 [s]', 'T20 cc [-]'):
        value=data[key][i]
        assert value!='--', (p,key)
        row[key]=float(value.replace(',','.'))
    records.append(row)
assert len(provenance)==12
assert {x['file'] for x in provenance}=={f'z{z}m{m}.txt' for z in (1,2) for m in range(1,7)}
def write_csv(name,rows):
    with (ROOT/'data/processed'/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
write_csv('reverberation-1khz.csv',records)
V=132.; Sv=165.8; A_approx=.15*Sv
surfaces={'srodek':16.7912,'sciana':9.0248,'rog':5.098}
averages=[]
for frequency in [1000.]:
    selected=[x for x in records if x['frequency_Hz']==frequency]
    valid=[x['T20 [s]'] for x in selected if x['T20 [s]'] is not None and x['T20 [s]']>0]
    assert valid
    T=mean(valid);A=.16*V/T
    row=dict(frequency_Hz=frequency,n=len(valid),T20_mean_s=T,T20_sd_s=stdev(valid),A_m2=A)
    for series in ['z1','z2']:
        v=[x['T20 [s]'] for x in selected if x['series']==series and x['T20 [s]'] is not None and x['T20 [s]']>0]
        row[series+'_T20_mean_s']=mean(v) if v else None
    for name,S in surfaces.items():row['K2_'+name+'_dB']=10*math.log10(1+4*S/A)
    averages.append(row)

at1k=[x for x in records if x['frequency_Hz']==1000]
assert len(at1k)==12 and all(x['T20 [s]']>0 and abs(x['T20 cc [-]'])>=.99 for x in at1k)
a1k=next(x for x in averages if x['frequency_Hz']==1000)
comparison={name:dict(S_m2=S,K2_approx_dB=10*math.log10(1+4*S/A_approx),K2_reverb_dB=a1k['K2_'+name+'_dB']) for name,S in surfaces.items()}
summary=dict(method='T20; Sabine coefficient 0.16; mean over 12 spatial combinations',at_1kHz=a1k,A_approx_m2=A_approx,alpha_equivalent_1kHz=a1k['A_m2']/Sv,comparison=comparison,files=provenance,layout_note='Series z1/z2 assigned to microphone settings M1/M2 according to user; six files per series represent successive source positions; no measured coordinates available.')
(ROOT/'data/processed/reverberation-results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
table('reverb-measurements.tex',[[str(i)]+[num(next(x for x in records if x['series']==series and x['source_index']==i)['T20 [s]']) for series in ('z1','z2')] for i in range(1,7)])
names={'srodek':'Środek','sciana':'Ściana','rog':'Róg'}
table('reverb-comparison.tex',[[names[k],num(v['K2_approx_dB']),num(v['K2_reverb_dB']),num(v['K2_reverb_dB']-v['K2_approx_dB'])] for k,v in comparison.items()])
(ROOT/'generated/reverb-values.tex').write_text('\n'.join(bs+'newcommand{'+bs+n+'}{'+num(v)+'}' for n,v in [('reverbTime',a1k['T20_mean_s']),('reverbAbsorption',a1k['A_m2']),('reverbCorrection',a1k['K2_srodek_dB']),('reverbAlpha',a1k['A_m2']/Sv)])+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='files'},ensure_ascii=False,indent=2))
