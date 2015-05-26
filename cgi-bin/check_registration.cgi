#!"C:\strawberry\perl\bin\perl.exe"

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use CGI::Session;
use CGI;
use XML::LibXML::NodeList;
use XML::LibXML::XPathContext;
use utf8;

#apri sessione se non ci sono erorri e manda utente in home page con sessione aperta

	
		
		
	my $session=getSession;
	$page=new CGI;

		
			my $parser = XML::LibXML->new();	#creo un parser per il file xml
			my %map = (							#creo una mappa per eseguire l'escape
				'>' => '<![CDATA[>]]>',
				'<' => '<![CDATA[<]]>'
			);

			
			#creo tutte le variabili che poi vado a mettere nell'xml
			$erroreDati=0;
			$erroreUser=0;
			$errorePwd=0;
			$erroreNome=0;
			$erroreCognome=0;
			$erroreVia=0;
			$erroreCivico=0;
			$errorePaese=0;
			$erroreProvincia=0;
			$ErroreFatt=0;
			
			$username=$page->param('username'); 
				$username =~ s/([<>])/$map{$1}/g;
				if($username !~ /[a-zA-Z0-9]+/ ){
					$erroreDati=1;
					$erroreUser=1;
				}
				$email=$page->param('email'); 
				$email =~ s/([<>])/$map{$1}/g;
				
			 $password=$page->param('password'); 
				$password =~ s/([<>])/$map{$1}/g;
				if( $password !~/[ \w ]+/ ){
					$erroreDati=1;
					$errorePwd=1;
				}
			 $firstname=$page->param('firstname'); 
				$name =~ s/([<>])/$map{$1}/g;
				if($firstname !~/[a-zA-Z]+/ ){
					$erroreDati=1;
					$firstname=1;
				}
			 $cognome=$page->param('cognome');
				$cognome =~ s/([<>])/$map{$1}/g;
				if($cognome !~ /[a-zA-Z]+/ ){
					$erroreDati=1;
					$erroreCognome=1;
				}
			 $via=$page->param('via'); 
				$via =~ s/([<>])/$map{$1}/g;
				if($via !~/([a-zA-Z0-9]+\s*[a-zA-Z0-9]+)+/){
					$erroreDati=1;
					$erroreVia=1;
				}
			 $civico=$page->param('civico'); 
				$civico =~ s/([<>])/$map{$1}/g;
				if($civico !~ m/[0-9]+[a-m]?/){
					$erroreDati=1;
					$erroreCivico=1;
				}
			 $provincia=$page->param('provincia'); 
				$provincia =~ s/([<>])/$map{$1}/g;
				if($provincia !~/[a-zA-Z]+/){
					$erroreDati=1;
					$erroreProvincia=1
				}
			 $paese=$page->param('paese'); 
				$paese =~ s/([<>])/$map{$1}/g;
				if($paese !~/[a-zA-Z]+/){
					$erroreDati=1;
					$errorePaese=1;
				}
			 $fatturazione=$page->param('fatturazione'); 
				$fatturazione =~ s/([<>])/$map{$1}/g;
				if($fatturazione !~ /[a-zA-Z0-9]+/){
					$erroreDati=1;
					$ErroreFatt=1;
				}
			 $tipo_fatt=$page->param('tipo_fatt');
				$tipo_fatt =~ s/([<>])/$map{$1}/g;
				
			
			if($erroreDati){
				require('registration.cgi');
			}
			else{
			
				my $file='../data/log_utenti.xml'; 
				my $doc = $parser->parse_file($file); #apre il file per lettura nel parser
				
				#controllo se il file è aperto
				if(!$doc){
						$ERRORE=1;
					}
					#trovo il nodo radice
				my $root = $doc->getDocumentElement; #trova la radice
				@feed = $root->getElementsByTagName('utente');
			
				if(!$erroreDati){ # se non ci sono errori nei dati inserisco l'utente
					my $frammento = "
						<utente>
							<username>$username</username>
							<email>$email</email>
							<password>$password</password>
							<nome>$firstname</nome>
							<cognome>$cognome</cognome>
							<indirizzo>
								<via>$via</via>
								<civico>$civico</civico>
								<provincia>$provincia</provincia>
								<paese>$paese</paese>
							</indirizzo>
							<fatturazione>$fatturazione</fatturazione>
							<tipo_fatt>$tipo_fatt</tipo_fatt>
						</utente>
						\n";
							
					my $nodo = $parser->parse_balanced_chunk($frammento);				
						
					$root->appendChild($nodo);
						
					open(OUT, ">$file");#apre il file per la scrittura
					print OUT $doc->toString;#scrive nel file
					close(OUT);# chiude il file
					print redirect(-uri=>'login.cgi');
				}
			}
exit
;
	
