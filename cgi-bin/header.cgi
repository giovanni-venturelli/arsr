	#!"C:\xampp\perl\bin\perl.exe"

	use utf8;
	
		$page = new CGI;
		$session = CGI::Session->load() or die $!;
		$utente = $session->param('utente');
		$admin = $session->param('admin');

	
	if($utente){
		$log="<div id=\"stato_utente\">sei collegato come $utente, <a href=\"logout.cgi\">[esci]</a></div>";
	}
	elsif($admin){
		$log="<div id=\"stato_utente\">sei collegato come $admin, <a href=\"logout.cgi\">[esci]</a></div>";
	}
	else{
		$log="<div id=\"stato_utente\">non sei collegato, <a href=\"login.cgi\">[login]</a> , <a href=\"registration.cgi\">[registrati]</a></div>";
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
	<a href=\"index.cgi\">
	<h1>
	<abbr>ARSR</abbr>
	<span lang=\"en\">Service</span>
	</h1>
	<h2>Audio e luci di qualità per il tuo Spettacolo</h2>
	</a>";
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
			<link rel=\"stylesheet\" type=\"text/css\" media=\"only screen and (max-device-width: 640px)\" href=\"../public_html/css/mobilestyle.css\" />
			<link rel=\"stylesheet\" type=\"text/css\" media=\"(max-width: 766px)\" href=\"../public_html/css/smallwinstyle.css\" />
			<link rel=\"stylesheet\" type=\"text/css\" media =\"(min-width: 767px) and (min-device-width: 1024px)\"  href=\"../public_html/css/generalstyle.css\" />
			<link rel=\"stylesheet\" type=\"text/css\" media =\"(min-width: 767px) and (min-device-width: 1024px)\"  href=\"../public_html/css/css_matteo.css\" />
			
			<link rel=\"stylesheet\" type=\"text/css\" media =\"(min-width: 767px) and (min-device-width: 1024px)\"  href=\"../public_html/css/css_nico.css\" />
			<link rel=\"stylesheet\" type=\"text/css\" media =\"(min-width: 767px) and (min-device-width: 1024px)\"  href=\"../public_html/css/css_francesco.css\" />
			<link rel=\"stylesheet\" type=\"text/css\" media=\"(max-width: 766px)\" href=\"../public_html/css/css_francesco_mobile.css\" />
			<link rel=\"stylesheet\" type=\"text/css\" media=\"(max-width: 766px)\" href=\"../public_html/css/mobile_nico.css\" />
			
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
	<a href=\"https://www.facebook.com/arsrservice?fref=ts\" target=\"new\" title=\"Pagina Facebook\" id=\"range-logo\">pagina <span lang=\"en\">facebook</span>
	</a>
	</div>
	</div>";


	1;
