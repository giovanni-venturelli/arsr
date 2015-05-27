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
		my $doc = $parser->parse_file('../data/log_admin.xml');
		my $root = $doc->getDocumentElement;
		my @users = $root->getElementsByTagName('admin');
		
		foreach $nod (@users) {
			$dbuser=$nod->getElementsByTagName('username');
			if("$dbuser" eq "$username"){
				$dbpass=$nod->getElementsByTagName('password');
				if("$dbpass" eq "$password"){
                    sub createSession(){
						$session= new CGI::Session();
						$session->param('utente',$user);
						print $session->header(-url =>"attrezzature.cgi");
					}
					#$cookie = $page->cookie(
                    #-name=>'utente',
                    #-value=>'utente');
                 	#print redirect(-cookie=>$cookie, -url=>"admin_menu.cgi");	###########
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
							<br>
						<label title=\"password\"><span xml:lang=\"en\">Password</span>
							<div class=\"inp_pass\">	
								<input title=\"password\" type=\"password\" name=\"Pass\" tabindex=\"2\"/>
							<\div>
						</label>
					
				<br>
				<input id=\"reset\" name=\"annulla\"  value=\"Reset\" type=\"reset\" tabindex=\"3\"/>
				<input id=\"submit\" name=\"login\"  value=\"Entra\" type=\"submit\" tabindex=\"4\"/>
				</fieldset>  
			</form>
		</div>
		";
	
	
	$htmlprint="$htmlprint</div>\n$footer";
        print $htmlprint;

