#!"C:\strawberry\perl\bin\perl.exe"

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use CGI::Session;
use CGI;
use DBI;
use XML::LibXML::NodeList;
use XML::LibXML::XPathContext;
use File::Basename;
use utf8;


require('session.cgi');
$page=new CGI;	#creo un oggetto CGI per recuperare i parametri passati con POST
if(length $admin){
	my $parser = XML::LibXML->new();	#creo un parser per il file xml
	my %map = (							#creo una mappa per eseguire l'escape
		'>' => '<![CDATA[>]]>',
		'<' => '<![CDATA[<]]>'
	);
	
	$nome = $page->param('nome');
		$nome =~ s/([<>])/$map{$1}/g;
	$filename = $page->param('foto');
	$alt = $page->param('alt');
		$alt =~ s/([<>])/$map{$1}/g;
	$descr = $page->param('descr');
		$descr =~ s/([<>])/$map{$1}/g;
	$prezzo = $page->param('prezzo');
	$disp = $page->param('disp');
	if($disp ne "disponibile" and $disp ne "non disponibile"){
		$day=$page->param('day');
		if(!($day =~ /[1-9].{1}/) and !($day =~ /[a-zA-Z]/)){
		$disp="disponibile tra $day giorni";
		}
		else{
			$errori=1;
			$errore_numero=1;
		}
	}
	if(!$filename){
		$errori=1;
		$errore_foto=1;

	}
	if(!($prezzo =~ /[0-9]{1,4}/)){
		$errori=1;
		$errore_prezzo=1;
	}
	if($errori){
		require('insert_attrezzature.cgi');
		print redirect(-uri=>'insert_attrezzature.cgi');
	}
	else{
	
		my $file='../data/attrezzature.xml';
		my $doc = $parser->parse_file($file);
			if(!$doc){
				$ERRORE=1;
			}
		my $root = $doc->getDocumentElement;
		@items = $root->getElementsByTagName('attrezzatura');
		$newid=1;
		foreach $item(@items){ #ciclo per trovare il numero di id
			$temp=$item->findvalue('codice_prodotto');
			if($temp>$maxid){
				$newid=$temp+1;
			}
		}
		my $frammento="<attrezzatura>
			<nome>$nome</nome>
			<codice_prodotto>$newid</codice_prodotto>
			<descrizione>$descr</descrizione>
			<prezzo>$prezzo €</prezzo>
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
		if ( !$filename ){
			print $page->header ( );
			print "There was a problem uploading your photo (try a smaller file).";
			exit;
		}
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
	}
	exit;
}
