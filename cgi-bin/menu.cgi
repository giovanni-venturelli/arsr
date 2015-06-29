#!\"C:\xampp\perl\bin\perl.exe\"

use utf8;

$tab=4;
sub ActiveLink{
	$nome = @_[0];
	$link = @_[1];
	$ref= @_[2];
	$ret;
	if ($nome eq $link){
	$ret=" id=\"active\">$link";
}
else {
	$ret="><a href=\"$ref\" tabindex=\"$tab\"> $link</a>";
	$tab=$tab+1;
}
return $ret;
}


$menu="<div id=\"menu\">

<ul>
<li class=\"menulist\"";
$temp=ActiveLink($where, "<span lang=\"en\">Home</span>", "index.cgi");
$menu="$menu$temp";
$menu="$menu
</li><li class=\"menulist\"";
$temp=ActiveLink($where, "Noleggio Attrezzature", "attrezzature.cgi");
$menu="$menu$temp";
$menu="$menu</li>
<li class=\"menulist\"";
$temp=ActiveLink($where, "Servizio", "servizio.cgi");
$menu="$menu$temp";
$menu="$menu
</li>
<li class=\"menulist\"";
$temp=ActiveLink($where, "Staff", "staff.cgi");
$menu="$menu$temp";
$menu="$menu
</li>
<li  class=\"menulist\"";
$temp=ActiveLink($where, "Dicono di Noi", "feedback.cgi");
$menu="$menu$temp";
$menu="$menu
</li>
<li  class=\"menulist\"";
$temp=ActiveLink($where, "Contatti", "contatti.cgi");
$menu="$menu$temp";
$menu="$menu</li>
</ul>
</div>
";
