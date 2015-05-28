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
$session = CGI::Session->load() or die $!;
my $admin = $session->param('admin');

my $session=getSession;
$page=new CGI;
print($page->header());

my $htmlprint;
require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
$htmlprint= "$header$menu<div id=\"content\">";
$htmlprint="$htmlprint
		<div class='TContact'>
			<div class='right'>
				<img class='image' src='../public_html/img/live.png' alt='immagine contatto'/>
			</div>
			<div class='left'>
				<div class='TFirst'>Ditta:</div><div class='TSecond'>A.R.S.R.</div><div class='break'></div>
				<div class='TFirst'>Di: </div><div class='TSecond'>Francesco e Amilcar</div><div class='break'></div>
				<div class='TFirst'>Telefono:</div><div class='TSecond'>049628818</div><div class='break'></div>
				<div class='TFirst'>E-Mail:</div><div class='TSecond'><a class='mailto' href='mailto:arsr.service".'@'."gmail.com'>arsr.service".'@'."gmail.com </a><img class='invisible' src='../public_html/img/mailto.png' alt='icona mail'/></div><div class='break'></div>
				<div class='TFirst'>Indirizzo:</div><div class='TSecond'>Via Monzambano 2, Padova (PD)</div><div class='break'></div>
			</div>
			<div class='break'></div>
		</div>
		<div class='TContact'>
			<div class='right'>
				<img class='image' src='../public_html/img/mixer.png' alt='immagine contatto'/>
			</div>
			<div class='left'>
				<div class='TFirst'>Ditta:</div><div class='TSecond'>Francesco</div><div class='break'></div>
				<div class='TFirst'>Di: </div><div class='TSecond'>Agostini</div><div class='break'></div>
				<div class='TFirst'>Telefono:</div><div class='TSecond'>3469468480</div><div class='break'></div>
				<div class='TFirst'>E-Mail:</div><div class='TSecond'><a class='mailto' href='mailto:altair80486".'@'."gmail.com'>altair80486".'@'."gmail.com </a><img class='invisible' src='../public_html/img/mailto.png' alt='icona mail'/></div><div class='break'></div>
			</div>
			<div class='break'></div>
		</div>
		<div class='TContact'>
			<div class='right'>
				<img class='image' src='../public_html/img/nota2.png' alt='immagine contatto'/>
			</div>
			<div class='left'>
				<div class='TFirst'>Ditta:</div><div class='TSecond'>Amilcar Rafael</div><div class='break'></div>
				<div class='TFirst'>Di: </div><div class='TSecond'>Rodriguez</div><div class='break'></div>
				<div class='TFirst'>Telefono:</div><div class='TSecond'>342995486</div><div class='break'></div>
				<div class='TFirst'>E-Mail:</div><div class='TSecond'><a class='mailto' href='mailto:sotorodriguez".'@'."gmail.com'>sotorodriguez".'@'."gmail.com </a><img class='invisible' src='../public_html/img/mailto.png' alt='icona mail'/></div><div class='break'></div>
			</div>
			<div class='break'></div>
		</div>
		<div class='validation center'><img class='image2' src='../public_html/img/vcss.gif' alt='logo validazione css'/><img class='image2' src='../public_html/img/vxhtml.png' alt='validazione html'/><div class='break'></div></div>
	</div>
	$footer";
print($htmlprint);












