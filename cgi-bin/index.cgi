#!"C:\strawberry\perl\bin\perl.exe"
use XML::LibXML;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser);
use utf8;


$title="Home";
$where="<span lang=\"en\">Home</span>";
#!"C:\xampp\perl\bin\perl.exe"
require ("session.cgi");
require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
$page = new CGI;
print $page->header;
#$utente= getSession();



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
$htmlprint= "$header$menu<div id=\"content\">";

if (length $admin){
	$htmlprint=$htmlprint.'<div id="editindex"><a href="editindex.cgi" tabindex="9"><button class="pulsante">Modifica informazioni</button></a></div>'
}
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
$htmlprint="$htmlprint</div>$footer";
print $htmlprint;










