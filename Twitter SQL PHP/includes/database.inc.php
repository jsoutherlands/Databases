<?php 

/*
Conexión a la Base de Datos.
*/
$server = 'localhost';
$username = 'root';
$pwd = '';
$db = 'tarea2';

$conn = mysqli_connect($server, $username, $pwd, $db);

if(!$conn){
	die("Conexión fallida: " . mysqli_connect_error());
}

?>