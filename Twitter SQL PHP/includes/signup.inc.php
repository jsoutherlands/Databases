<?php 

/*
Se registra al usuario.
*/

if (isset($_POST['submit'])){
	$user = $_POST['username'];
	$name = $_POST['name'];
	$pwd1 = $_POST['pwd1'];
	$pwd2 = $_POST['pwd2'];
	$born = $_POST['born'];
	$gndr = $_POST['gender'];

	require_once 'database.inc.php';
	require_once 'functions.inc.php';

	if(emptyInputSignUp($user, $name, $pwd1, $pwd2, $born, $gndr) !== false){
		header("location: ../signup.php?error=emptyinput");
		exit();
	}
	if(invalidPwd($pwd1, $pwd2) !== false){
		header("location: ../signup.php?error=pwdsdontmatch");
		exit();
	}
	if (userExists($conn, $user) !== false){
		header("location: ../signup.php?error=usertaken");
		exit();
	}

	createUser($conn, $user, $name, $pwd1, $born, $gndr);

}else{
	header("location: ../signup.php");
	exit();
}

?>