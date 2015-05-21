#!"C:\strawberry\perl\bin\perl.exe"

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use utf8;

my $parser = XML::LibXML->new();
$title = 'Inserisci Attrezzatura';
$where = "<span lang=\"en\">Home</span>";
$header;
$menu;
$footer;
my $htmlprint;


print "content-type: text/html\n\n";

		require ("header.cgi");
		require ("admin_menu.cgi");
        require ("footer.cgi");
        $htmlprint= "$header$menu<div id=\"content\">";
		my $fileattr='../data/attrezzature.xml';
    	my $doc = $parser->parse_file($fileattr);
      	#controllo se il file è aperto
      	if(!$doc){$ERRORE=1;}
      	#trovo il nodo radice
    	my $root = $doc->getDocumentElement;
    	@attr = $root->getElementsByTagName('attrezzatura');
    	$id=0;
    	foreach $nod (@attr){
    		my $src=$nod->find('img/source');
    		my $alt=$nod->find('img/alt');
    		$htmlprint="$htmlprint<div class=\"attrezzatura\">\n";
    		$immagine="\n<div>\n<img class=\"attr_img\" id=\"attr_img$id\" src=\"$src\" alt=\"$alt\"/></div>\n";
            my $nome=$nod->find('nome');
            my $codice= $nod->find('codice_prodotto');
            my $descrizione=$nod->find('descrizione');
            my $prezzo=$nod->find('prezzo');
            $htmlprint= "$htmlprint$immagine\n
            <div>\n
            <h3>$nome</h3>\n
            <p>Codice: $codice</p>\n
            <p>Descrizione: $descrizione</p>\n
            <p>Prezzo: $prezzo</p>\n
            </div>\n
            </div>\n";
    		$id++;
    	}
		$htmlprint="$htmlprint</div>\n$footer";
        print $htmlprint;
