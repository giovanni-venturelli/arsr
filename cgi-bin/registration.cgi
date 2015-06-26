#!"C:\strawberry\perl\bin\perl.exe"

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Cookie qw();
use CGI::Session;
use CGI;
use DBI;
use utf8;
$page = new CGI;
$session = new CGI::Session();
print $session->header();

my $parser = XML::LibXML->new();
$title = 'Registrazione';
$where = "Pennello di registrazione";
$header;
$menu;
$footer;

my $htmlprint;

#print "content-type: text/html\n\n";
require ("session.cgi");
require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");


$htmlprint= "$header$menu<div id=\"content\">";

if($erroreDati){
	if($erroreUser ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: <span xml:lang='en'> Username</span> </div>";
		
	}
	if($errorePwd ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: <span xml:lang='en'> Password</span> </div>";
		
	}
	if($firstname ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: Nome </div>";
		
	}
	if($erroreCognome ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: cognome</div>";
		
	}
	if($erroreVia ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: via</div>";
		
	}
	if($erroreCivico ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: civico</div>";
		
	}
	if($erroreProvincia ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: provincia</div>";
		
	}
	if($errorePaese ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: Stato</div>";
		
	}
	if($ErroreFatt ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: fatturazione </div>";
		
	}
}

$htmlprint="$htmlprint

	<form class=\"pure-form pure-form-aligned\" method=\"post\" action=\"check_registration.cgi\" id=\"registration_form\" onsubmit=\"return validateForm(this)\">
		<div class=\"pure-control-group\">
			<fieldset>
				<legend>Registrazione: completare i campi come richiesto</legend>
				
					<label class=\"label_block\" for=\"username\" >Username</label>
						<input type=\"text\" value=\"$username\"  name=\"username\" id=\"username\" maxlength=\"10\" onkeyup=\"checkNotEmpty('username')\"/>
					<label class=\"label_block\" for=\"email\" >Indirizzo email</label>
						<input type=\"email\" value=\"$email\"  name=\"email\" id=\"email\" maxlength=\"80\" onkeyup=\"checkEmail()\"/>
					<label class=\"label_block\" for=\"password\" >Password</label>
						<input type=\"password\" value=\"$password\"  name=\"password\" id=\"password\" maxlength=\"8\" onkeyup=\"checkNotEmpty('password')\"/>
					<label class=\"label_block\" for=\"nome\">Nome</label>
						<input type=\"text\" value=\"$firstname\"  name=\"firstname\" id=\"nome\" maxlength=\"20\" ronkeyup=\"checkNotEmpty('nome')\"/>
					<label class=\"label_block\" for=\"cognome\">Cognome</label>
						<input type=\"text\" value=\"$cognome\"  name=\"cognome\" id=\"cognome\" maxlength=\"20\" onkeyup=\"checkNotEmpty('cognome')\"/>
					
					<label class=\"label_block\" for=\"via\">Indirizzo</label>
						<input type=\"text\" value=\"$via\"  name=\"via\" id=\"via\" maxlength=\"20\" onkeyup=\"checkNotEmpty('via')\"/>
					<label class=\"label_block\" for=\"civico\"> Numero civico</label>
						<input type=\"text\" value=\"$civico\"  name=\"civico\" id=\"civico\" maxlength=\"8\" onkeyup=\"checkNotEmpty('civico')\"/>
					<label class=\"label_block\" for=\"provincia\">Provincia </label>
						<input type=\"text\" value=\"$provincia\"  name=\"provincia\" id=\"provincia\" maxlength=\"20\" onkeyup=\"checkNotEmpty('provincia')\"/>
					<label class=\"label_block\" for=\"paese\">Stato</label>
						<input type=\"text\" value=\"$paese\"  name=\"paese\" id=\"paese\" maxlength=\"20\" onkeyup=\"checkNotEmpty('paese')\"/>
					<label class=\"label_block\" for=\"fatturazione\">Dati e tipo di fatturazione</label>
						<input type=\"text\" value=\"$fatturazione\"  name=\"fatturazione\" id=\"fatturazione\" maxlength=\"16\"  onkeyup=\"checkNotEmpty('fatturazione')\"/>
				
					<input type=\"radio\" name=\"tipo_fatt\" ";
						if($tipo_fatt=="p.iva"){
							$htmlprint="$htmlprint checked ";
						}
						$htmlprint="$htmlprint> Partita Iva
					
					<input type=\"radio\" name=\"tipo_fatt\" value=\"cod.fiscale\" ";
						if($tipo_fatt=="cod.fiscale"){
							$htmlprint="$htmlprint checked ";
						}
						$htmlprint="$htmlprint> Codice Fiscale
				<div>
					<input class=\"pulsante\" type=\"submit\" value=\"Registrati\"/>
					<input class=\"pulsante\" type=\"reset\" value=\"Reset\"/>
				</div>
			</fieldset>
			</div>
	</form>

			

	

";


$htmlprint="$htmlprint</div>\n$footer";
print $htmlprint;
