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
		$htmlprint="$htmlprint<form id=\"insert_attrezzatura\" action=\"check_insert_attrezzature.cgi\" method=\"post\" enctype='multipart/form-data'>
								<fieldset id=\"fieldset_attrezzature\">
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
											<input name=\"foto\" type=\"file\" />";
										if($errore_foto){
											$htmlprint="$htmlprint<div class=\"errore_attrezzature\">ERRORE: inserire un file immagine valido</div>";
										}
									$htmlprint="$htmlprint</div></div>
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
									";
									if($errore_prezzo){
										$htmlprint="$htmlprint<div class=\"errore_attrezzature\">ERRORE: inserire un numero compreso tra 0 e 9999</div>";
									}
								$htmlprint="$htmlprint</div></div>
								<div class=\"form_attr_nome\">
									<div id=\"form_attr_disp_name\">
										disponibilità:
									</div>
									<div id=\"form_attr_disp_input\">";
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
											$htmlprint="$htmlprint<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\" checked=\"checked\"/>disponibile tra <input name=\"day\" type=\"text\" value=\"$day\" id=\"day_number\"/> giorni";
											if($errore_numero){
												$htmlprint="$htmlprint <div class=\"errore_attrezzature\"> ERRORE: inserire un numero compreso tra 1 e 9 </div> "
											}
											$htmlprint="$htmlprint </div>";
										}
										else{
										$htmlprint="$htmlprint<div class=\"form_attr_disp_input_\"><input type=\"radio\" name=\"disp\"/>disponibile tra <input name=\"day\" type=\"text\" id=\"day_number\"/> giorni </div>"
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
