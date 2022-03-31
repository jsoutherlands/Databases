<?php
if (isset($_POST['submit'])) {
	require_once 'database.inc.php';
	require_once 'functions.inc.php';
	session_start();
	$nombre = $_POST['nombre'];
	$desc = $_POST['descripcion'];
	$web = $_POST['web'];
	//Vemos cuál de los campos serán modificados
	if ($nombre !== "") {
		modificarNombre($conn, $nombre, $_SESSION['user']);
	}
	if ($desc !== "") {
		insertarDescripcion($conn, $desc, $_SESSION['user']);
	}
	if ($web !==""){
		modificarWeb($conn, $web, $_SESSION['user']);
	}
	header("location: ../editprofile.php?error=none");
	exit();
}
?>