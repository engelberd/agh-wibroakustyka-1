#!/usr/bin/env python3
"""Create, build and export independent laboratory reports (standard library only)."""
import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def exercise(value):
    path = (ROOT / 'cwiczenia' / value).resolve()
    if path.parent != (ROOT / 'cwiczenia').resolve() or not (path / 'main.tex').is_file():
        raise SystemExit('Nie znaleziono ćwiczenia: ' + value)
    return path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    new = commands.add_parser('new', help='Utwórz ćwiczenie z template/')
    new.add_argument('name', help='Np. 02-drgania-swobodne')
    new.add_argument('--title', required=True)
    new.add_argument('--number', required=True, type=int)
    for action in ('build', 'export'):
        commands.add_parser(action).add_argument('name')
    args = parser.parse_args()
    if args.command == 'new':
        if not re.fullmatch(r'[0-9]{2,}-[a-z0-9]+(?:-[a-z0-9]+)*', args.name):
            parser.error('Nazwa powinna mieć postać 02-nazwa-cwiczenia (bez polskich znaków).')
        if args.number < 1 or any(c in args.title for c in '\\{}%&#_$^~\n\r'):
            parser.error('Podaj dodatni numer i tytuł jako zwykły tekst bez znaków specjalnych LaTeX.')
        dest = ROOT / 'cwiczenia' / args.name
        if dest.exists():
            parser.error('Katalog już istnieje: ' + str(dest))
        shutil.copytree(ROOT / 'template', dest, ignore=shutil.ignore_patterns('.output', '__pycache__'))
        p = dest / 'main.tex'
        p.write_text(p.read_text().replace(r'\reporttitle{Temat ćwiczenia}', r'\reporttitle{' + args.title + '}').replace(r'\reportlabnumber{Numer ćwiczenia}', r'\reportlabnumber{' + str(args.number) + '}'))
        (dest / 'latexmkrc').write_text("my $result = do '../../latexmkrc';\n" + 'die "Cannot load shared latexmkrc: $@ $!" unless defined $result;\n')
        print(dest)
    elif args.command == 'build':
        path = exercise(args.name)
        env = os.environ.copy()
        env['PATH'] = os.pathsep.join([str(ROOT / '.output/texlive/bin/universal-darwin'), '/Library/TeX/texbin', env.get('PATH', '')])
        tool = shutil.which('latexmk', path=env['PATH'])
        if not tool:
            raise SystemExit('Brak latexmk. Zainstaluj TeX Live / MacTeX i dodaj go do PATH.')
        subprocess.run([tool, '-pdf', 'main.tex'], cwd=path, env=env, check=True)
    else:
        path = exercise(args.name)
        target = ROOT / '.output/exports' / (args.name + '.zip')
        target.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
            for p in sorted(path.rglob('*')):
                rel = p.relative_to(path)
                if not p.is_file() or any(x.startswith('.') or x == '__pycache__' for x in rel.parts) or rel.as_posix() == 'latexmkrc':
                    continue
                archive.write(p, rel)
            archive.write(ROOT / 'shared/style/universityreport.sty', 'universityreport.sty')
            archive.write(ROOT / 'figures/agh_small.jpg', 'agh_small.jpg')
            archive.write(ROOT / 'LICENSE', 'LICENSE')
            archive.writestr('latexmkrc', "$pdf_mode = 1;\n$bibtex_use = 2;\n")
        print(target)

if __name__ == '__main__':
    main()
