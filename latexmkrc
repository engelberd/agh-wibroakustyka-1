# pdfLaTeX; latexmk detects biblatex's .bcf and runs Biber automatically.
$pdf_mode = 1;
# Keep generated files together; command-line -outdir can override this.
$out_dir = '.output';
$aux_dir = $out_dir;
$bibtex_use = 2;
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$clean_ext = 'bbl run.xml synctex.gz nav snm vrb';
