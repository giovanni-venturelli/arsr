#!"C:\strawberry\perl\bin\perl.exe"

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use CGI::Session;
use CGI;
use Time::localtime;#data e ora
use Time::Piece;

use XML::LibXML::NodeList;
use XML::LibXML::XPathContext;
use utf8;
#apri sessione
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

my $session=getSession; #richiama sessione
$page=new CGI; #crea oggetto CGI per recuperare i parametri passati con POST
if(!$session->is_empty ) #se c'è sessione
	{
		if(length $page->param('feed_body')) # recupera POST['feed_body']
			{

				my $parser = XML::LibXML->new(); #crea un nuovo parser
				my $user = $session->param('utente'); #recupera il nome utente della sessione
				my $dt = localtime->strftime('%Y-%m-%d'); #recupera la data corrente
				my $text=$page->param('feed_body'); #inserisce POST['feed_body'] nella variabile $text
				utf8::upgrade($text); #esegue l'escate con utf8
				my %map = (
				'>' => '&gt;',
				'<' => '&lt;'
				);#crea mappa per l'escape dei tag html
				$text =~ s/([<>])/$map{$1}/g; #fa l'escape html
				my $file='../data/feedback.xml'; 
		    	my $doc = $parser->parse_file($file); #apre il file per lettura nel parser
		      	#controllo se il file è aperto
		      	if(!$doc){$ERRORE=1;}
		      	#trovo il nodo radice
		    	my $root = $doc->getDocumentElement; #trova la radice
		       	@feed = $root->getElementsByTagName('feedback'); 
    			$newid=1;
    			foreach $feed(@feed){
    				$temp=$feed->findvalue('id');
    				if ($temp>$maxid){
    					$newid=$temp+1;
    				}
    			}#trova il valore da assegnare come id al nuovo nodo
				my $frammento = "<feedback>
				<id>$newid</id>
				<autore>$user</autore>
				<immagine>avatar.jpg</immagine>
				<data>$dt</data>
				<corpo>$text</corpo>
				</feedback>\n";#contenuto del nuovo nodo
				my $nodo = $parser->parse_balanced_chunk($frammento)|| die("frammento non ben formato");#controlla se il nodo è scritto correttamente in xml
				$root->appendChild($nodo)	|| die("non riesco a trovare il padre"); #inserisce all'interno della radice il nuovo nodo
				open(OUT, ">$file");#apre il file per la scrittura
				print OUT $doc->toString;#scrive nel file
				close(OUT);# chiude il file
				print redirect(-uri=>'feedback.cgi');#redirect alla pagina feedback.cgi
				exit;
			}#end if(length $page->param('feed_body'))
		else{
			print $session->header();
		}
	}#end if(!$session->is_empty )
