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
	
	$title = "Modifica Attrezzature";
	$where = "Modifica Attrezzature";
	require ("session.cgi");
	require("header.cgi");
	if($admin){
		require("menu.cgi");
		print "content-type: text/html\n\n";
		$htmlprint="$header$menu<div id=\"content\">";
		$htmlprint="$htmlprint<form id=\"insert_attrezzatura\" action=\"check_modifica_attrezzature.cgi\" method=\"post\" enctype='multipart/form-data'>
								<fieldset id=\"fieldset_attrezzature\">
								<input type=\"hidden\" name=\"codice\" value=\"$codice\" />
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_nome_nome\">
										<label>nome:</label>
									</div>
									<div id=\"form_attr_nome_input\">
										<input name=\"nome\" type=\"text\" maxlength=\"64\" value=\"$name\" />
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_img\">
										<div id=\"form_attr_img_nome\">
											<label>immagine:</label>
										</div>
											<input id=\"form_attr_img_input\" name=\"foto\" type=\"file\"  value=\"$source\" />
									</div>
									<div id=\"form_attr_img_alt\">
										<div id=\"form_attr_img_alt_nome\">
											<label>descrizione immagine:</label>
										</div>
										
											<textarea id=\"form_attr_img_alt_input\" name=\"alt\" rows=\"2\" cols=\"22\">$alt</textarea>
										
									</div>
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_descr_nome\">
										descrizione:
									</div>
										<textarea id=\"form_attr_descr_input\" name=\"descr\" rows=\"6\" cols=\"50\">$desc</textarea>
									
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_prezzo_nome\">
										prezzo:
									</div>
									
										<input id=\"fomr_attr_prezzo_input\" name=\"prezzo\" type=\"text\" value=\"$prezzo\" />€
								
								</div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_disp_name\">
										disponibilità:
									</div>
									<div id=\"form_attr_disp_input\" class=\"form_attr_disp_input_\">
									";
									
										$htmlprint="$htmlprint<input type=\"radio\" name=\"disp\" value=\"disponibile\"";
										if($disp eq "disponibile"){
										$htmlprint="$htmlprint checked=\"checked\"";
										}
										$htmlprint="$htmlprint/><label>disponibile</label></div>
										<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" value=\"non disponibile\"";
										if($disp eq "non disponibile"){
											$htmlprint="$htmlprint checked=\"checked\"";
										}
										$htmlprint="$htmlprint/>non disponibile</div>";
										if($disp ne "non disponibile" && $disp ne "disponibile"){
											$htmlprint="$htmlprint<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" checked=\"checked\"/>disponibile tra <input name=\"day\" type=\"text\" value=\"$day\" id=\"day_number\"/> giorni </div>";
										}
										else{
										$htmlprint="$htmlprint<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\"/>disponibile tra <input name=\"day\" type=\"text\" id=\"day_number\"/> giorni </div>"
										}
									$htmlprint="$htmlprint
									
								</div>
									<input class=\"pulsante\" id=\"pulsante_vai\" type=\"submit\" value=\"MODIFICA\" />
							</fieldset>
							</form>
							</div>";
		require("footer.cgi");
		$htmlprint="$htmlprint$footer";
		print $htmlprint;
	}


