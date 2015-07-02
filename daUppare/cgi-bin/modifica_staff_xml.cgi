#!/usr/bin/perl -w

use XML::LibXML;
#use XML::LibXML::NodeList;
use XML::LibXML::XPathContext;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Cookie qw();
use CGI qw(:standard);
use DBI;
use File::Basename;
use utf8;

$title = 'Modifica staff';
$where = "Modifica staff";

require "session.cgi";

#lettura dei parametri
$page=new CGI;
if($admin){
my $id=$page->param('id');
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
my $old_source;
foreach $item(@items){
	my $idf=$item->find('id');
	if($idf eq $id){
		$old_source=$item->find('img/source');		
	}
}

$Xpath = "/../database/persona[id=\"$id\"]";
for my $dead ($doc ->findnodes ($Xpath)){
	$dead->unbindNode;
	open(OUT, ">$file");
	print OUT $doc->toString;
	close(OUT);
}

if($filename){
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
}
else {$filename=$old_source;}

my $xml_frag="
<persona>
	<id>$id</id>
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
#stampa del codice HTML
my $htmlprint;
require ("session.cgi");
require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
$htmlprint= "$header$menu<div id=\"content\">";
$htmlprint="$htmlprint
	<fieldset class='container'>
		<legend>Modifica in Corso...</legend>
		<p>Modifica avvenuta con successo</p>
		<p>Redirect Alla pagina di amministrazione</p>
		<META http-equiv='refresh' content='2;URL=admin_staff.cgi'>
	</fieldset>
	$footer
";
print $htmlprint;
}
else{
	print $page->redirect(-uri=>'index.cgi');
}
