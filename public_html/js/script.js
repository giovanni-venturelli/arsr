function checkEmail(){
	var email=document.getElementById("email");
    var mess=document.getElementById("email_check")
    var regex = /([a-zA-Z0-9]+)(@[a-z]+).(it|com|net|org)/;
    if (email.value == '' || !regex.test(email.value))
    {
        email.style.borderColor = "red";
        mess.style.display="inline-block";

    }
    else
    {
     email.style.borderColor = "#2CDC2C";
     mess.style.display="none";
 }
}

function checkNotEmpty(inp){
    var mess=document.getElementById(inp.id+"_check");
    var val = false;
    if (inp.value == '' && inp.id!="cognome")
    {
        inp.style.borderColor = "red";
        mess.style.display="inline-block";
        val=false;

    }
    else if (inp.value == '' && inp.id==="cognome" && !document.getElementById("seleziona_partita_iva").checked)
    {
        inp.style.borderColor = "red";
        mess.style.display="inline-block";
        val=false;

    }
    else
    {
     inp.style.borderColor = "#2CDC2C";
     mess.style.display="none";
     val = true;

 }
 return val;
}

function validateForm(form){
    var valid=true;
    var el=form.elements;
    for (var i=0; i<el.length; i++) {
        var temp=true;
        if(el[i].nodeName!="FIELDSET" && el[i].type!="submit" && el[i].type!="radio" && el[i].type!="reset"){
        temp=checkNotEmpty(el[i]);
        if(temp===false){
            valid=false;
        }
    }
    }
    return valid; 
}

function validateAttrForm(form){
    var valid=true;
    var el=form.elements;
    if(document.getElementById('disp_tra_input').checked && document.getElementById('day_number').value===""){
        valid=false;
        window.alert("Devi riempire nome, prezzo, descrizione dell'immagine e prossima disponibilita' dell'attrezzatura!");
    }
    else{
        for (var i=0; i<el.length && valid===true; i++) {
            if (el[i].value==='' && el[i].id!="form_attr_descr_input"){
                if(el[i].id!="day_number"){
                    valid=false;
                    window.alert("Devi riempire nome, prezzo e descrizione dell'immagine!");
                }
            }
        }
    }
    return valid; 
}

function checkNumber(inp){
    var regex = /^[0-9]{1,4}$/;
    var mess = document.getElementById(inp.id+"_check")
    if (!regex.test(inp.value) )
    {
        inp.style.borderColor = "red";
        mess.style.display="inline-block";

    }
    else
    {
     inp.style.borderColor = "#2CDC2C";
     mess.style.display="none";

 }
}

function checkDayNumber(inp){
    var regex = /^[0-9]$/;
    var mess = document.getElementById(inp.id+"_check");
    var valid=true;
    if (document.getElementById('disp_input').checked && !regex.test(inp.value) )
    {
        inp.style.borderColor = "red";
        mess.style.display="inline-block";
        valid=false;
    }
    else
    {
     inp.style.borderColor = "#2CDC2C";
     mess.style.display="none";
     valid=true;
 }
 return valid;
}

function handleCognome(){
    var dis = document.getElementById("cognome");
    var par = document.getElementById("seleziona_partita_iva");
    var cod = document.getElementById("seleziona_codice");
    if(par.checked){
        dis.setAttribute("disabled", "disabled");
        checkNotEmpty(dis);
    }
    else{
        dis.removeAttribute("disabled");
        checkNotEmpty(dis);
    }
}