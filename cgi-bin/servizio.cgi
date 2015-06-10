#!"C:\strawberry\perl\bin\perl.exe"

$title = 'Servizio';
$where = "Servizio";
$header;
$menu;
$footer;
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
		<h4 class='sub sub1'>Musica <span lang='en'>Live</span></h4>
		<p class='par par1'>Microfoni, Casse, <span lang='en'>Mixer</span> e tutto quello che serve per un ottimo <span lang='en'>show</span> &egrave; a vostra disposizione. Al giorno d'oggi molte <span lang='en'>band</span> e molti organizzatori di eventi hanno difficolt&agrave; nel trovare un buon servizio al giusto prezzo. Professionale... ma costoso, Economico... ma non professionale. Cosa scegliere? Professionale o economico? sei stufo di trovarti di fronte a questa scelta? E allora fai la scelta giusta! Noi offriamo la giusta via di mezzo, prezzi contenuti e professionalit&agrave!</p>

		<h4 class='sub sub2'>Feste e <span lang='en'><abbr title='disk jockey'>DJ</abbr> Set</span></h4>
		<p class='par par2'>Festa di compleanno? Voglia di ballare? Vuoi rendere indimenticabile il tuo 18° compleanno? Perch&egrave; spendere milioni per far la festa in discoteca quando la discoteca puoi farla a casa tua? Abbiamo impianti su misura per feste domestiche fino alle sale più grandi. Oltre a impianti audio di adeguata potenza per musica da discoteca abbiamo luci ed effetti di ogni tipo e per ogni gusto! Per rendere la tua festa qualcosa di unico e indimenticabile! E tutto ad un ottimo prezzo! Inoltre abbiamo la possibilit&agrave; di mettervi in contatto con <span lang='en'><abbr title='disk jockey'>DJ</abbr></span> Personale bar e <span lang='en'>security</span>!</p>

		<h4 class='sub sub3'><span lang='en'>Studio Recording</span></h4>
		<p class='par par3'>Hai una band e vorresti registrare una demo? Hai il pezzo del secolo in mente e vorresti registrarlo? Spesso e volentieri gli studi per registrare una semplice <span lang='en'>demo</span>, offrendo servizi di altissimo livello e strutture hanno prezzi inaccessibili ai privati e alle band emergenti. Noi abbiamo la possibilit&agrave; di registrazione in multitraccia fino a 24 canali con possibilità di <span lang='en'>editing</span> e <span lang='en'>mastering</span> mediante software professionali! Disponiamo di una piccola struttura per la registrazione di singoli strumenti oppure la possibilit&agrave; di servizio di registrazione a domicilio direttamente nella vostra sala prove!</p>
		
		<div class='validation center'><img class='image2' src='../public_html/img/vcss.gif' alt='logo validazione css'/><img class='image2' src='../public_html/img/vxhtml.png' alt='validazione html'/></div>
		</div>
	$footer";
print($htmlprint);












