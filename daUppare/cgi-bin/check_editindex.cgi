#!/usr/bin/perl -w

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use CGI::Session;
use CGI;
use DBI;
#use XML::LibXML::NodeList;
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
	
	my $titolouno = $page->param('titolo_uno');
	$titolouno =~ s/([<>])/$map{$1}/g;
	utf8::encode($titolouno);
	my $corpouno = $page->param('corpo_uno');
	utf8::encode($corpouno);
	my $titolodue = $page->param('titolo_due');
	$titolodue =~ s/([<>])/$map{$1}/g;
	utf8::encode($titolodue);
	my $corpodue = $page->param('corpo_due');
	utf8::encode($corpodue);
	my $titolotre = $page->param('titolo_tre');
	$titolotre =~ s/([<>])/$map{$1}/g;
	utf8::encode($titolotre);
	my $corpotre = $page->param('corpo_tre');
	utf8::encode($corpotre);
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
			<id>uno</id>
			<titolo>$titolouno</titolo>
			<corpo>$corpouno</corpo>
			</frame>
			<frame>
			<id>due</id>
			<titolo>$titolodue</titolo>
			<corpo>$corpodue</corpo>
			</frame>
			<frame >
			<id>tre</id>
			<titolo>$titolotre</titolo>
			<corpo>$corpotre</corpo>
			</frame>\n";
			my $nodo = $parser->parse_balanced_chunk($frammento) || die("frammento non ben formato");
			$root->appendChild($nodo) || die("non riesco a trovare il padre");
			open(OUT, ">$file");
			print OUT $doc->toString;
			close(OUT);
		}
		print redirect(-uri=>'index.cgi');
		exit;


