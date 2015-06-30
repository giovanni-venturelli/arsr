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
$page = new CGI;
require('session.cgi');
if(length $admin){
$parser = XML::LibXML->new();
my $htmlprint;
	require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
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
	

$htmlprint= "$header$menu<div id=\"content\">";


print $page->header;


	$htmlprint="$htmlprint<div>
	<div id='inserisci'>	
		<form action='inserisci_staff.cgi' method='post' enctype='multipart/form-data'>
			<fieldset class='form-group'>
				<legend>Inserisci Nuovo Membro Staff</legend>
				<p><label class='label-flex'>Nome:</label><input type='text' name='nome' tabindex=\"10\" /></p>
				<p><label class='label-flex'>Cognome:</label><input type='text' name='cognome' tabindex=\"11\" /></p>
				<p><label class='label-flex'>Ruolo:</label><input type='text' name='ruolo' tabindex=\"12\" /></p>
				<p><label class='label-flex'>Foto:</label><input type='file' name='foto' accept='image/*' tabindex=\"13\" /></p>
				
				<input class='pulsante' type='submit' value='Aggiungi' tabindex=\"14\"/>
			</fieldset>
		</form>	
	</div>
	<div id='modifica'>	
		<form action='modifica_staff.cgi' method='post'>
			<fieldset class='form-group'>
			<legend>Modifica Membro Staff</legend>
				<p><select name='staff' tabindex=\"15\">
					$h_opt
				</select></p>
				<input class='pulsante' type='submit' value='Modifica' tabindex=\"16\" />
			</fieldset>
		</form>	
	</div>
	<div id='elimina'>
		<form action='elimina_staff.cgi' method='post'>
			<fieldset class='form-group'>
				<legend>Elimina Membro Staff</legend>
				<p><select name='staff' tabindex=\"17\">
					$h_opt
				</select></p>
				<input class='pulsante' type='submit' value='Elimina' tabindex=\"18\"/>
			</fieldset>
		</form>
	</div>
	</div>
	</div>
	";

$htmlprint="$htmlprint $footer";
print($htmlprint);
}
else{
	print $page->redirect(-uri=>'index.cgi');
}