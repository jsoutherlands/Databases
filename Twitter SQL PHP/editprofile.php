<?php
include_once 'views/header.php';
//Formulario para editar perfil con método post.
?>

<?php 
include_once 'sidebar.php';
?>


<?php 
$infouser = $_SESSION['user'];
if(isset($_GET['deleteaccount'])){
	if($_GET['deleteaccount'] == 'true'){
		mysqli_query($conn, "DELETE FROM usmers WHERE usuario = '$infouser'");
		header('location: includes/logout.inc.php?exito=true');
		exit();	
	}
}

?>
<div class="elimina-box">
	<a href="editprofile.php?deleteaccount=true">Eliminar mi cuenta</a>
</div>

<div class="edita-descripcion">
	<h3>Editar perfil</h3>
	<form action="includes/editprofile.inc.php" method="post">
		<input type="text" name="nombre" placeholder="Cambiar nombre...">
		<textarea name="descripcion" maxlength="279" placeholder="Modificar descripción..."></textarea>
		<input type="text" name="web" placeholder="Sitio web...">
		<button type="submit" name="submit">Modificar</button>
	</form>
</div>

<?php
include_once 'views/footer.php';
?>