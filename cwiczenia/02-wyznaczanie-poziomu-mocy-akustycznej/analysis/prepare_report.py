"""Obliczenia z LAeq w SVL; notatki służą do przypisania punktów."""
from pathlib import Path
import csv, json, math, hashlib
ROOT = Path(__file__).resolve().parents[1]
from export_svl import read
rows = list(csv.DictReader((ROOT/'data/raw/notatki-pomiarowe.csv').open()))
for row in rows:
    meta, _ = read(ROOT/'data/raw/29_10'/(row['plik']+'.SVL'))
    row['poziom_dB'] = str(meta['LAeq_dB'])
    if row['opis'] == 'do ustalenia':
        row['opis'] = 'punkt ' + str(int(row['plik'][1:])-(49 if row['polozenie']=='rog' else 52))
V = 5*8*3.3
Sv = 2*(5*8+5*3.3+8*3.3)
alpha = .15
A = alpha*Sv
a,b,c = 1.24,1.13,1.18
S = 4*(a*b+a*c+b*c)
K2 = 10*math.log10(1+4*S/A)
means = {p:10*math.log10(sum(10**(float(r['poziom_dB'])/10) for r in rows if r['polozenie']==p and r['rola']=='zrodlo')/sum(r['polozenie']==p and r['rola']=='zrodlo' for r in rows)) for p in ('srodek','rog','sciana')}
# User confirmed the 48 cm side against the wall. Contact with reflecting
# planes, d=1 m and equal point weights are explicit model assumptions.
surfaces = {'srodek': S, 'sciana': (0.48+2)*(0.26+1)+(0.48+2)*c+2*(0.26+1)*c,
            'rog': (0.48+1)*(0.26+1)+(0.48+1)*c+(0.26+1)*c}
background = next(float(r['poziom_dB']) for r in rows if r['rola']=='tlo')
final = {}
for position, surface in surfaces.items():
    delta = means[position]-background
    k1 = 0 if delta > 10 else -10*math.log10(1-10**(-delta/10))
    k2 = 10*math.log10(1+4*surface/A)
    final[position] = dict(S_m2=surface,LAeq_dB=means[position],background_dB=background,
        delta_L_dB=delta,K1A_dB=k1,K2A_dB=k2,LWA_estimate_dB=means[position]-k1-k2+10*math.log10(surface),
        source_points=sum(r['polozenie']==position and r['rola']=='zrodlo' for r in rows))
result = dict(V_m3=V,Sv_m2=Sv,alpha=alpha,A_m2=A,a_m=a,b_m=b,c_m=c,S_srodek_m2=S,K2_srodek_dB=K2,mean_levels_dB=means,estimates=final,notes='Model: contact with reflecting planes, d=1 m, long side against wall, equal point weights, common P38 background. Wall has only three confirmed points. Estimates do not establish full ISO conformity.')
(ROOT/'data/processed/report-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
fmt=lambda x: f'{x:.2f}'
bs=chr(92)
tex='\n'.join(bs+'newcommand{'+bs+name+'}{'+bs+'num{'+fmt(value)+'}}' for name,value in [('roomVolume',V),('roomSurface',Sv),('roomAbsorption',A),('measurementSurface',S),('environmentCorrection',K2)])+'\n'
(ROOT/'generated/values.tex').write_text(tex)
names={'srodek':'Środek','rog':'Róg','sciana':'Ściana'}
(ROOT/'generated/measurement-rows.tex').write_text('\n'.join(f"{names[r['polozenie']]} & {r['plik']} & {r['opis']} & " + bs+'num{'+r['poziom_dB']+'} '+bs*2 for r in rows)+'\n')
(ROOT/'generated/mean-rows.tex').write_text('\n'.join(f"{names[p]} & {sum(r['polozenie']==p and r['rola']=='zrodlo' for r in rows)} & " + bs+'num{'+fmt(v)+'} '+bs*2 for p,v in means.items())+'\n')
for name in ('measurement-rows.tex', 'mean-rows.tex'):
    p = ROOT/'generated'/name
    p.write_text(p.read_text()+bs+'bottomrule'+chr(10))
files=sorted((ROOT/'data/raw/29_10').glob('*.SVL'))
with (ROOT/'data/processed/svl-inventory.csv').open('w') as f:
 w=csv.writer(f,lineterminator='\n');w.writerow(['file','size_bytes','sha256','assignment'])
 assignment={r['plik']+'.SVL':r['polozenie']+': '+r['rola']+'; '+r['opis'] for r in rows}
 for p in files:w.writerow([p.name,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest(),assignment.get(p.name,'nieprzypisany')])
print(json.dumps(result,ensure_ascii=False,indent=2))

(ROOT/'generated/final-rows.tex').write_text('\n'.join(f"{names[p]} & {v['source_points']} & " + ' & '.join(bs+'num{'+fmt(v[k])+'}' for k in ('S_m2','LAeq_dB','K1A_dB','K2A_dB','LWA_estimate_dB'))+' '+bs*2 for p,v in final.items())+'\n'+bs+'bottomrule\n')
