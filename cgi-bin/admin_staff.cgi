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
$page=new CGI;

$parser = XML::LibXML->new();
my $file = "../data/staff.xml";
my $doc = $parser->parse_file($file);

my $root= $doc->getDocumentElement;
@items = $root->getElementsByTagName('persona');
my $h_opt='';

foreach $item(@items){
	my $id=$item->find('id');
	my $nome=$item->find('nome');
	my $cognome=$item->find('cognome');
	$h_opt="$h_opt\n <option value='$id'>$nome $cognome</option>";
}
	
print($page->header());

my $htmlprint;
require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
$htmlprint= "$header$menu<div id=\"content\">";
$htmlprint="$htmlprint
	<h3 class='SubTitle'>Amministrazione-Staff</h3>
	<div id='inserisci'>
	<fieldset class='container form-group'>
		<legend><h4>Inserisci</h4></legend>
		<form action='inserisci_staff.cgi' method='POST' enctype='multipart/form-data'>
			<p><label class='label'>Nome:</label><input type='text' name='nome'/></p>
			<p><label class='label'>Cognome:</label><input type='text' name='cognome'/></p>
			<p><label class='label'>Ruolo:</label><input type='text' name='ruolo'/></p>
			<p><label class='label'>Foto:</label><input type='file' name='foto' accept='image/*'/></p>
			
			<input type='submit' value='Aggiungi'/>
		</form>
	</fieldset>
	</div>
	<div id='modifica'>
	<fieldset class='container  form-group'>
		<legend><h4>Modifica</h4></legend>
		<form action='modifica_staff.cgi' method='POST'>
			<p><select name='staff'>
				$h_opt
			</select></p>
			<input type='submit' value='Modifica'/>
		</form>
	</fieldset>
	</div>
	<div id='elimina'>
	<fieldset class='container  form-group'>
		<legend><h4>Elimina</h4></legend>
		<form action='elimina_staff.cgi' method='POST'>
			<p><select name='staff'>
				$h_opt
			</select></p>
			<input type='submit' value='Elimina'/>
		</form>
	</fieldset>
	</div>
	<div id='break'></div>
	$footer";
print($htmlprint);