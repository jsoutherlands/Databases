<?php
//Conexion con la BD para conocer los datos del usuario
$actual = $_SESSION['user'];
$usuarioget = $_GET['userid'];
$query = "SELECT * FROM usmers WHERE usuario = '$usuarioget'";
$resss = mysqli_query($conn, $query);
$datauser = mysqli_fetch_array($resss, MYSQLI_ASSOC);
?>

<div class="profile-box">
	<div class="up-profile-box">
		<div class="up-info-box">
			<h1><?php echo $datauser['nombre']?></h1>
			<span>@<?php echo $datauser['usuario']?></span>
		</div>
		<div class="up-button-box">
			
				<?php
				//Configuramos las opciones de seguimiento del perfil con respecto al usuario en sesión
				$infoseguimiento = mysqli_query($conn, "SELECT * FROM seguimientos WHERE sigue_a = '$usuarioget' AND seguidor = '$actual'");
				$numerar = mysqli_num_rows($infoseguimiento);
				if (isset($_GET['seguir'])) {
					if ($_GET['seguir'] === 'true') {
						mysqli_query($conn, "INSERT INTO seguimientos(sigue_a, seguidor) VALUES ('$usuarioget', '$actual')");
						header('location: indexprofile.php?userid='.$datauser['usuario']);
						exit();
					}elseif ($_GET['seguir'] === 'false') {
						mysqli_query($conn, "DELETE FROM seguimientos WHERE sigue_a = '$usuarioget' AND seguidor = '$actual'");
						header('location: indexprofile.php?userid='.$datauser['usuario']);
						exit();
					}
				}

				if($_GET['userid'] === $_SESSION['user']){?>
					<a style="color: white; background-color: #004B85 "href="editprofile.php?acc=<?php echo $actual?>">
						Editar perfil
					</a>
					<?php
				}else{
					if ($numerar > 0) {?>
						<a style="color: white; background-color: #D60019;" href="indexprofile.php?seguir=false&userid=<?php echo $datauser['usuario']?>">
						Dejar de Seguir
						</a>
					<?php
					}else{?>
						<a style="color: white; background-color: #008452;" href="indexprofile.php?seguir=true&userid=<?php echo $datauser['usuario']?>">
						Seguir
						</a>
					<?php 
					}
				}
				?>
			</button>
		</div>
	</div>
		<div class="descweb">
			<?php
			if($datauser['descripcion']!==NULL){?>
				<h3>Biografía</h3>
				<p><?php echo $datauser['descripcion']?></p>
			<?php
			}
			if($datauser['sitio_web']!==NULL){?>
				<span>Sitio Web: <a href="<?php echo $datauser['sitio_web']?>"><?php echo $datauser['sitio_web']?></a></span>
			<?php
			}
			?>
			<div class="fechas">
				<p>Fecha de Nacimiento: <?php echo $datauser['fecha_nacimiento']?></p>
				<p>Fecha de Creación: <?php echo $datauser['fecha_creacion']?></p>
			</div>
			<div class="numerosbox">
				<div class="usmitos">
					<span><?php echo $datauser['cantidad_usmitos']?> usmitos</span>
				</div>
				<div class="siguea">
					<span><?php echo $datauser['cantidad_seguidos']?> seguidos</span>
				</div>
				<div class="seguidores">
					<span><?php echo $datauser['cantidad_seguidores']?> seguidores</span>
				</div>
			</div>
		</div>
		
	</div>
</div>
