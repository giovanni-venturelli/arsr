#!/usr/bin/perl -w

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
$session = CGI::Session->load() or die $!;
my $admin = $session->param('admin');

my $session=getSession;
$page=new CGI;
print($page->header());

my $htmlprint;
require("session.cgi");
require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
$htmlprint= "$header$menu<div id=\"content\">";
$htmlprint="$htmlprint
		<div class='TContact'>
			<div class='contact_../data'>
				<div class='pair'>
					<div class='TFirst'>Ditta:</div>
					<div class='TSecond'>A.R.S.R.</div>
				</div>
				<div class='pair'>
					<div class='TFirst'>Di: </div>
					<div class='TSecond'>Francesco e Amilcar</div>
				</div>
				<div class='pair'>
					<div class='TFirst'>Telefono:</div>
					<div class='TSecond'>049628818</div>
				</div>
				<div class='pair'>
					<div class='TFirst'>E-Mail:</div>
					<div class='TSecond'>
						<a class='mailto' href='mailto:arsr.service".'@'."gmail.com' tabindex=\"9\">arsr.service".'@'."gmail.com </a>
						<img class='invisible' src='../img/mailto.png' alt='icona mail'/>
					</div>
				</div>
				<div class='pair'>
					<div class='TFirst'>Indirizzo:</div>
					<div class='TSecond'>Via Monzambano 2, Padova (PD)</div>
				</div>
			</div>
		</div>
		<div class='TContact'>
			<div class='contact_../data'>
				<div class='pair'><div class='TFirst'>Nome:</div><div class='TSecond'>Francesco</div></div>
				<div class='pair'><div class='TFirst'>Cognome: </div><div class='TSecond'>Agostini</div></div>
				<div class='pair'><div class='TFirst'>Telefono:</div><div class='TSecond'>3469468480</div></div>
				<div class='pair'><div class='TFirst'>E-Mail:</div><div class='TSecond'><a class='mailto' tabindex=\"10\" href='mailto:altair80486".'@'."gmail.com'>altair80486".'@'."gmail.com </a><img class='invisible' src='../public_html/img/mailto.png' alt='icona mail'/></div></div>
			</div>

		</div>
		<div class='TContact'>
			<div class='contact_../data'>
				<div class='pair'><div class='TFirst'>Nome:</div><div class='TSecond'>Amilcar Rafael</div></div>
				<div class='pair'><div class='TFirst'>Cognome: </div><div class='TSecond'>Rodriguez</div></div>
				<div class='pair'><div class='TFirst'>Telefono:</div><div class='TSecond'>342995486</div></div>
				<div class='pair'><div class='TFirst'>E-Mail:</div><div class='TSecond'><a class='mailto' tabindex=\"11\" href='mailto:sotorodriguez".'@'."gmail.com'>sotorodriguez".'@'."gmail.com </a><img class='invisible' src='../public_html/img/mailto.png' alt='icona mail'/></div></div>
			</div>
					
		</div>
		</div>
		
	$footer";
print($htmlprint);












