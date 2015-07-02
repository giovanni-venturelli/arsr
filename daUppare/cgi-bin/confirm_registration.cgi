#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser);
use utf8;

	require 'session.cgi';

	$title="Conferma Regitrazione";
	$where="confirm_registration";

	$parser = XML::LibXML->new();
	
	my $file = "../data/staff.xml";
	my $doc = $parser->parse_file($file);
		if(!$doc){
			$ERRORE=1;
		}

	my $root = $doc->getDocumentElement;
	@items = $root->getElementsByTagName('persona');
	$num_attr=@items;
$page = new CGI;
print $page->header;
require ("session.cgi");
	require("header.cgi");
	require("menu.cgi");
	require("footer.cgi");

	$htmlprint="$header $menu <div id=\"content\">
	<div id=\"registration_confirm\">
	<p>Registrazione avvenuta correttamente!</p>
	<a href=\"index.cgi\" class=\"link_body pulsante\">Torna alla <span lang=\"en\">Home</span></a>
	</div>
	</div>";
		
	$htmlprint="$htmlprint$footer";
	print $htmlprint;
	
	
