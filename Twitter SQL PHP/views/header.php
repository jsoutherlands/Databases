<?php 
session_start();
?>

<!DOCTYPE html>
<!-- Contiene lo necesario para la página de index y los archivos css y js -->
<html>
<head>
	<meta charset="utf-8">
	<title>Usmwer</title>
	<link rel="stylesheet" type="text/css" href="css/styles.css">
	<script src="https://kit.fontawesome.com/d2501af021.js" crossorigin="anonymous"></script>
</head>
<body>
	<header>
		<div class="ancho">		
			<div class="logo">
				<a href="index.php"><img src="img/usmwer.png"></a>
			</div>
			<nav class="nav-header">
				<ul>
					<?php 
					if (isset($_SESSION['user'])) {
						$data=$_SESSION['user'];
						echo "<li><input type='search' name='search' placeholder='Buscar'>";
						echo "<li><a href='indexprofile.php?userid=".$data."'>".$_SESSION['name']."</a></li>";
						echo "<li><a href='includes/logout.inc.php'>Cerrar Sesión</a></li>";
					}else{
						echo "<li><a href='signup.php'>Regístrate</a></li>";
						echo "<li><a href='login.php'>Iniciar Sesión</a></li>";
					}
					?>
				</ul>
			</nav>
		</div>
	</header>
<div class="weas">