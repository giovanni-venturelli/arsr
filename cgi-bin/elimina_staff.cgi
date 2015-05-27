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
use utf8;

$title = 'Elimina staff';
$where = "Elimina staff";

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
my $id=$page->param('staff');

#apertura del file staff.xml
$parser = XML::LibXML->new();
my $file = "../data/staff.xml";
my $doc = $parser->parse_file($file);
my $root= $doc->getDocumentElement;
@items = $root->getElementsByTagName('persona');
my $Xpath = "/Database/persona[id=\"$id\"]";
for my $dead ($doc ->findnodes ($Xpath)){ 
	$dead->unbindNode;
	open(OUT, ">$file");
	print OUT $doc->toString;
	close(OUT);
}
print($page->header());
#stampa del codice HTML
my $htmlprint;

require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
$htmlprint= "$header$menu<div id=\"content\">";
$htmlprint="$htmlprint
	<fieldset class='container'>
		<legend><h4 class='legend'>Eliminazione in Corso...</h4></legend>
		<p>Eliminazione avvenuta con successo</p>
		<p>Redirect Alla pagina di amministrazione</p>
		<META http-equiv='refresh' content='2;URL=admin_staff.cgi'>
	</fieldset>
	</div>
	$footer
";
print $htmlprint;