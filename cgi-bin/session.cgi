#!"C:\xampp\perl\bin\perl.exe"

use CGI;
use CGI::Session;
$session = CGI::Session->load() or die $!;
my %map = (
	'>' => '&gt;',
	'<' => '&lt;'
	);#crea mappa per l'escape dei tag html in lettura da xml
$utente = $session->param('utente');
$admin = $session->param('admin');
if ($utente){
	$utente=~ s/([<>])/$map{$1}/g;
}
if ($admin){
	$admin=~ s/([<>])/$map{$1}/g;
}
return 1;