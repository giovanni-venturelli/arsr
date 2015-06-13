#!"C:\xampp\perl\bin\perl.exe"

use CGI;
use CGI::Session;
$session = CGI::Session->load() or die $!;
$utente = $session->param('utente');
$admin = $session->param('admin');
return 1;