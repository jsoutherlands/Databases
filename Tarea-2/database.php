<?php 
$server = 'localhost';
$username = 'root';
$pwd = '';
$database = 'tarea2';

try{
	$conn = new PDO("mysql:host=$server;dbname=$database;", $username, $pwd);
}catch{
	die("Conexión fallida: " $err->getMessage());
}


?>