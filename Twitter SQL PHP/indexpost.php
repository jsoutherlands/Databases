<?php
include_once 'views/header.php';
include_once 'sidebar.php';
//Muestra el usmito de un usuario. No está totalmente funcional ya que debería mostrar abajo las respuestas, pero estas no están creadas.
?>

<?php 

require_once 'includes/database.inc.php';

$usmitoget = $_GET['id'];

$query = "SELECT * FROM usmitos WHERE id_usmito = '$usmitoget'";

$sql = mysqli_query($conn, $query);

$sqlarr = mysqli_fetch_array($sql, MYSQLI_ASSOC);

$userid = mysqli_real_escape_string($conn, $sqlarr['usuario']);

$usmitoid = mysqli_real_escape_string($conn, $sqlarr['id_usmito']);

$datosUsuario = mysqli_query($conn, "SELECT * FROM usmers WHERE usuario = '$userid'");
$usar = mysqli_fetch_array($datosUsuario);

?>

<div class="post-box">
	<br>
	<div class="up-post-box">
		<div class="nombre-box">
			<a class="nombre" href="profile.php?usuario=<?php echo $usar['usuario']?>"><?php echo $usar['nombre']; ?></a>
			<a class="usuario" href="profile.php?usuario=<?php echo $usar['usuario']?>"><?php echo '@'.$usar['usuario'];?></a>
		</div>
		<div class="fecha-box">
			<a class="fecha" href="post.php?id=<?php echo $usmitoid?>"><?php echo $sqlarr['fecha_publicacion'];?></a>
		</div>
	</div>
	<div class="text-post-box">
		<div>
			<p><?php echo $sqlarr['mensaje'];?></p>
		</div>
		<div>

			<?php

			$qtag = "SELECT * FROM tags WHERE id_usmito = $usmitoid";
			$qsql = mysqli_query($conn, $qtag);

			while ($tags = mysqli_fetch_array($qsql, MYSQLI_ASSOC)) {
			?>
			<a href="tag.php?id=<?php echo $tags['id_tag']?>"><?php echo "#".$tags['tag']?></a>

			<?php 
			}
			?>
		</div>
	</div>
	<div class="options-post-box">
		<div class="respuesta-box">
			<i class="fas fa-reply"></i>
			<span>Responder</span>
		</div>
		<div class="reusmeo-box">
			<i class="fas fa-retweet"></i>
			<span>Reusmear</span>
		</div>
		<div class="meencanta-box">
			<i class="fas fa-heart"></i>
			<span>Me encanta</span>
		</div>
	</div>
	<br>
</div>


<?php 
include_once 'views/footer.php';
?>