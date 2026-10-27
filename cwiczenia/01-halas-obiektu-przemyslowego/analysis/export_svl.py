#!/usr/bin/env python3
"""Read the specific SVAN 971 / filesystem 1.07 files in this exercise.
Reference: manufacturer SVAN 971 manual, Appendix B, tables B.1.1–18,
B.2.1. This deliberately rejects unsupported configurations. No dependencies.
Raw inputs are never modified. Absolute seconds remain unresolved: the manual's
B.4 time formula appears inconsistent with two-second packed time; keep raw code.
"""
from pathlib import Path
import csv, hashlib, json, math, struct
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/processed'

def require(ok, message):
    if not ok: raise ValueError(message)

def read(path):
    data = path.read_bytes()
    require(len(data) % 2 == 0, 'Odd byte count')
    w = struct.unpack(f'<{len(data)//2}H', data)
    require(data[:6] == b'SvanPC', 'Missing SvanPC signature')
    blocks = {}; i = 16
    while i < len(w):
        size, tag = w[i] >> 8, w[i] & 255
        require(size > 0 and i+size <= len(w), 'Invalid header block')
        require(tag not in blocks, 'Duplicate header block')
        blocks[tag] = w[i:i+size]; i += size
        if tag == 15: break
    unit, settings, profiles, logger = [blocks[k] for k in (2,4,5,15)]
    require(unit[2] == 971 and unit[7] == 107, 'Unsupported model/filesystem')
    require(settings[3] == 3 and settings[14] == 0, 'Expected third octave, linear Leq')
    require(profiles[1] == 0x0307, 'Expected three active profiles')
    expected = ((1,2,15,2),(0,3,15,3),(1,1,15,1))
    require(tuple(tuple(profiles[j:j+4]) for j in (3,9,15)) == expected,
            'Unexpected Fast/A, Impulse/C, Fast/Z profiles or logger masks')
    require(logger[1:6] == (1,0,2000,31,3), 'Unexpected logger step/spectrum')
    require(i*2 + logger[6] + (logger[7]<<16) == len(data), 'Logger byte length mismatch')
    records = []; main = None; audio_frames = 0; frame_count = 0
    while i < len(w):
        h = w[i]
        if h & 0xf000 == 0x9000:
            n = w[i+1]
            require(n >= 4 and i+n <= len(w) and w[i+n-1] == h|0x800,
                    'Invalid audio frame boundary')
            audio_frames += 1; i += n
        elif h >> 8 == 0xc3:
            n = h & 255 or w[i+1]
            require(n >= 3 and i+n <= len(w) and w[i+n-1] == h|0x800,
                    'Invalid summary frame boundary')
            extra = 1 if h & 255 == 0 else 0
            payload = w[i+1+extra:i+n-1-extra]
            if payload and payload[0] & 255 == 7:
                require(main is None and len(payload) == 62, 'Unexpected main results')
                main = payload
            frame_count += 1; i += n
        elif h < 0x8000:
            require(i+47 <= len(w), 'Truncated logger record')
            records.append(w[i:i+47]); i += 47
        else:
            raise ValueError(f'Unsupported record at byte {2*i}: {h:#x}')
    require(main is not None, 'Missing main summary')
    require(len(records) == logger[8] + (logger[9]<<16) == 10, 'Record count mismatch')
    require(logger[10] + (logger[11]<<16) == len(records), 'Skipped logger records')
    require(main[3] + (main[4]<<16) == settings[11] + (settings[12]<<16) == 10,
            'Duration mismatch')
    require(all(all(abs(r[a]-r[b]) <= 1 for a,b in ((44,4),(45,8),(46,12))) for r in records),
            'Profile Leq and spectrum totals disagree')
    leq = 10*math.log10(sum(10**(r[4]/1000) for r in records)/len(records))
    summary = main[10]/100
    require(abs(leq-summary) <= .011, 'Logger energy mean and summary disagree')
    require(all(r[0] == 0 for r in records), 'Logger reports warning flags')
    require(all(main[j] & 2 == 0 for j in (21,41,61)), 'Summary overload')
    date, time = settings[1:3]
    cal = blocks[0x47]
    meta = dict(file=path.name,sha256=hashlib.sha256(data).hexdigest(),
        model=unit[2],serial_low_word=unit[1],firmware=unit[3],filesystem=unit[7],
        date=f'{2000+(date>>9):04d}-{(date>>5)&15:02d}-{date&31:02d}',
        start_time_code=time,start_hour=time//1800,start_minute=(time//30)%60,
        time_note='Seconds unresolved: manual B.4 gives code%30; two-second encoding gives 2*(code%30). No timezone stored.',
        duration_s=10,logger_step_s=1,logger_records=len(records),
        LAeq_dB=summary,LAFmax_dB=main[7]/100,LAFmin_dB=main[8]/100,
        LCeq_dB=main[30]/100,LZeq_dB=main[50]/100,
        LAeq_from_logger_dB=leq,consistency_error_dB=leq-summary,
        audio_frames=audio_frames,summary_frames=frame_count,
        pre_calibration_type=cal[1],pre_calibration_date_code=cal[2],
        pre_calibration_time_code=cal[3],pre_calibration_factor_dB=cal[4]/100,
        post_calibration_type=cal[5],assignment='unconfirmed')
    rows = [dict(file=path.name,second=k+1,flags=r[0],LAeq_dB=r[4]/100,
                 LAFmax_dB=r[2]/100,LAFmin_dB=r[3]/100,
                 LCeq_dB=r[8]/100,LZeq_dB=r[12]/100)
            for k,r in enumerate(records)]
    return meta, rows

def write_csv(name, rows):
    with (OUT/name).open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)

if __name__ == '__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    results = [read(p) for p in sorted((ROOT/'data/raw').glob('*.SVL'))]
    require(bool(results),'No SVL files')
    metadata=[m for m,_ in results]
    write_csv('svl_summary.csv',metadata)
    write_csv('svl_logger_1s.csv',[r for _,rows in results for r in rows])
    (OUT/'svl_metadata.json').write_text(json.dumps(metadata,indent=2,ensure_ascii=False)+'\n')
    for m in metadata:
        print(f"{m['file']}: LAeq={m['LAeq_dB']:.2f} dB, "
              f"duration={m['duration_s']} s, error={m['consistency_error_dB']:+.5f} dB")
