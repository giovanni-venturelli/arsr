#!"C:\strawberry\perl\bin\perl.exe"
use XML::LibXML;
use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Cookie qw();
use CGI qw(:standard);
use DBI;
use utf8;

use XML::LibXML::NodeList;
use XML::LibXML::XPathContext;

	sub getSession(){
		$session = CGI::Session->load() or die $!;
		if($session->is_expired || $session->is_empty){
			return undef;
		}
		else{
			my $admin = $session->param('admin');
			$session;
		}
	}
	
	my $session=getSession;
	$page=new CGI;
	if($session){ #ATTENZIONE! ENTRO NELL'IF SENZA SESSIONE SOLO PER PROVARE LA PAGINA, DA MODIFICARE DOPO LA CREAZIONE DELLA PAGINA DI LOGIN
		require ("session.cgi");
		require("header.cgi");
		require("menu.cgi");
		print "content-type: text/html\n\n";
		$htmlprint="$header$menu<div id=\"content\">";
		$htmlprint="$htmlprint<form id=\"insert_attrezzatura\" action=\"check_insert_attrezzature.cgi\" method=\"post\" enctype='multipart/form-data'>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_nome_nome\">
										nome:
									</div>
									<div id=\"form_attr_nome_input\">
										<input name=\"nome\" type=\"text\" maxlength=\"64\" />
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_img\">
										<div id=\"form_attr_img_nome\">
											immagine:
										</div>
										<div id=\"form_attr_img_input\">
											<input name=\"img\" type=\"file\" name=\"img\" />
										</div>
									</div>
									<div id=\"form_attr_img_alt\">
										<div id=\"form_attr_img_alt_nome\">
											descrizione immagine:
										</div>
										<div id=\"form_attr_img_alt_input\">
											<textarea name=\"alt\" rows=\"2\" cols=\"22\"></textarea>
										</div>
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_descr_nome\">
										descrizione:
									</div>
									<div id=\"form_attr_descr_input\">
										<textarea name=\"descr\" rows=\"6\" cols=\"100\"></textarea>
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_prezzo_nome\">
										prezzo:
									</div>
									<div id=\"fomr_attr_prezzo_input\">
										<input name=\"prezzo\" type=\"text\" />€
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_disp_name\">
										disponibilità:
									</div>
									<div id=\"form_attr_disp_input\">
										<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" value=\"disponibile\" checked>disponibile</div>
										<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" value=\"non disponibile\">non disponibile</div>
										<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\">disponibile tra <input name=\"day\" type=\"number\" min=\"1\" max=\"9\"> giorni </div>
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<input class=\"pulsante_vai\" type=\"submit\" value=\"AGGIUNGI\" />
								</div>
							</form>
							</div>";
	}
	require("footer.cgi");
	$htmlprint="$htmlprint$footer";
	print $htmlprint;
