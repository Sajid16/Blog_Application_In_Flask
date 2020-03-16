function display(){
    alert("its working");
}

function match_pass() {
  if (document.getElementById('password').value ==
    document.getElementById('repassword').value) {
    document.getElementById('check_pass').style.color = 'green';
    document.getElementById('check_pass').innerHTML = 'Password matched';
  }
  else {
    document.getElementById('check_pass').style.color = 'red';
    document.getElementById('check_pass').innerHTML = 'Password not matched';
  }
}