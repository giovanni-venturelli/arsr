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
use File::Basename;

require 'session.cgi';
$page=new CGI;	#creo un oggetto CGI per recuperare i parametri passati con POST


if(length $admin){ 	
	my $parser = XML::LibXML->new();	#creo un parser per il file xml
	my %map = (							#creo una mappa per eseguire l'escape
	'>' => '&gt;',
	'<' => '&lt;'
	);
	
	my $nome = $page->param('nome');
		$nome =~ s/([<>])/$map{$1}/g;
	my $filename = $page->param('foto');
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
				<source>$filename</source>
				<alt>$alt</alt>
			</img>
			<disponibile>$disp</disponibile>
		</attrezzatura>\n";
		my $nodo = $parser->parse_balanced_chunk($frammento) || die("frammento non ben formato");
		$root->appendChild($nodo) || die("non riesco a trovare il padre");
		open(OUT, ">$file");
		print OUT $doc->toString;
		close(OUT);
		#upload del file immagine
		$CGI::POST_MAX = 1024 * 5000;
		my $safe_filename_characters = "a-zA-Z0-9_.-";
		my $upload_dir = "../public_html/img/attrezzature";
		my ( $name, $path, $extension ) = fileparse ( $filename, '..*' );
		$filename = $name . $extension;
		$filename =~ tr/ /_/;
		$filename =~ s/[^$safe_filename_characters]//g;
		if ( $filename =~ /^([$safe_filename_characters]+)$/ ){$filename = $1;}
		else{die "Filename contains invalid characters";}
		my $upload_filehandle = $page->upload("foto");
		open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";
		binmode UPLOADFILE;
		while ( <$upload_filehandle> ){print UPLOADFILE;}
		close UPLOADFILE;
		#print $page->header ( );
		print redirect(-uri=>'attrezzature.cgi');
		exit;
}

