#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser);
use utf8;
require("session.cgi");

$page = new CGI;
if(length $admin){
$title="Home";
$where="<span lang=\"en\">Edit Home</span>";

require("header.cgi");
require("menu.cgi");
my $htmlprint;
require ("footer.cgi");

print $page->header;
$parser = XML::LibXML->new();
my $file = "../data/index.xml";
my $doc = $parser->parse_file($file);
	if(!$doc){
		$ERRORE=1;
	}

my $root = $doc->getDocumentElement;
@items = $root->getElementsByTagName('frame');
$item=@items;
	

$htmlprint= "$header$menu<div id=\"content\">";

$htmlprint=$htmlprint."<form action='check_editindex.cgi' method='post'><fieldset>";
foreach $item(@items){
		my $titolo=$item->find('titolo');
		my $corpo=$item->find('corpo');
		my $id=$item->find('id');
		$htmlprint="$htmlprint
			
			<div id='colonna_$id' class='colonna'>
			<label class=\"label_block\" for='titolo_$id'>Titolo</label>
			<input type='text' id='titolo_$id' name='titolo_$id' value='$titolo'/>
			<label class=\"label_block\" for='corpo_$id'>Contenuto</label>
			<textarea class='inputcorpo' id='corpo_$id' name='corpo_$id' rows=\"20\" cols=\"40\">$corpo</textarea>
			</div>
		";
}
	$htmlprint="$htmlprint <input type='submit' class='pulsante modifica' name='modifica' value='Modifica'/><input type='submit' class='pulsante annulla' name='annulla' value='Annulla'/></fieldset></form>";
require("footer.cgi");
$htmlprint="$htmlprint</div>$footer";
print $htmlprint;
}
else {
	print $page->redirect(-uri=>'index.cgi');
}











