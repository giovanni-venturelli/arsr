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

sub getSession(){
	$session = CGI::Session->load() or die $!;
	if($session->is_expired || $session->is_empty){
		return undef;
	}
else{
	my $utente = $session->param('utente');
	my $admin = $session->param('admin');
	return $utente;
}
}


my $utente = getSession(); #richiama sessione
$page=new CGI; #crea oggetto CGI per recuperare i parametri passati con POST

if(!length $utente) #se non c'è sessione
	{

		if(length $page->param('login')){
		my $nome=$page->param('user'); # recupera POST['user'];
		my $pass=$page->param('pass'); # recupera POST['password'];
		my $parser = XML::LibXML->new();
		my $doc = $parser->parse_file('../data/login.xml');
		my $root = $doc->getDocumentElement;
		my @users = $root->getElementsByTagName('utente');

		foreach $nod (@users) {
			$user=($nod->getElementsByTagName('username'))->string_value;
			if("$nome" eq "$user"){
				$password=($nod->getElementsByTagName('password'))->string_value;
				if("$pass" eq "$password"){
					$session = new CGI::Session();
					$admin=($nod->getElementsByTagName('admin'))->string_value;
					if($admin eq "si"){
						$session->param('admin', $nome);
					}
					else{
						$session->param('utente', $nome);
					}
					print $session->header(-location => "index.cgi");
					exit;
				}
			}
		}
		$erroreb=1;
			require ("login.cgi");
	}
}
else{
	print $page->header;
	print $page->redirect(-uri=> 'index.cgi');
}
