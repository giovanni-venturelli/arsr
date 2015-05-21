#!"C:\strawberry\perl\bin\perl.exe"

$title = 'Servizo';
$where = "Servizo";
$header;
$menu;
$footer;
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
	<h3 class='SubTitle'>Servizi</h3>
		<h4 class='HParag'>Musica <span lang='en'>Live</span></h4>
		<p class='par1'>Microfoni, Casse, Mixer e tutto quello che serve per un ottimo show è a vostra disposizione. Al giorno d'oggi molte band e molti organizzatori di eventi hanno difficoltà nel trovare un buon servizio al giusto prezzo. Professionale... ma costoso, Economico... ma non professionale. Cosa scegliere? Professionale o economico? sei stufo di trovarti di fronte a questa scelta? E allora fai la scelta giusta! Noi offriamo la giusta via di mezzo, prezzi contenuti e professionalità!</p>

		<h4 class='HParag'>Feste e <span lang='en'>DJ Set</span></h4>
		<p class='par2'>Festa di compleanno? Voglia di ballare? Vuoi rendere indimenticabile il tuo 18° compleanno? Perchè spendere milioni per far la festa in discoteca quando la discoteca puoi farla a casa tua? Abbiamo impianti su misura per feste domestiche fino alle sale più grandi. Oltre a impianti audio di adeguata potenza per musica da discoteca abbiamo luci ed effetti di ogni tipo e per ogni gusto! Per rendere la tua festa qualcosa di unico e indimenticabile! E tutto ad un ottimo prezzo! Inoltre abbiamo la possibilità di mettervi in contatto con <span lang='en'>DJ</span> Personale bar e <span lang='en'>security</span>!</p>

		<h4 class='HParag'><span lang='en'>Studio Recording</span></h4>
		<p class='par3'>Hai una band e vorresti registrare una demo? Hai il pezzo del secolo in mente e vorresti registrarlo? Spesso e volentieri gli studi per registrare una semplice demo, offrendo servizi di altissimo livello e strutture hanno prezzi inaccessibili ai privati e alle band emergenti. Noi abbiamo la possibilit&agrave; di registrazione in multitraccia fino a 24 canali con possibilità di editing e mastering mediante software professionali! Disponiamo di una piccola struttura per la registrazione di singoli strumenti oppure la possibilit&agrave; di servizio di registrazione a domicilio direttamente nella vostra sala prove!</p>

	$footer";
print($htmlprint);












