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
$title = 'registration';
$where = "pagina di registrazione";
$header;
$menu;
$footer;

my $htmlprint;

#print "content-type: text/html\n\n";

require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");


$htmlprint= "$header$menu<div id=\"content\">";

$htmlprint="$htmlprint

	<form method=\"post\" action=\"check_registration.cgi\">
		<div class=\"form-group\">
			<fieldset>
				<legend>Registrazione: completare i campi come richiesto</legend>
				
				<label class=\"label-block\" for=\"username\" >Username*:</label>
					<input type=\"text\" value=\"$username\" name=\"username\" id=\"username\" maxlength=\"10\" required/>
				<label class=\"label-block\" for=\"email\" >Indirizzo Email*:</label>
					<input type=\"text\" value=\"$email\" name=\"email\" id=\"email\" maxlength=\"40\" /> <br>
				<label class=\"label-block\" for=\"password\" >Password*:</label>
					<input type=\"password\" value=\"$password\" name=\"password\" id\"password\" maxlength\"8\" required/>
				<label class=\"label-block\" for=\"name\">Nome*: </label>
					<input type=\"text\" value=\"$name\" name=\"name\" id=\"nome\" maxlength=\"20\" required/>
				<label class=\"label-block\" for=\"name\">Cognome*: </label>
					<input type=\"text\" value=\"$cognome\" name=\"cognome\" id=\"cognome\" maxlength=\"20\" required/>
				<legend>indirizzo:</legend>
				<label class=\"label-block\" for=\"name\">via: </label>
					<input type=\"text\" value=\"$via\" name=\"via\" id=\"via\" maxlength=\"20\" required/>
				<label class=\"label-block\" for=\"name\">civico: </label>
					<input type=\"text\" value=\"$civico\" name=\"civico\" id=\"civico\" maxlength=\"8\" required/>
				<label class=\"label-block\" for=\"name\">provincia*: </label>
					<input type=\"text\" value=\"$provincia\" name=\"provincia\" id=\"provincia\" maxlength=\"20\" required/>
				<label class=\"label-block\" for=\"name\">Stato*: </label>
					<input type=\"text\" value=\"$paese\" name=\"paese\" id=\"paese\" maxlength=\"20\" required/>
				<label class=\"label-block\" for=\"name\">Dati e tipo di fatturazione*: </label>
					<input type=\"text\" value=\"$fatturazione\" name=\"fatturazione\" id=\"fatturazione\" maxlength=\"16\" required/>
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
				
				<input id=\"reset\" type=\"reset\" value=\"Reset\"/>
				<input id=\"Registrati\" type=\"submit\" value=\"Registrati\"/>
			</fieldset>
		</div> 
	</form>
</div>
";

if($erroreDati){
	if($erroreUser ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: <span xml:lang='en'> Username</span> </div>";
		
	}
	if($errore_mail ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: <span xml:lang='en'> email</span> </div>";
		
	}
	if($errorePwd ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: <span xml:lang='en'> Password</span> </div>";
		
	}
	if($erroreNome ){
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

$htmlprint="$htmlprint</div>\n$footer";
print $htmlprint;
