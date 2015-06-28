#!"C:\strawberry\perl\bin\perl.exe"

use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Cookie qw();
use CGI::Session;
use CGI;
use DBI;
use utf8;


my $htmlprint;
sub pageList{
	$numero= @_[0];
	my $ret="";
	my $numid=@_[1];
	my $num=@_[2];
	my $link=@_[3];
	if( $utente){
$ret="<span class=\"link_to_comment\">";
if($link!=0){
$ret="$ret<a href=\"\#bottom\">";
}
$ret="$ret Lascia un commento";
if($link!=0){
$ret="$ret</a>";
}
$ret="$ret</span>";
} 
if($numid>10){
#
#if($utente){
#$ret="$ret<span class=\"link_to_comment\"><a href=\"\#bottom\">Lascia un commento</a></span>";
#} 
#=cut
	$pagelist=" <fieldset class=\"fieldset_page\"><label for=\"page_number_$numero\">Sei a pagina $num vai a pagina</label><select name=\"pagina\" id=\"page_number_$numero\"";
$top;
$top=$numid/10;

for($p=1;$p<($top+1);$p++){

if($p != $num){
$pagelist="$pagelist><option value=\"$p\"";
	if($p==$num+1){
$pagelist="$pagelist selected=\"selected\"";
}
$pagelist="$pagelist>$p</option>";
}
}
$pagelist="$pagelist</select>";

$ret="$ret<div class=\"pagine\"><form method=\"get\" class=\"form_pagine\" action=\"#\">$pagelist
<input class=\"pulsante pagine_submit\"  type=\"submit\" value=\"VAI\"/>
</fieldset></form></div>";
}# end if ($numid>10)

return $ret;
}


$title = 'Guestbook';
$where = "Dicono di Noi";

require("session.cgi");

require ("header.cgi");
$page = new CGI;



print $session->header();
#crea un oggetto CGI

my $parser = XML::LibXML->new();

$header;
$menu;
$footer;



require ("menu.cgi");
require ("footer.cgi");
$htmlprint= "$header$menu<div id=\"content\">";
my $file='../data/feedback.xml';
my $doc = $parser->parse_file($file);
#controllo se il file è aperto
if(!$doc){$ERRORE=1;}
#trovo il nodo radice
my $root = $doc->getDocumentElement;
@feed = $root->getElementsByTagName('feedback');
$numid=@feed;
@reversefeed=reverse(@feed);
$buffer = $ENV{'QUERY_STRING'};
@pairs = split(/&/, $buffer);
$numpair=@pairs;
$num;
$contatore=0;
if($numpair){
foreach $pair (@pairs) {
($name, $value) = split(/=/, $pair);
$num=$value;
}
}#if($numpair)
else {
  $num=1;
}
$lim1=$num*10;
$lim2=$lim1-10;
$pagelist;

if($num eq 1){ #se siamo a pagina 1 visualizza il riquadro di descrizione
$htmlprint="$htmlprint <div id=\"feedback_main\"><h3>GUESTBOOK</h3>Questo è il libro degli ospiti, puoi leggere cosa pensano di noi i nostri collaboratori e puoi tu stesso lasciare un commento.</div>";
}

if(!$utente && !$admin){
	$htmlprint="$htmlprint<div>Effettua il log in per lasciare un commento.</div>";
}
elsif(!$utente && $admin){
	$htmlprint="$htmlprint<div>Effettua il log in come utente normale per lasciare un commento.</div>";
}
$htmlprint=$htmlprint.pageList(1, $numid, $num,1);
		foreach $nod (@reversefeed){
			if (((!$numpair||$num == 1)&&($contatore < 10))||($contatore < $lim1 && $contatore >= $lim2)){
				my $nodid=$nod->findvalue('id');
				my $author=$nod->find('autore');
				my $date=$nod->find('data');
				my $body=$nod->find('corpo');
				my %map = (
						'>' => '&gt;',
						'<' => '&lt;'
						);#crea mappa per l'escape dei tag html in lettura da xml
						$body =~ s/([<>])/$map{$1}/g; #escape dei tag html in xml
				my $image=$nod->find('immagine');
				$htmlprint="$htmlprint<div class=\"commento\">
				<img class=\"commento_immagine\" src=\"..\/public_html\/img\/avatars\/$image\" alt=\"Immagine di profilo di $author\"/>";
				if($author eq $utente || $admin){
				$htmlprint=$htmlprint."<form action=\"delete_feedback.cgi\" method=\"post\">
				<fieldset class=\"fieldset_feedback\">
				<input type=\"hidden\" name=\"id\" value=\"$nodid\" /><input type=\"submit\" class=\"pulsante erase\" value=\"elimina\"/>";
				
				$htmlprint="$htmlprint</fieldset></form>";
					}
				$htmlprint="$htmlprint<div class=\"commento_content\">$prova
				<p class=\"commento_autore\"><strong>$author</strong></p>
				<p class=\"commento_corpo\">$body</p>
				<div class=\"commento_intestazione\">
				<p class=\"commento_numdat\">commento \#$nodid</p>
				<p class=\"commento_numdat\">$date</p>

				</div>
				</div>\n
				</div>\n";
			}
			$contatore++;

		}

$htmlprint="$htmlprint
<div class=\"pagine\">";
if($numid>10){
  $htmlprint=$htmlprint
.pageList(2,$numid,$num,0);
}
$htmlprint="$htmlprint<div id=\"back_to_top\"><a href=\"\#\" id=\"back_to_top_link\">torna in alto</a></div>";

$htmlprint="$htmlprint</div>";
	if($utente){
		$htmlprint="$htmlprint
		<form method=\"post\" action=\"check_feedback.cgi\">
		<fieldset id=\"feedbackfieldset\">
		<div class=\"form-group\" id=\"bottom\">
		<label id=\"commento_label\" for=\"commento_textarea\">Inserisci un commento</label>
		<textarea name=\"feed_body\" id=\"commento_textarea\" rows=\"20\" cols=\"10\"></textarea>
		</div> 
		<input id=\"commento_submit\" class=\"pulsante\" type=\"submit\" value=\"INSERISCI\"/>
		</fieldset>
		</form>
		";
	}
$htmlprint="$htmlprint</div>\n$footer";
print $htmlprint;
