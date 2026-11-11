"""Audit all raw SVL; do not infer spatial assignments from similar levels."""
from pathlib import Path
import csv
from export_svl import read
ROOT = Path(__file__).resolve().parents[1]
assigned = {r['plik']+'.SVL':r['polozenie']+': '+r['rola'] for r in csv.DictReader((ROOT/'data/raw/notatki-pomiarowe.csv').open())}
rows = []
for p in sorted((ROOT/'data/raw/29_10').glob('*.SVL')):
    row = dict(file=p.name,assignment=assigned.get(p.name,'niepotwierdzone'),status='ok',date='',hour='',minute='',time_code='',duration_s='',configured_duration_s='',LAeq_dB='',LCeq_dB='',LZeq_dB='',LAFmin_dB='',LAFmax_dB='',error='')
    try:
        meta, _ = read(p)
        for key in ('date','duration_s','configured_duration_s','LAeq_dB','LCeq_dB','LZeq_dB','LAFmin_dB','LAFmax_dB'):
            row[key] = meta[key]
        row.update(hour=meta['start_hour'],minute=meta['start_minute'],time_code=meta['start_time_code'])
        if meta['stopped_early']: row['status'] = 'shortened'
    except ValueError as e:
        row.update(status='rejected',error=str(e))
    rows.append(row)
with (ROOT/'data/processed/svl-audit.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
print(f"Audited {len(rows)} files; rejected {sum(r['status']=='rejected' for r in rows)}")
