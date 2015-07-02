#!/usr/bin/perl -w

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use CGI::Session;
use CGI;
use Time::localtime;#../data e ora
use Time::Piece;

#use XML::LibXML::NodeList;
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
		my $parser = XML::LibXML->new(); #crea un nuovo parser
		my $user = $session->param('utente'); #recupera il nome utente della sessione
		my $id=$page->param('id');
		my $file='../data/feedback.xml'; 
    	my $doc = $parser->parse_file($file); #apre il file per lettura nel parser
      	#controllo se il file è aperto
      	if(!$doc){$ERRORE=1;}
      	#trovo il nodo radice
    	my $root = $doc->getDocumentElement; #trova la radice
    	@feed = $root->getElementsByTagName('feedback'); 
       	my $Xpath = "/commenti/feedback[id=\"$id\"]"; #imposto il percorso per trovare il nodo da eliminare
       	print $id;
		for my $dead ($doc ->findnodes ($Xpath)){ #trovo il nodo da eliminare
			$dead->unbindNode; # elimino il nodo 
			open(OUT, ">$file"); # tre istruzioni per salvare lo stato del file xml
			print OUT $doc->toString;
			close(OUT);
		}	
		print redirect(-uri=>'feedback.cgi');#redirect alla pagina feedback.cgi
		exit;
}#end if(!$session->is_empty )
