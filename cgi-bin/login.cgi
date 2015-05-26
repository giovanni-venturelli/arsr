#!"C:\strawberry\perl\bin\perl.exe
use XML::LibXML;

use CGI;
use CGI::Cookie qw();
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use utf8;

$page = CGI->new;
$titolo="Login";
$where="Pannello di login";
$header;
$footer;


if($page->param('login') eq "Entra"){
	$username = $page->param('User');
	$password = $page->param('Pass');

	#Controllo cosa contiene login
	if($username!~/^([a-zA-Z0-9])/){
		$erroreb=1;
	}
	if($password!~/^([a-zA-Z0-9])/){
		$erroreb=1;
	}

	if(!$erroreb){
		
		my $parser = XML::LibXML->new();
		my $doc = $parser->parse_file('../data/log_utenti.xml');
		my $root = $doc->getDocumentElement;
		my @users = $root->getElementsByTagName('utente');
		
		foreach $nod (@users) {
			$user=$nod->getElementsByTagName('username');
			if("$user" eq "$username"){
				$pass=$nod->getElementsByTagName('password');
				if("$pass" eq "$password"){
                    $cookie = $page->cookie(
                    -name=>'utente',
                    -value=>'utente');
                 	print redirect(-cookie=>$cookie, -url=>"attrezzature.cgi");	###########
				}
			}
		}
	}
	$erroreb=1;
}



#html e form
my $htmlprimt;

	print "Content-type: text/html\n\n";
		require("header.cgi");
        require("menu.cgi");
		require ("footer.cgi");

		$htmlprint= "$header$menu<div id=\"content\">";
	 
	 
	if($erroreb){    #Segnalo errore se presente nei dati di accesso
		$htmlprint="$htmlprint<div id=\"errore_login\">ERRORE LOGIN: <span xml:lang='en'> Username/Password</span> errate</div>";
		
	}

	$htmlprint="$htmlprint 
		<form method=\"post\" action=\"login.cgi\">
			<div class=\"content_form\">
				<fieldset>
					<legend>Inserire i dati di <span xml:lang=\"eng\">login</span></legend>
						<label title=\"utente\">Utente
							<div class=\"inp_utente\">
								<input title=\"utente\" type=\"text\" name=\"User\" tabindex=\"1\"/>
							<\div>
						</label>
							
						<label title=\"password\"><span xml:lang=\"en\">Password</span>
							<div class=\"inp_pass\">	
								<input title=\"password\" type=\"password\" name=\"Pass\" tabindex=\"2\"/>
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

