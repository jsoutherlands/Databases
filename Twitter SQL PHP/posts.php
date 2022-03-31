<?php 

//Se pueden ver los posts de los usuarios seguidos, así como también los reusmeos de dichos usuarios. Infinito.
require_once 'includes/database.inc.php';

$userquery = $_SESSION['user'];

$query = "SELECT * FROM usmitos WHERE usuario IN (SELECT sigue_a FROM seguimientos WHERE seguidor = '$userquery') OR id_usmito IN (SELECT id_usmito FROM reusmeos WHERE usuario IN (SELECT sigue_a FROM seguimientos WHERE seguidor = '$userquery'))ORDER BY fecha_publicacion DESC;";

$sql = mysqli_query($conn, $query);
while ($usmitos = mysqli_fetch_array($sql, MYSQLI_ASSOC)){

	$userid = mysqli_real_escape_string($conn, $usmitos['usuario']);

	$usmitoid = mysqli_real_escape_string($conn, $usmitos['id_usmito']);

	$datosUsuario = mysqli_query($conn, "SELECT * FROM usmers WHERE usuario = '$userid'");
	$usar = mysqli_fetch_array($datosUsuario);


	if (isset($_GET['reusmear'])) {
		$numid = $_GET['idre'];
		if ($_GET['reusmear'] === 'true') {
			mysqli_query($conn, "INSERT INTO reusmeos(usuario, id_usmito) VALUES ('$userquery', '$numid')");
			header('location: index.php');
			exit();
		}elseif ($_GET['reusmear'] === 'false') {
			mysqli_query($conn, "DELETE FROM reusmeos WHERE id_usmito = '$numid' AND usuario = '$userquery'");
			header('location: index.php');
			exit();
		}
	}

	if (isset($_GET['meencanta'])) {
		$numid = $_GET['idme'];
		if($_GET['meencanta'] === 'true'){
			mysqli_query($conn, "INSERT INTO me_encanta(usuario, id_usmito) VALUES ('$userquery', '$numid')");
			header('location: index.php');
			exit();
		}elseif ($_GET['meencanta'] === 'false') {
			mysqli_query($conn, "DELETE FROM me_encanta WHERE id_usmito = '$numid' AND usuario = '$userquery'");
			header('location: index.php');
			exit();
		}
	}
	?>

<div class="post-box">
	<br>
	<div class="up-post-box">
		<div class="nombre-box">
			<a class="nombre" href="indexprofile.php?userid=<?php echo $usar['usuario']?>"><?php echo $usar['nombre']; ?></a>
			<a class="usuario" href="indexprofile.php?userid=<?php echo $usar['usuario']?>"><?php echo '@'.$usar['usuario'];?></a>
		</div>
		<div class="fecha-box">
			<a class="fecha" href="indexpost.php?id=<?php echo $usmitoid?>"><?php echo $usmitos['fecha_publicacion'];?></a>
		</div>
	</div>
	<div class="text-post-box">
		<div>
			<p><?php echo $usmitos['mensaje'];?></p>
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
		<a class="responder" href="indexpost.php?id=<?php echo $usmitoid?>">
			<div class="respuesta-box">
				<i class="fas fa-reply"></i>
				<span>Responder</span>
			</div>
		</a>
			<div class="reusmeo-box">
				<?php
				$reuquery = "SELECT * FROM reusmeos WHERE id_usmito = '$usmitoid' AND usuario = '$userquery'";
				$resql = mysqli_query($conn, $reuquery);
				$numre = mysqli_num_rows($resql);

				if ($numre > 0) {?>
					<a href="index.php?reusmear=false&idre=<?php echo $usmitoid?>">
						<span style="color: #008452;"><?php echo $usmitos['cantidad_reusmeos']?></span>
						<i style="color: #008452;" class="fas fa-retweet"></i>
						<span style="color: #008452;">Desreusmear</span>
					</a>
				<?php
				}elseif ($numre === 0) {
					?>
					<a href="index.php?reusmear=true&idre=<?php echo $usmitoid?>">
						<span><?php echo $usmitos['cantidad_reusmeos']?></span>
						<i class="fas fa-retweet"></i>
						<span>Reusmear</span>
					</a>
				<?php 
				}
				?>
			</div>
		<div class="meencanta-box">
			<?php 
			$encquery = "SELECT * FROM me_encanta WHERE id_usmito = '$usmitoid' AND usuario = '$userquery'";
			$mesql = mysqli_query($conn, $encquery);
			$num = mysqli_num_rows($mesql);

			if ($num > 0) {?>
				<a href="index.php?meencanta=false&idme=<?php echo $usmitoid?>">
					<span style="color: #D60019;"><?php echo $usmitos['cantidad_meencanta']?></span>
					<i style="color: #D60019;" class='fas fa-heart'></i>
					<span style="color: #D60019;">Ya no me encanta</span>
				</a>
			<?php
			}elseif($num === 0){
				?>
				<a href="index.php?meencanta=true&idme=<?php echo $usmitoid?>">
					<span><?php echo $usmitos['cantidad_meencanta']?></span>
					<i class='fas fa-heart'></i>
					<span>Me encanta</span>
				</a>
			<?php 
			}
			?>
		</div>
	</div>
	<br>
</div>

<?php
}
?>