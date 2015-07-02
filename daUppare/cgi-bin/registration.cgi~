#!/usr/bin/perl -w

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Cookie qw();
use CGI::Session;
use CGI;
use DBI;
use utf8;
$page = new CGI;
$session = new CGI::Session();


my $parser = XML::LibXML->new();
$title = 'Registrazione';
$where = "Pennello di registrazione";
$header;
$menu;
$footer;

my $htmlprint;

#print "content-type: text/html\n\n";
require ("session.cgi");
if(!$utente&&!$admin){
	print $session->header();
require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");


$htmlprint= "$header$menu<div id=\"content\">";

if($erroreDati){
	if($erroreUser==1){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: <span xml:lang='en'> Username</span> </div>";
		
	}
	elsif($erroreUser==2 ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. Username già in uso. </div>";
		
	}
	if($errorePwd ){
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE Dati inseriti. verificare: <span xml:lang='en'> Password</span> </div>";
		
	}
	if($erroreFirstname ){
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
						<input class=\"registration_input\" type=\"text\" value=\"$username\" tabindex=\"10\"  name=\"username\" id=\"username\" maxlength=\"10\" onkeyup=\"checkNotEmpty(this)\"/><div class=\"registration_message\" id=\"username_check\">campo non valido</div>
					<label class=\"label_block\" for=\"email\" >Indirizzo email</label>
						<input class=\"registration_input\" type=\"email\" value=\"$email\" tabindex=\"11\"  name=\"email\" id=\"email\" maxlength=\"80\" onkeyup=\"checkEmail(this)\"/><div class=\"registration_message\" id=\"email_check\">campo non valido</div>
					<label class=\"label_block\" for=\"password\" >Password</label>
						<input class=\"registration_input\" type=\"password\" value=\"$password\" tabindex=\"12\" name=\"password\" id=\"password\" maxlength=\"8\" onkeyup=\"checkNotEmpty(this)\"/><div class=\"registration_message\" id=\"password_check\">campo non valido</div>
					<label class=\"label_block\" for=\"nome\">Nome</label>
						<input class=\"registration_input\" type=\"text\" value=\"$firstname\" tabindex=\"13\"  name=\"firstname\" id=\"nome\" maxlength=\"20\" onkeyup=\"checkNotEmpty(this)\"/><div class=\"registration_message\" id=\"nome_check\">campo non valido</div>
					<label class=\"label_block\" for=\"cognome\">Cognome</label>
						<input class=\"registration_input\" type=\"text\" value=\"$cognome\" tabindex=\"14\"  name=\"cognome\" id=\"cognome\" maxlength=\"20\" onkeyup=\"checkNotEmpty(this)\"/><div class=\"registration_message\" id=\"cognome_check\">campo non valido</div>
					<label class=\"label_block\" for=\"via\">Indirizzo</label>
						<input class=\"registration_input\" type=\"text\" value=\"$via\" tabindex=\"15\"  name=\"via\" id=\"via\" maxlength=\"20\" onkeyup=\"checkNotEmpty(this)\"/><div class=\"registration_message\" id=\"via_check\">campo non valido</div>
					<label class=\"label_block\" for=\"civico\"> Numero civico</label>
						<input class=\"registration_input\" type=\"text\" value=\"$civico\" tabindex=\"16\"  name=\"civico\" id=\"civico\" maxlength=\"8\" onkeyup=\"checkNotEmpty(this)\"/><div class=\"registration_message\" id=\"civico_check\">campo non valido</div>
					<label class=\"label_block\" for=\"provincia\">Provincia </label>
						<input class=\"registration_input\" type=\"text\" value=\"$provincia\" tabindex=\"17\"  name=\"provincia\" id=\"provincia\" maxlength=\"20\" onkeyup=\"checkNotEmpty(this)\"/><div class=\"registration_message\" id=\"provincia_check\">campo non valido</div>
					<label class=\"label_block\" for=\"paese\">Stato</label>
						<input class=\"registration_input\" type=\"text\" value=\"$paese\" tabindex=\"18\"  name=\"paese\" id=\"paese\" maxlength=\"20\" onkeyup=\"checkNotEmpty(this)\"/><div class=\"registration_message\" id=\"paese_check\">campo non valido</div>
					<label class=\"label_block\" for=\"fatturazione\">Dati e tipo di fatturazione</label>
						<input class=\"registration_input\" type=\"text\" value=\"$fatturazione\" tabindex=\"19\"  name=\"fatturazione\" id=\"fatturazione\" maxlength=\"16\"  onkeyup=\"checkNotEmpty(this)\"/>
				
					<input type=\"radio\" name=\"tipo_fatt\" tabindex=\"20\" id=\"seleziona_partita_iva\" onchange=\"handleCognome()\"";
						if($tipo_fatt=="p.iva"){
							$htmlprint="$htmlprint checked ";
						}
						$htmlprint="$htmlprint> <label for=\"seleziona_partita_iva\">Partita Iva</label>
					
					<input type=\"radio\" name=\"tipo_fatt\" tabindex=\"21\" id=\"seleziona_codice\" value=\"cod.fiscale\" onchange=\"handleCognome()\" ";
						if($tipo_fatt=="cod.fiscale"){
							$htmlprint="$htmlprint checked ";
						}
						$htmlprint="$htmlprint> <label for=\"seleziona_codice\" >Codice Fiscale</label>
				<div class=\"registration_message\" id=\"fatturazione_check\">campo non valido</div>
				<div>
					<input class=\"pulsante\" type=\"submit\" value=\"Registrati\" tabindex=\"22\"/>
					<input class=\"pulsante\" type=\"reset\" value=\"Reset\" tabindex=\"23\" onclick=\"resetFields('registration_form')\"/>
				</div>
			</fieldset>
			</div>
	</form>";


$htmlprint="$htmlprint</div>\n$footer";
print $htmlprint;
}
else {
	print $page->redirect(-uri=>'index.cgi');
}
