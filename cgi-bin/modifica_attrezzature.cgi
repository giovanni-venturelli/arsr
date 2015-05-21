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
	
	$parser = XML::LibXML->new();
	my $file = "../data/attrezzature.xml";
	my $doc = $parser->parse_file($file);
		if(!$doc){
			$ERRORE=1;
		}
	my $root= $doc->getDocumentElement;
	@items = $root->getElementsByTagName('attrezzatura');
	foreach $item(@items){
		if($item->find('codice_prodotto') eq $page->param('cod_')){
			$name=$item->find('nome');
			$desc=$item->find('descrizione');
			$prezzo=$item->find('prezzo');
				$prezzo=substr($prezzo, 0, -1); # tolgo il simbolo € dalla variabile
			$source=$item->find('img/source');
			$alt=$item->find('img/alt');
			$disp=$item->find('disponibile');
				$day=substr($disp,16,1); #disponibile tra x giorni -> x è in posizione 16
			$codice=$item->find('codice_prodotto');
			# qua ci va un'istruzione per interrompere il ciclo!
		}
	}
	if($session || !$session){ #ATTENZIONE! ENTRO NELL'IF SENZA SESSIONE SOLO PER PROVARE LA PAGINA, DA MODIFICARE DOPO LA CREAZIONE DELLA PAGINA DI LOGIN
		require("header.cgi");
		require("admin_menu.cgi");
		print "content-type: text/html\n\n";
		$htmlprint="$header$menu<div id=\"content\">";
		$htmlprint="$htmlprint<form id=\"insert_attrezzatura\" action=\"check_modifica_attrezzature.cgi\" method=\"post\">
								<input type=\"hidden\" name=\"codice\" value=\"$codice\" />
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_nome_nome\">
										nome:
									</div>
									<div id=\"form_attr_nome_input\">
										<input name=\"nome\" type=\"text\" maxlength=\"64\" value=\"$name\" />
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_img\">
										<div id=\"form_attr_img_nome\">
											immagine:
										</div>
										<div id=\"form_attr_img_input\">
											<input name=\"img\" type=\"file\" name=\"img\" value=\"$source\" />
										</div>
									</div>
									<div id=\"form_attr_img_alt\">
										<div id=\"form_attr_img_alt_nome\">
											descrizione immagine:
										</div>
										<div id=\"form_attr_img_alt_input\">
											<textarea name=\"alt\" rows=\"2\" cols=\"22\">$alt</textarea>
										</div>
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_descr_nome\">
										descrizione:
									</div>
									<div id=\"form_attr_descr_input\">
										<textarea name=\"descr\" rows=\"6\" cols=\"100\">$desc</textarea>
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_prezzo_nome\">
										prezzo:
									</div>
									<div id=\"fomr_attr_prezzo_input\">
										<input name=\"prezzo\" type=\"text\" value=\"$prezzo\" />€
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_disp_name\">
										disponibilità:
									</div>
									<div id=\"form_attr_disp_input\">";
									if($disp eq "disponibile"){
										$htmlprint="$htmlprint<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" value=\"disponibile\" checked>disponibile</div>
										<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" value=\"non disponibile\">non disponibile</div>
										<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\">disponibile tra <input name=\"day\" type=\"number\" min=\"1\" max=\"9\"> giorni </div>"
									}
									elsif($disp eq "non disponibile"){
										$htmlprint="$htmlprint<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" value=\"disponibile\">disponibile</div>
										<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" value=\"non disponibile\" checked>non disponibile</div>
										<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\">disponibile tra <input name=\"day\" type=\"number\" min=\"1\" max=\"9\"> giorni </div>"
									}
									else{
										$htmlprint="$htmlprint<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" value=\"disponibile\">disponibile</div>
										<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" value=\"non disponibile\">non disponibile</div>
										<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" checked>disponibile tra <input name=\"day\" type=\"number\" min=\"1\" max=\"9\" value=\"$day\"> giorni </div>"
									}
									$htmlprint="$htmlprint	
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<input class=\"pulsante submit\" id=\"pulsante_vai\" type=\"submit\" value=\"MODIFICA\" />
								</div>
							</form>
							</div>";
		require("footer.cgi");
		$htmlprint="$htmlprint$footer";
		print $htmlprint;
	}


