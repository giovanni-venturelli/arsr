#!"C:\strawberry\perl\bin\perl.exe
use XML::LibXML;

use CGI;
use CGI::Session;
use CGI::Cookie qw();
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use utf8;

require("header.cgi");

$page = CGI->new;
$titolo="Login";
$where="Pannello di login";
$header;
$footer;

#html e form
my $htmlprimt;

	print "Content-type: text/html\n\n";
        require("menu.cgi");
		require ("footer.cgi");

		$htmlprint= "$header$menu<div id=\"content\">";
	 
	 
	if($erroreb){    #Segnalo errore se presente nei dati di accesso
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE LOGIN: <span xml:lang='en'> Username/Password</span> errate</div>";
		
	}

	$htmlprint="$htmlprint 
		<form method=\"post\" action=\"check_login.cgi\">
			<div class=\"content_form\">
				<fieldset>
					<legend>Inserire i dati di <span xml:lang=\"eng\">login</span></legend>
						<label title=\"utente\">Utente
							<div class=\"inp_utente\">
								<input title=\"utente\" type=\"text\" name=\"user\" tabindex=\"1\"/>
							<\div>
						</label>
							
						<label title=\"password\"><span xml:lang=\"en\">Password</span>
							<div class=\"inp_pass\">	
								<input title=\"password\" type=\"password\" name=\"pass\" tabindex=\"2\"/>
							<\div>
						</label>
					
				
				<input id=\"reset\" name=\"annulla\"  value=\"Reset\" type=\"reset\" tabindex=\"3\"/>
				<input id=\"submit\" name=\"login\"  value=\"Entra\" type=\"submit\" tabindex=\"4\"/>
				</fieldset>  
		</form>
				<div class=\"registrati_ora\">
					Non sei ancora registrato? fallo ora <a href=\"registration.cgi\"> Cliccando QUI</a>
				</div>
			</div>
		";
	
	
	$htmlprint="$htmlprint</div>\n$footer";
        print $htmlprint;

