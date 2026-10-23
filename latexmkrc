# Shared pdfLaTeX + Biber configuration. Build from root or exercise folder.
use Cwd qw(abs_path);
use File::Basename qw(dirname);
use File::Spec;
my $root = dirname(abs_path(__FILE__));
my $sep = ($^O eq 'MSWin32') ? ';' : ':';
$ENV{'TEXINPUTS'} = File::Spec->catdir($root, 'shared', 'style') . '//'
    . $sep . ($ENV{'TEXINPUTS'} // '');
my $localtex = File::Spec->catdir($root, '.output', 'texlive', 'bin', 'universal-darwin');
$ENV{'PATH'} = $localtex . $sep . $ENV{'PATH'} if -d $localtex;
$pdf_mode = 1;
$do_cd = 1;
$out_dir = '.output';
$aux_dir = $out_dir;
$bibtex_use = 2;
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$clean_ext = 'bbl run.xml synctex.gz nav snm vrb';
1;
