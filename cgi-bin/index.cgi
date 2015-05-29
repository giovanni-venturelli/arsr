#!"C:\strawberry\perl\bin\perl.exe"
use XML::LibXML;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser);
use utf8;

print "content-type: text/html\n\n";
$title="Home";
$where="home";
require("header.cgi");
require("menu.cgi");
$page = new CGI;
$utente= getSession();



$parser = XML::LibXML->new();
my $file = "../data/index.xml";
my $doc = $parser->parse_file($file);
	if(!$doc){
		$ERRORE=1;
	}

my $root = $doc->getDocumentElement;
@items = $root->getElementsByTagName('frame');
$item=@items;
	
my $htmlprint;
require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
$htmlprint= "$header$menu<div id=\"content\">";


foreach $item(@items){
		my $titolo=$item->find('titolo');
		my $corpo=$item->find('corpo');
		my $id=$item->find('id');
		$htmlprint="$htmlprint
			<div id='colonna_$id' class='colonna'>
			<h3>$titolo</h3>
				<p>$corpo</p>
			</div>
		";
}
require("footer.cgi");
$htmlprint="$htmlprint$footer";
print $htmlprint;










