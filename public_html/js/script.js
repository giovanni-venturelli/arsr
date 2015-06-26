function checkEmail(){
	var email=document.getElementById("email");
var regex = /([a-zA-Z0-9]+)(@[a-z]+).(it|com|net|org)/;
if (email.value == '' || !regex.test(email.value))
{
    email.style.borderColor = "red";

}
else
{
	email.style.borderColor = "#2CDC2C";
}
}

function checkNotEmpty(id){
	var inp=document.getElementById(id);
if (inp.value == '')
{
    inp.style.borderColor = "red";
}
else
{
	inp.style.borderColor = "#2CDC2C";
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