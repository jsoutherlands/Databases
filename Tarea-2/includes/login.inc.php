<?php 

if (isset($_POST['submit'])) {
	$user = $_POST['username'];
	$pwdd = $_POST['password'];

	require_once 'database.inc.php';
	require_once 'functions.inc.php';

	if(emptyInputLogin($user, $pwdd) !== false){
		header("location: ../login.php?error=emptyinput");
		exit();
	}

	loginUser($conn, $user, $pwdd);
}else{
	header("location: ../login.php");
	exit();
}

?>