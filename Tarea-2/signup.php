<?php
include_once 'views/header.php';
?>

<section class="signup-form">
	<h2>Regístrate</h2>
	<form action="includes/signup.inc.php" method="post">
		<input type="text" name="username" placeholder="Nombre de usuario">
		<input type="text" name="name" placeholder="Nombre">
		<input type="password" name="pwd1" placeholder="Contraseña">
		<input type="password" name="pwd2" placeholder="Confirma tu contraseña">
		<div>
			<label>Fecha de nacimiento</label>
		</div>
		<input type="date" name="born">
		<div>
			<label>Género</label>
		</div>
		<select name="gender">
			<option value="Masculino">Masculino</option>
			<option value="Femenino">Femenino</option>
			<option value="Otros">Otros</option>
		</select>
		<button type="submit" name="submit">Registrarse</button>
	</form>
	<?php 
	if (isset($_GET['error'])) {
		if ($_GET['error'] == "emptyinput") {
			echo "<p class='error'>Todos los campos son obligatorios.</p>";
		} else if ($_GET['error'] == "pwdsdontmatch"){
			echo "<p class='error'>Las contraseñas no coinciden.</p>";
		} else if ($_GET['error'] == "usertaken"){
			echo "<p class='error'>Escoge otro nombre de usuario.</p>";
		} else if ($_GET['error'] == "queryfailed"){
			echo "<p class='error'>Ha ocurrido un error inesperado.</p>";
		} else if (($_GET['error'] == "none")) {
			echo "<p>¡Felicidades! Bienvenido/a a Usmwer</p>";
		}
	}
	?>
</section>



<?php 
include_once 'views/footer.php';
?>