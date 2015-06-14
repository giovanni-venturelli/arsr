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

require 'session.cgi';
$page=new CGI;	#creo un oggetto CGI per recuperare i parametri passati con POST



  my $random_number = rand();
my $file = "temp$random_number.txt";

# Use the open() function to create the file.
unless(open FILE, '>'.$file) {
  # Die with error message 
  # if we can't open it.
 die "nUnable to create $filen";
}

# Write some text to the file.

print FILE "Hello theren";
print FILE "How are you?n";

# close the file.
close FILE;



if(length $admin){ 	
	my $parser = XML::LibXML->new();	#creo un parser per il file xml
	my %map = (							#creo una mappa per eseguire l'escape
	'>' => '&gt;',
	'<' => '&lt;'
	);
	
	my $nome = $page->param('nome');
		$nome =~ s/([<>])/$map{$1}/g;
	my $img = $page->param('img');
	my $alt = $page->param('alt');
		$alt =~ s/([<>])/$map{$1}/g;
	my $descr = $page->param('descr');
		$descr =~ s/([<>])/$map{$1}/g;
	my $prezzo = $page->param('prezzo');
	my $disp = $page->param('disp');
	if($disp ne "disponibile" and $disp ne "non disponibile"){
		$day=$page->param('day');
		$disp="disponibile tra $day giorni";
	}
		my $file='../data/attrezzature.xml';
		my $doc = $parser->parse_file($file);
			if(!$doc){
				$ERRORE=1;
			}
		my $root = $doc->getDocumentElement;
		@items = $root->getElementsByTagName('attrezzatura');
		
		my $code = $page->param('codice'); #salvo il codice prodotto dal file di modifica (passato come input type="hidden")
			my $Xpath = "/database/attrezzatura[codice_prodotto=\"$code\"]"; # salva la stringa xpath in variabile
			for my $dead ($doc ->findnodes ($Xpath)){ # elimina il nodo
				$dead->unbindNode; # elimino il nodo 
				open(OUT, ">$file"); # tre istruzioni per salvare lo stato del file xml
				print OUT $doc->toString;
				close(OUT);
			}
	

		my $frammento="<attrezzatura>
			<nome>$nome</nome>
			<codice_prodotto>$code</codice_prodotto>
			<descrizione>$descr</descrizione>
			<prezzo>$prezzo€</prezzo>
			<img>
				<source>$img</source>
				<alt>$alt</alt>
			</img>
			<disponibile>$disp</disponibile>
		</attrezzatura>\n";
		my $nodo = $parser->parse_balanced_chunk($frammento) || die("frammento non ben formato");
		$root->appendChild($nodo) || die("non riesco a trovare il padre");
		open(OUT, ">$file");
		print OUT $doc->toString;
		close(OUT);
		print redirect(-uri=>'attrezzature.cgi');
		exit;
}

