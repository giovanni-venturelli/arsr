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
		$htmlprint="$htmlprint<form id=\"insert_attrezzatura\" action=\"check_modifica_attrezzature.cgi\" method=\"post\" enctype='multipart/form-data' onsubmit=\"return validateAttrForm(this)\">
								<fieldset id=\"fieldset_attrezzature\">
								<input type=\"hidden\" name=\"codice\" value=\"$codice\" />
								<div class=\"form_attr_nome\">
										<label class=\"label_block\" for=\"form_attr_nome_input\">nome:</label>
										<input id=\"form_attr_nome_input\" name=\"nome\" type=\"text\" maxlength=\"64\" value=\"$name\" tabindex=\"10\" />
								</div>
								<div class=\"form_attr_nome\">
										<label for=\"form_attr_img_input\" id=\"form_attr_img_nome\" class=\"label_block\">
											immagine:
										</label>
											<input name=\"foto\" type=\"file\" id=\"form_attr_img_input\" value=\"$source\" tabindex=\"11\" />";
											if($errore_foto){
												$htmlprint="$htmlprint <div class=\"errore_attrezzature\"> ERRORE: selezionare un file immagine valido </div>"
											}
									$htmlprint="$htmlprint
										<label for=\"form_attr_img_alt_input\" class=\"label_block\" id=\"form_attr_img_alt_nome\">
											descrizione immagine:
										</label>
											<textarea name=\"alt\" rows=\"2\" cols=\"52\" id=\"form_attr_img_alt_input\" tabindex=\"12\" onkeyup=\"checkNotEmpty(this)\">$alt</textarea> <div class=\"registration_message\" id=\"form_attr_img_alt_input_check\">campo non valido</div>
								</div>
								<div class=\"form_attr_nome\">
									<label for=\"form_attr_descr_input\" class=\"label-block\" id=\"form_attr_descr_nome\">
										descrizione:
									</label>
										<textarea name=\"descr\" rows=\"6\" cols=\"10\" id=\"form_attr_descr_input\" tabindex=\"13\">$desc</textarea>
								</div>
								<div class=\"form_attr_nome\">
									<label for=\"form_attr_prezzo_input\" class=\"label_block\" id=\"form_attr_prezzo_nome\">
										prezzo:
									</label>
										<input name=\"prezzo\" type=\"text\"  id=\"form_attr_prezzo_input\" tabindex=\"14\" onkeyup=\"checkNumber(this)\" value=\"$prezzo\"/>€ (0-9999)<div class=\"registration_message\" id=\"form_attr_prezzo_input_check\">campo non valido</div>
									";
									if($errore_prezzo){
										$htmlprint="$htmlprint<div class=\"errore_attrezzature\">ERRORE: inserire un numero compreso tra 0 e 9999</div>";
									}
								$htmlprint="$htmlprint</div>
								<div class=\"form_attr_nome\">
									<div class=\"label_block\" id=\"form_attr_disp_name\">
										disponibilità:
									</div>";
										$htmlprint="$htmlprint<div><input type=\"radio\" name=\"disp\" id=\"form_attr_disponibile\" value=\"disponibile\" tabindex=\"15\"";
										if($disp eq "disponibile"){
										$htmlprint="$htmlprint checked=\"checked\"";
										}
										$htmlprint="$htmlprint/><label for=\"form_attr_disponibile\" >disponibile</label></div>
										<div><input type=\"radio\" name=\"disp\" id=\"form_attr_non_disponibile\" value=\"non disponibile\" tabindex=\"16\"";
										if($disp eq "non disponibile"){
											$htmlprint="$htmlprint checked=\"checked\"";
										}
										$htmlprint="$htmlprint/><label for=\"form_attr_disponibile\">non disponibile</label></div>";
										if($disp ne "non disponibile" && $disp ne "disponibile"){
											$htmlprint="$htmlprint<div><input type=\"radio\" name=\"disp\" id=\"disp_tra_input\" checked=\"checked\" tabindex=\"17\"/><label for=\"disp_tra_input\">disponibile tra</label> <input name=\"day\" type=\"text\" value=\"$day\" tabindex=\"18\" id=\"day_number\" onkeyup=\"checkDayNumber(this)\"/><label for=\"day_number\"> giorni (0-9)</label><div class=\"registration_message\" id=\"day_number_check\">campo non valido</div>";
											if($errore_numero){
												$htmlprint="$htmlprint <div class=\"errore_attrezzature\"> ERRORE: inserire un numero compreso tra 1 e 9 </div> "
											}
											$htmlprint="$htmlprint </div>";
										}
										else{
										$htmlprint="$htmlprint<div><input type=\"radio\" id=\"disp_tra_input\" name=\"disp\" tabindex=\"17\"/><label for=\"disp_tra_input\">disponibile tra</label><input name=\"day\" type=\"text\" id=\"day_number\" value=\"$day\" tabindex=\"18\" onkeyup=\"checkDayNumber(this)\"/> <label for=\"day_number\"> giorni (0-9)</label><div class=\"registration_message\" id=\"day_number_check\">campo non valido</div></div>"
										}
									$htmlprint="$htmlprint
								
								</div>
									<input class=\"pulsante\" id=\"pulsante_vai\" type=\"submit\" value=\"MODIFICA\" tabindex=\"19\" />
							</fieldset>
							</form>
							</div>";
		require("footer.cgi");
		$htmlprint="$htmlprint$footer";
		print $htmlprint;
	}


