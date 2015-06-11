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

	<form class=\"pure-form pure-form-aligned\" method=\"post\" action=\"check_registration.cgi\">
		<div class=\"pure-control-group\">
			<fieldset>
				<legend>Registrazione: completare i campi come richiesto</legend>
				
					<label class=\"label_block\" for=\"username\" >Username</label>
						<input type=\"text\" value=\"$username\" placeholder=\"Username \" name=\"username\" id=\"username\" maxlength=\"10\" required/>
					<label class=\"label_block\" for=\"email\" >Indirizzo email</label>
						<input type=\"email\" value=\"$email\" placeholder=\"Email \" name=\"email\" id=\"email\" maxlength=\"80\" />
					<label class=\"label_block\" for=\"password\" >Password</label>
						<input type=\"password\" value=\"$password\" placeholder=\"Passoword\" name=\"password\" id\"password\" maxlength\"8\" required/>
					<label class=\"label_block\" for=\"name\">Nome</label>
						<input type=\"text\" value=\"$firstname\" placeholder=\" Nome\" name=\"firstname\" id=\"nome\" maxlength=\"20\" required/>
					<label class=\"label_block\" for=\"name\">Cognome</label>
						<input type=\"text\" value=\"$cognome\" placeholder=\"Cognome \" name=\"cognome\" id=\"cognome\" maxlength=\"20\" required/>
					
					<label class=\"label_block\" for=\"name\">Indirizzo</label>
						<input type=\"text\" value=\"$via\" placeholder=\"via,piazza,vicolo,corso \" name=\"via\" id=\"via\" maxlength=\"20\" required/>
					<label class=\"label_block\" for=\"name\"> Numero civico</label>
						<input type=\"text\" value=\"$civico\" placeholder=\"Nmero civico \" name=\"civico\" id=\"civico\" maxlength=\"8\" required/>
					<label class=\"label_block\" for=\"name\">Provincia </label>
						<input type=\"text\" value=\"$provincia\" placeholder=\" Provincia \" name=\"provincia\" id=\"provincia\" maxlength=\"20\" required/>
					<label class=\"label_block\" for=\"name\">Stato</label>
						<input type=\"text\" value=\"$paese\" placeholder=\" Stato\" name=\"paese\" id=\"paese\" maxlength=\"20\" required/>
					<label class=\"label_block\" for=\"name\">Dati e tipo di fatturazione</label>
						<input type=\"text\" value=\"$fatturazione\" placeholder=\"P.iva o Codice Fiscale \" name=\"fatturazione\" id=\"fatturazione\" maxlength=\"16\" minlength=\"11\" required/></label>
				
						<input type=\"radio\" name=\"tipo_fatt\" ";
						if($tipo_fatt=="p.iva"){
							$htmlprint="$htmlprint checked";
						}
						$htmlprint="$htmlprint> Partita Iva
						<input type=\"radio\" name=\"tipo_fatt\" value=\"cod.fiscale\" ";
						if($tipo_fatt=="cod.fiscale"){
							$htmlprint="$htmlprint checked";
						}
						$htmlprint="$htmlprint> Codice Fiscale
				<div><input class=\"pulsante\" type=\"reset\" value=\"Reset\"/>
				<input class=\"pulsante\" type=\"submit\" value=\"Registrati\"/>
				</div>
			</fieldset>
			</div>
	</form>

			

	

";


$htmlprint="$htmlprint</div>\n$footer";
print $htmlprint;
