<?php
include_once 'views/header.php';
//Inicio de sesión mediante método post.
?>

<section class="login-form">
	<h2>Iniciar Sesión</h2>
	<form action="includes/login.inc.php" method="post">
		<input type="text" name="username" placeholder="Nombre de usuario">
		<input type="password" name="password" placeholder="Contraseña">
		<button type="submit" name="submit">Iniciar Sesión</button>
		<p>o <a href="signup.php">Regístrate.</a></p>
	</form>
	<?php 
	if (isset($_GET['error'])) {
		if ($_GET['error'] == "emptyinput") {
			echo "<p class='error'>Ingresa información en todos los campos.</p>";
		} else if ($_GET['error'] == "wronglogin"){
			echo "<p class='error'>Tu usuario o contraseña son incorrectos.</p>";
		}
	}
	?>
</section>

<?php 
include_once 'views/footer.php';
?>