	#!"C:\xampp\perl\bin\perl.exe"

	use utf8;
	

	
	if($utente){
		$log="<div id=\"stato_utente\">sei collegato come $utente, <a href=\"logout.cgi\" class=\"link_header\">[esci]</a></div>";
	}
	elsif($admin){
		$log="<div id=\"stato_utente\">sei collegato come $admin, <a href=\"logout.cgi\" class=\"link_header\">[esci]</a></div>";
	}
	elsif($title ne "Login" && $title ne "Registrazione"){
		$log="<div id=\"stato_utente\">non sei collegato, <a href=\"login.cgi\" class=\"link_header\">[login]</a> , <a href=\"registration.cgi\" class=\"link_header\">[registrati]</a></div>";
	}
	elsif($title eq "Registrazione"){
		$log="<div id=\"stato_utente\">non sei collegato, <a href=\"login.cgi\" class=\"link_header\">[login]</a> </div>";
	}
	else{
		$log="<div id=\"stato_utente\">non sei collegato, <a href=\"registration.cgi\" class=\"link_header\">[registrati]</a></div>";
	}
	
	$ref;
	if ($where eq "<span lang=\"en\">Home</span>"){
		$ref="$log
	<h1>
	<abbr>ARSR</abbr>
	<span lang=\"en\">Service</span>
	</h1>
	<h2>Audio e luci di qualità per il tuo Spettacolo</h2>";
	}
else{
	$ref="$log
	<h1>
	<abbr>ARSR</abbr>
	<span lang=\"en\">Service</span>
	</h1>
	<h2>Audio e luci di qualità per il tuo Spettacolo</h2>
	";
}
	$header= "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
	<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\">
		<head>
			<title>$title - ARSR</title>
			<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/> 
			<meta name=\"description\" content=\"login per nuove news\"/>
			<meta name=\"keywords\" content=\"attrezzatura, inserimento\"/> 
	        <meta name=\"language\" content=\"italian it\"/> 
			<meta name=\"author\" content=\"y-tech\"/>

			<link rel=\"stylesheet\" type=\"text/css\" media=\"(max-width: 50.99em)\" href=\"../public_html/css/mobilestyle.css\" />
			<link rel=\"stylesheet\" type=\"text/css\" media =\"(min-width: 51em) and (min-device-width: 68em)\"  href=\"../public_html/css/generalstyle.css\" />
			<script type=\"text/javascript\" src=\"../public_html/js/script.js\"></script>
		</head>
		<body>
				<div id=\"main\">
				<div id=\"header\">
$ref

	</div>
	<div id=\"subheader\">
	<div id=\"position\">
	Ti trovi in: $where</div>
	<div class=\"social\" id=\"facebook\">
	<a href=\"https://www.facebook.com/arsrservice?fref=ts\" title=\"Pagina Facebook\" id=\"range-logo\">pagina <span lang=\"en\">facebook</span>
	</a>
	</div>
	</div>";


	1;
