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

$title = 'Admin Staff';
$where = "Admin Staff";

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
	
require ("session.cgi");
require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
$page = new CGI;
print $page->header;

my $htmlprint;
$htmlprint= "$header$menu<div id=\"content\">";
if (length $admin){
	$htmlprint="$htmlprint
	<div id='inserisci'>	
		<form action='inserisci_staff.cgi' method='post' enctype='multipart/form-data'>
			<fieldset class='container form-group'>
				<legend>Inserisci</legend>
				<p><label class='label'>Nome:</label><input type='text' name='nome'/></p>
				<p><label class='label'>Cognome:</label><input type='text' name='cognome'/></p>
				<p><label class='label'>Ruolo:</label><input type='text' name='ruolo'/></p>
				<p><label class='label'>Foto:</label><input type='file' name='foto' accept='image/*' class='pulsante' /></p>
				
				<input class='pulsante' type='submit' value='Aggiungi'/>
			</fieldset>
		</form>	
	</div>
	<div id='modifica'>	
		<form action='modifica_staff.cgi' method='post'>
			<fieldset class='container  form-group'>
			<legend>Modifica</legend>
				<p><select name='staff'>
					$h_opt
				</select></p>
				<input class='pulsante' type='submit' value='Modifica' />
			</fieldset>
		</form>	
	</div>
	<div id='elimina'>
		<form action='elimina_staff.cgi' method='post'>
			<fieldset class='container  form-group'>
				<legend>Elimina</legend>
				<p><select name='staff'>
					$h_opt
				</select></p>
				<input class='pulsante' type='submit' value='Elimina' />
			</fieldset>
		</form>
	</div>
	<div id='break'></div>
	</div>
	";
}
else {$htmlprint="$htmlprint<p class='error'>PRIVILEGI INSUFFICIENTI PER ACCEDERE A QUESTA PAGINA</p>";}
$htmlprint="$htmlprint $footer";
print($htmlprint);