<?php

/*
Se encarga de publicar el Usmito, junto con sus tags (si es que hay)
*/

if(isset($_POST['submit'])){
	session_start();
	$usmito = $_POST['usmito'];
	$tags = $_POST['tag-container'];
	$priv = $_POST['privacidad'];

	require_once 'database.inc.php';
	require_once 'functions.inc.php';

	if(emptyUsmito($usmito)){
		header('location: ../index.php?error=emptyinput');
		exit();
	}
	
	$postId = postUsmito($conn, $_SESSION['user'], $usmito, $priv);
	if(!emptyTags($tags)){
		pushTags($conn, $tags, $postId);
	}else{
		header('location: ../index.php?error=notags');
		exit();
	}
}

?>