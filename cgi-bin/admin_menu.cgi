#!\"C:\xampp\perl\bin\perl.exe\"

use utf8;

sub ActiveLink{
	$nome = @_[0];
	$link = @_[1];
	$ref= @_[2];
	$ret;
	if ($nome eq $link){
	$ret=" id=\"active\">$link";
}
else {
	$ret="><a href=\"$ref\"> $link</a>";
}
return $ret;
}


$menu="<div id=\"menu\">
<ul>
<li class=\"menulist\"";
$temp=ActiveLink($where, "<span lang=\"en\">Home</span>", "administrator.cgi");
$menu="$menu$temp";
$menu="$menu
</li><li class=\"menulist\"";
$temp=ActiveLink($where, "Iserisci Attrezzature", "admin_attrezzature.cgi");
$menu="$menu$temp";
$menu="$menu</li>
<li class=\"menulist\"";
$temp=ActiveLink($where, "Staff", "admin_staff.cgi");
$menu="$menu$temp";
$menu="$menu
</li>
<li  class=\"menulist\"";
$temp=ActiveLink($where, "Edit Home", "admin_edithome.cgi");
$menu="$menu$temp";
$menu="$menu
</li>
</ul>
</div>
";
