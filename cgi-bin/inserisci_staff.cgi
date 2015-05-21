#!"C:\strawberry\perl\bin\perl.exe"

use XML::LibXML;
use XML::LibXML::NodeList;
use XML::LibXML::XPathContext;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Cookie qw();
use CGI qw(:standard);
use DBI;
use File::Basename;
use utf8;

#verifica della sessione
sub getSession(){
	$session = CGI::Session->load() or die $!;
	if($session->is_expired || $session->is_empty){
		return undef;
	}
	else{
		my $admin = $session->param('admin');
		$session;
	}
}
my $session=getSession;

#lettura dei parametri
$page=new CGI;
my $nome=$page->param('nome');
my $cognome=$page->param('cognome');
my $ruolo=$page->param('ruolo');
my $filename = $page->param("foto");

#apertura del file staff.xml
$parser = XML::LibXML->new();
my $file = "../data/staff.xml";
my $doc = $parser->parse_file($file);

my $root= $doc->getDocumentElement;
@items = $root->getElementsByTagName('persona');
$newid=1;
foreach $item(@items){ #ciclo per trovare il numero di id
	$temp=$item->findvalue('id');
	if($temp>$maxid){
		$newid=$temp+1;
	}
}
my $xml_frag="
<persona>
	<id>$newid</id>
	<nome>$nome</nome>
	<cognome>$cognome</cognome>
	<ruolo>$ruolo</ruolo>
	<img>
		<source>$filename</source>
		<alt>Foto di $nome $cognome</alt>
	</img>
</persona>";
my $nodo = $parser->parse_balanced_chunk($xml_frag) || die("frammento non ben formato");
$root->appendChild($nodo) || die("non riesco a trovare il padre");
open(OUT, ">$file");
print OUT $doc->toString;
close(OUT);	
print($page->header());

#upload del file immagine
$CGI::POST_MAX = 1024 * 5000;
my $safe_filename_characters = "a-zA-Z0-9_.-";
my $upload_dir = "../public_html/img/avatars";
if ( !$filename ){
	print $page->header ( );
	print "There was a problem uploading your photo (try a smaller file).";
	exit;
}
my ( $name, $path, $extension ) = fileparse ( $filename, '..*' );
$filename = $name . $extension;
$filename =~ tr/ /_/;
$filename =~ s/[^$safe_filename_characters]//g;
if ( $filename =~ /^([$safe_filename_characters]+)$/ ){$filename = $1;}
else{die "Filename contains invalid characters";}
my $upload_filehandle = $page->upload("foto");
open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";
binmode UPLOADFILE;
while ( <$upload_filehandle> ){print UPLOADFILE;}
close UPLOADFILE;
print $page->header ( );

#stampa del codice HTML
my $htmlprint;

require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
$htmlprint= "$header$menu<div id=\"content\">";
$htmlprint="$htmlprint
	<fieldset class='container'>
		<legend><h4>Inserimento in Corso...</h4></legend>
		<p>Inserimento Avvenuto con successo</p>
		<p>Redirect Alla pagina di amministrazione</p>
		<META http-equiv='refresh' content='2;URL=admin_staff.cgi'>
	</fieldset>
	$footer
";
print $htmlprint;