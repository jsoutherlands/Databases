<?php
include_once 'views/header.php';
?>

<?php 
if (isset($_SESSION['name'])) {
	include_once 'sidebar.php';
	include_once 'newpost.php';
}
else{
	echo "<h1>Entérate de lo que pasa</h1>";
	echo "<h3>Ingresa ahora a Usmwer.</h3>";
}
?>

<?php 
include_once 'views/footer.php';
?>