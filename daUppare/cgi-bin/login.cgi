#!/usr/bin/perl -w
use XML::LibXML;

use CGI;
use CGI::Session;
use CGI::Cookie qw();
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use utf8;

$page = CGI->new;
print $page->header;

$title="Login";
$where="Pannello di login";
require ("session.cgi");
require("header.cgi");

my $htmlprimt;

        require("menu.cgi");
		require ("footer.cgi");

		$htmlprint= "$header$menu<div id=\"content\">";
	 
	 
	if($erroreb){    #Segnalo errore se presente nei dati di accesso
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE <span xml:lang='en'> LOGIN: Username/Password</span> errate</div>";	
	}
	
	$htmlprint="$htmlprint 
		<form method=\"post\" action=\"check_login.cgi\">
			<div class=\"content_form\">
				<fieldset>
					<legend>Inserire i dati di <span xml:lang=\"eng\">login</span></legend>
						<label title=\"utente\" class=\"inp_utente\" for=\"username\"><span xml:lang=\"en\">Username</span> </label>
								<input title=\"utente\" type=\"text\" name=\"user\" tabindex=\"10\" id=\"username\"/>

						<label title=\"password\" class=\"inp_pass\" for=\"password\"><span xml:lang=\"en\">Password</span></label>
						<input title=\"password\" type=\"password\" name=\"pass\" tabindex=\"11\" id=\"password\"/>

				<input class=\"pulsante\" name=\"login\"  value=\"Entra\" type=\"submit\" tabindex=\"12\"/>
				<input class=\"pulsante\" name=\"annulla\"  value=\"Reset\" type=\"reset\" tabindex=\"13\"/>
				</fieldset>  
			</div>
		</form>
		
			<div class=\"registrati_ora\">
				Non sei ancora registrato? fallo ora <a href=\"registration.cgi\" tabindex=\"14\"> Cliccando QUI</a>
			</div>
		";
	
	$htmlprint="$htmlprint</div>\n$footer";
        print $htmlprint;