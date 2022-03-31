<?php
include_once 'views/header.php';
//Página principal, se convierte en feed una vez iniciada la sesión.
?>

<?php 
if (isset($_SESSION['name'])) {
	include_once 'sidebar.php';
	include_once 'newpost.php';
	include_once 'posts.php';
}
else{
	echo "<h1>Entérate de lo que pasa</h1>";
	echo "<h3>Ingresa ahora a Usmwer.</h3>";
	if(isset($_GET['exito'])){
		if ($_GET['exito'] === 'true') {
			echo "<p> Cuenta eliminada con éxito.</p>";
		}
	}
}
?>

<?php 
include_once 'views/footer.php';
?>