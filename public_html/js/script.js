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
    var mess=document.getElementById(inp.id+"_check")
    if (inp.value == '')
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

function validateForm(form){
    var valid=true;
    var el=form.elements;
    for (var i=0; i<el.length && valid===true; i++) {
        if (el[i].value===''){
            valid=false;
            window.alert("Devi riempire tutti i campi!");
        }
    }
    return valid; 
}