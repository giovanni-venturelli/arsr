#!/usr/bin/perl -w
use XML::LibXML;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser);
use utf8;


sub destroySession(){
	$session = CGI::Session->load() or die $!;
	my $user = $session->param('utente');
	$session->close();
	$session->delete();
	$session->flush();

}

my $page=CGI->new;
destroySession();
print $page->redirect(-uri=>'index.cgi');
