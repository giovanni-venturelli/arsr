#!"C:\strawberry\perl\bin\perl.exe"

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use CGI::Session;
use CGI;
use DBI;
use XML::LibXML::NodeList;
use XML::LibXML::XPathContext;
use utf8;
sub getSession() 
{
	$session = CGI::Session->load() or die $!;
	if ($session->is_expired || $session->is_empty ) 
		{
			return undef;
		}#end if
	else 
		{
			my $utente = $session->param('utente');
			$session;
		}#end else
}#end sub getSession()

my $session=getSession; #richiamo la sessione
$page=new CGI;	#creo un oggetto CGI per recuperare i parametri passati con POST
if($session || !$session){ # se la sessione è aperta (ATTUALMENTE SE NON ESISTE SOLO PER PROVA)
	
	my $parser = XML::LibXML->new();	#creo un parser per il file xml
	
		my $file='../data/attrezzature.xml';
		my $doc = $parser->parse_file($file);
			if(!$doc){
				$ERRORE=1;
			}
		my $root = $doc->getDocumentElement;
		@items = $root->getElementsByTagName('attrezzatura');
		
		my $code = $page->param('codice'); #salvo il codice prodotto dal file di modifica (passato come input type="hidden")
			my $Xpath = "/database/attrezzatura[codice_prodotto=\"$code\"]"; # genialata di Giovanni di salvare la stringa xpath in variabile
			for my $dead ($doc ->findnodes ($Xpath)){ # trovato su stackoverflow per eliminare il nodo
				$dead->unbindNode; # elimino il nodo 
				open(OUT, ">$file"); # tre istruzioni per salvare lo stato del file xml
				print OUT $doc->toString;
				close(OUT);
			}
	
		open(OUT, ">$file");
		print OUT $doc->toString;
		close(OUT);
		print redirect(-uri=>'attrezzature.cgi');
		exit;
}

