#!"C:\strawberry\perl\bin\perl.exe"
use XML::LibXML;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser);
use utf8;


$title="Servizio";
$where="Servizio";
#!"C:\xampp\perl\bin\perl.exe"
require ("session.cgi");
require ("header.cgi");
require ("menu.cgi");
require ("footer.cgi");
$page = new CGI;
print $page->header;


my $htmlprint;
$htmlprint= "$header$menu<div id=\"content\">
	<h4 class='sub' id='sub1'>Musica <span lang='en'>Live</span></h4>
		<p class='par'>Microfoni, Casse, <span lang='en'>Mixer</span> e tutto quello che serve per un ottimo <span lang='en'>show</span> &egrave; a vostra disposizione. Al giorno d'oggi molte <span lang='en'>band</span> e molti organizzatori di eventi hanno difficolt&agrave; nel trovare un buon servizio al giusto prezzo. Professionale... ma costoso, Economico... ma non professionale. Cosa scegliere? Professionale o economico? sei stufo di trovarti di fronte a questa scelta? E allora fai la scelta giusta! Noi offriamo la giusta via di mezzo, prezzi contenuti e professionalit&agrave;!</p>

		<h4 class='sub'id='sub2'>Feste e <span lang='en'><abbr title='disk jockey'>DJ</abbr> Set</span></h4>
		<p class='par'>Festa di compleanno? Voglia di ballare? Vuoi rendere indimenticabile il tuo 18° compleanno? Perch&egrave; spendere milioni per far la festa in discoteca quando la discoteca puoi farla a casa tua? Abbiamo impianti su misura per feste domestiche fino alle sale più grandi. Oltre a impianti audio di adeguata potenza per musica da discoteca abbiamo luci ed effetti di ogni tipo e per ogni gusto! Per rendere la tua festa qualcosa di unico e indimenticabile! E tutto ad un ottimo prezzo! Inoltre abbiamo la possibilit&agrave; di mettervi in contatto con <span lang='en'><abbr title='disk jockey'>DJ</abbr></span> Personale bar e <span lang='en'>security</span>!</p>

		<h4 class='sub' id='sub3'><span lang='en'>Studio Recording</span></h4>
		<p class='par'>Hai una band e vorresti registrare una demo? Hai il pezzo del secolo in mente e vorresti registrarlo? Spesso e volentieri gli studi per registrare una semplice <span lang='en'>demo</span>, offrendo servizi di altissimo livello e strutture hanno prezzi inaccessibili ai privati e alle band emergenti. Noi abbiamo la possibilit&agrave; di registrazione in multitraccia fino a 24 canali con possibilità di <span lang='en'>editing</span> e <span lang='en'>mastering</span> mediante software professionali! Disponiamo di una piccola struttura per la registrazione di singoli strumenti oppure la possibilit&agrave; di servizio di registrazione a domicilio direttamente nella vostra sala prove!</p>


";


require("footer.cgi");
$htmlprint="$htmlprint</div>$footer";
print $htmlprint;


		










