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

require ("session.cgi");
$page = new CGI; #creo un oggetto CGI per recuperare i parametri passati con POST

if(length $utente + length $admin && $page->param('modifica')){
	
	my $parser = XML::LibXML->new();	#creo un parser per il file xml
	my %map = (							#creo una mappa per eseguire l'escape
	'>' => '&gt;',
	'<' => '&lt;'
	);
	
	my $titololive = $page->param('titolo_live');
		$titololive =~ s/([<>])/$map{$1}/g;
		utf8::encode($titololive);
	my $corpolive = $page->param('corpo_live');
	utf8::encode($corpolive);
	my $titolodj = $page->param('titolo_djset');
		$titolodj =~ s/([<>])/$map{$1}/g;
		utf8::encode($titolodj);
	my $corpodj = $page->param('corpo_djset');
	utf8::encode($corpodj);
	my $titolostudio = $page->param('titolo_studio');
		$titolostudio =~ s/([<>])/$map{$1}/g;
		utf8::encode($titolostudio);
	my $corpostudio = $page->param('corpo_studio');
	utf8::encode($corpostudio);
		my $file='../data/index.xml';
		my $doc = $parser->parse_file($file);
			if(!$doc){
				$ERRORE=1;
			}
		my $root = $doc->getDocumentElement;
		@items = $root->getElementsByTagName('frame');
		my $Xpath = "/main/frame"; # salva la stringa xpath in una variabile
			for my $dead ($doc ->findnodes ($Xpath)){ 
				$dead->unbindNode; # elimino il nodo 
				open(OUT, ">$file"); # tre istruzioni per salvare lo stato del file xml
				print OUT $doc->toString;
				close(OUT);
			}
	

		my $frammento="	<frame >
		<id>live</id>
		<titolo>$titololive</titolo>
		<corpo>$corpolive</corpo>
	</frame>
	<frame>
		<id>djset</id>
		<titolo>$titolodj</titolo>
		<corpo>$corpodj</corpo>
	</frame>
	<frame >
		<id>studio</id>
		<titolo>$titolostudio</titolo>
		<corpo>$corpostudio</corpo>
	</frame>\n";
		my $nodo = $parser->parse_balanced_chunk($frammento) || die("frammento non ben formato");
		$root->appendChild($nodo) || die("non riesco a trovare il padre");
		open(OUT, ">$file");
		print OUT $doc->toString;
		close(OUT);
	}
		print redirect(-uri=>'index.cgi');
		exit;


