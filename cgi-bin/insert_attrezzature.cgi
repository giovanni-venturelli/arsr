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
$page = new CGI;
$title="Inserisci Attrezzatura";
$where="Inserisci attrezzatura";
	require("session.cgi");
	require("header.cgi");
	require("menu.cgi");
	$htmlprint="$header$menu<div id=\"content\">";

	if($admin){
		print "content-type: text/html\n\n";
		$htmlprint="$htmlprint<form id=\"insert_attrezzatura\" action=\"check_insert_attrezzature.cgi\" method=\"post\" enctype='multipart/form-data' onsubmit=\"return validateAttrForm(this)\">
								<fieldset id=\"fieldset_attrezzature\">
								<div class=\"form_attr_nome\">
									<label for=\"form_attr_nome_input\" class=\"label_block\">
										nome:
									</label>
										<input name=\"nome\" type=\"text\" maxlength=\"64\" id=\"form_attr_nome_input\" onkeyup=\"checkNotEmpty(this)\"/> <div class=\"registration_message\" id=\"form_attr_nome_input_check\">campo non valido</div>
								</div>
								<div class=\"form_attr_nome\">
										<label for=\"form_attr_img_input\" id=\"form_attr_img_nome\" class=\"label_block\">
											immagine:
										</label>
											<input name=\"foto\" type=\"file\" id=\"form_attr_img_input\" />";
										if($errore_foto){
											$htmlprint="$htmlprint<div class=\"errore_attrezzature\">ERRORE: inserire un file immagine valido</div>";
										}
									$htmlprint="$htmlprint
										<label for=\"form_attr_img_alt_input\" class=\"label_block\" id=\"form_attr_img_alt_nome\">
											descrizione immagine:
										</label>
											<textarea name=\"alt\" rows=\"2\" cols=\"52\" id=\"form_attr_img_alt_input\" onkeyup=\"checkNotEmpty(this)\"></textarea> <div class=\"registration_message\" id=\"form_attr_img_alt_input_check\">campo non valido</div>

								</div>
								<div class=\"form_attr_nome\">
																		<label for=\"form_attr_descr_input\" class=\"label-block\" id=\"form_attr_descr_nome\">
										descrizione:
									</label>
										<textarea name=\"descr\" rows=\"6\" cols=\"10\" id=\"form_attr_descr_input\"></textarea>
								</div>
								<div class=\"form_attr_nome\">
									<label for=\"form_attr_prezzo_input\" class=\"label_block\" id=\"form_attr_prezzo_nome\">
										prezzo:
									</label>
										<input name=\"prezzo\" type=\"text\"  id=\"form_attr_prezzo_input\" onkeyup=\"checkNumber(this)\"/>€ <div class=\"registration_message\" id=\"form_attr_prezzo_input_check\">campo non valido</div>
									";
									if($errore_prezzo){
										$htmlprint="$htmlprint<div class=\"errore_attrezzature\">ERRORE: inserire un numero compreso tra 0 e 9999</div>";
									}
								$htmlprint="$htmlprint</div>
								<div class=\"form_attr_nome\">
									<div class=\"label_block\" id=\"form_attr_disp_name\">
										disponibilità:
									</div>";
										$htmlprint="$htmlprint<div><input type=\"radio\" name=\"disp\" id=\"form_attr_disponibile\" value=\"disponibile\"";
										if($disp eq "disponibile"){
										$htmlprint="$htmlprint checked=\"checked\"";
										}
										$htmlprint="$htmlprint/><label for=\"form_attr_disponibile\" >disponibile</label></div>
										<div><input type=\"radio\" name=\"disp\" id=\"form_attr_non_disponibile\" value=\"non disponibile\"";
										if($disp eq "non disponibile"){
											$htmlprint="$htmlprint checked=\"checked\"";
										}
										$htmlprint="$htmlprint/><label for=\"form_attr_disponibile\">non disponibile</label></div>";
										if($disp ne "non disponibile" && $disp ne "disponibile"){
											$htmlprint="$htmlprint<div><input type=\"radio\" name=\"disp\" id=\"disp_tra_input\" checked=\"checked\"/><label for=\"disp_tra_input\">disponibile tra</label> <input name=\"day\" type=\"text\" value=\"$day\" id=\"day_number\" onkeyup=\"checkDayNumber(this)\"/><label for=\"day_number\"> giorni (0-9)</label><div class=\"registration_message\" id=\"day_number_check\">campo non valido</div>";
											if($errore_numero){
												$htmlprint="$htmlprint <div class=\"errore_attrezzature\"> ERRORE: inserire un numero compreso tra 1 e 9 </div> "
											}
											$htmlprint="$htmlprint </div>";
										}
										else{
										$htmlprint="$htmlprint<div><input type=\"radio\" id=\"disp_tra_input\" name=\"disp\"/><label for=\"disp_tra_input\">disponibile tra</label><input name=\"day\" type=\"text\" id=\"day_number\" onkeyup=\"checkDayNumber(this)\"/> <label for=\"day_number\"> giorni (0-9)</label><div class=\"registration_message\" id=\"day_number_check\">campo non valido</div></div>"
										}
									$htmlprint="$htmlprint
									
									</div>
									<input class=\"pulsante\" type=\"submit\" value=\"AGGIUNGI\" />

								</fieldset>
							</form>
							</div>";
	}
	require("footer.cgi");
	$htmlprint="$htmlprint$footer";
	print $htmlprint;
