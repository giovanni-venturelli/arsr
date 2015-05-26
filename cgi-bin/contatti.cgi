#!"C:\strawberry\perl\bin\perl.exe"

$title = 'Contatti';
$where = "Contatti";
$header;
$menu;
$footer;
$title = 'Contatti';
$where = "Contatti";

my $htmlprint;

use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use CGI::Session;
use CGI;

use utf8;

sub getSession() {
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

my $session=getSession;
$page=new CGI;
print($page->header());

my $htmlprint;
require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
$htmlprint= "$header$menu<div id=\"content\">";
$htmlprint="$htmlprint
	<h3 class='SubTitle'>Contatti</h3>
	<p>
		<table class='TContact'>
			<tr><td class='TFirst'>Ditta:</td><td class='TSecond'>A.R.S.R.</td><td rowspan='5'><img class='image' src='../public_html/img/live.png' alt='immagine contatto'/></td></tr>
			<tr><td class='TFirst'>Di: </td><td class='TSecond'>Francesco e Amilcar</td></tr>
			<tr><td class='TFirst'>Telefono:</td><td class='TSecond'>049628818</td></tr>
			<tr><td class='TFirst'>E-Mail:</td><td class='TSecond'><a class='mailto' href='mailto:arsr.service".'@'."gmail.com'>arsr.service".'@'."gmail.com </a><img class='invisible' src='../public_html/img/mailto.png' alt='icona mail'/></td></tr>
			<tr><td class='TFirst'>Indirizzo:</td><td class='TSecond'>Via Monzambano 2, Padova (PD)</td></tr>
		</table>
	</p>
	<p>
		<table class='TContact'>
			<tr><td class='TFirst'>Nome:</td><td class='TSecond'>Francesco</td><td rowspan='4'><img class='image' src='../public_html/img/mixer.png' alt='immagine contatto'/></td></tr>
			<tr><td class='TFirst'>Cognome: </td><td class='TSecond'>Agostini</td></tr>
			<tr><td class='TFirst'>Telefono:</td><td class='TSecond'>3469468480</td></tr>
			<tr><td class='TFirst'>E-Mail:</td><td class='TSecond'><a class='mailto' href='mailto:altair80486".'@'."gmail.com'>altair80486".'@'."gmail.com </a><img class='invisible' src='../public_html/img/mailto.png' alt='icona mail'/></td></tr>
		</table>
	</p>
	<p>
		<table class='TContact'>
			<tr><td class='TFirst'>Nome:</td><td class='TSecond'>Amilcar</td><td rowspan='4'><img class='image' src='../public_html/img/nota2.png' alt='immagine contatto'/></td></tr>
			<tr><td class='TFirst'>Cognome: </td><td class='TSecond'>Rodriguez</td></tr>
			<tr><td class='TFirst'>Telefono:</td><td class='TSecond'>348228877</td></tr>
			<tr><td class='TFirst'>E-Mail:</td><td class='TSecond'><a class='mailto' href='mailto:sotorodriguez".'@'."gmail.com'>sotorodriguez".'@'."gmail.com </a><img class='invisible' src='../public_html/img/mailto.png' alt='icona mail'/></td></tr>
		</table>
	</p>
	$footer";
print($htmlprint);












