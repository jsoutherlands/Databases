<?php 


//Comprueba que los inputs de registro estén completados.
function emptyInputSignUp($user, $name, $pwd1, $pwd2, $born, $gndr){
	if (empty($user) || empty($name) || empty($pwd1) || empty($pwd2) || empty($born) || empty($gndr)) {
		$res = true;
	}else{
		$res = false;
	}
	return $res;
}

//Ve si las contraseñas de registro coinciden.
function invalidPwd($pwd1, $pwd2){
	if ($pwd1 !== $pwd2) {
		$res = true;
	}else{
		$res = false;
	}
	return $res;
}


//Verifica si el usuario existe.
function userExists($conn, $user){
	$query = "SELECT * FROM usmers WHERE usuario = ?;";
	$sql = mysqli_stmt_init($conn);
	if (!mysqli_stmt_prepare($sql, $query)){
		header("location: ../signup.php?error=queryfailed");
		exit();
	}

	mysqli_stmt_bind_param($sql, "s", $user);
	mysqli_stmt_execute($sql);

	$res = mysqli_stmt_get_result($sql);

	if ($row = mysqli_fetch_assoc($res)){
		return $row;
	}else{
		$res = false;
		return $res;
	}
	mysqli_stmt_close($sql);
}


//Crea el usuario ingresado en el registro.
function createUser($conn, $user, $name, $pwd1, $born, $gndr){
	$query = "INSERT INTO usmers(usuario, contrasena, nombre, fecha_nacimiento, genero) VALUES (?, ?, ?, ?, ?);";
	$sql = mysqli_stmt_init($conn);
	if (!mysqli_stmt_prepare($sql, $query)){
		header("location: ../signup.php?error=queryfailed");
		exit();
	}

	$hashpwd = password_hash($pwd1, PASSWORD_DEFAULT);
	mysqli_stmt_bind_param($sql, "sssss", $user, $hashpwd, $name, $born, $gndr);
	mysqli_stmt_execute($sql);
	mysqli_stmt_close($sql);
	header("location: ../signup.php?error=none");
	exit();
}

//Verifica si el input de login está o no vacío.
function emptyInputLogin($user, $pwd){
	if (empty($user) || empty($pwd)) {
		$res = true;
	}else{
		$res = false;
	}
	return $res;
}

//Realiza el inicio de sesión comprobando la contraseña y el usuario
//con la base de datos.
function loginUser($conn, $user, $pwd){
	$userExists = userExists($conn, $user);
	if ($userExists === false) {
		header("location: ../login.php?error=wronglogin");
		exit();
	}
	$pwdHash = $userExists["contrasena"];
	$checkPwd = password_verify($pwd, $pwdHash);
	if ($checkPwd === false) {
		header("location: ../login.php?error=wronglogin");
		exit();
	}else if($checkPwd === true){
		session_start();
		$_SESSION['user'] = $userExists["usuario"];
		$_SESSION['name'] = $userExists["nombre"];
		header("location: ../index.php");
		exit();
	}
}

//Verifica si el usmito a publicar no es vacío.
function emptyUsmito($usmito){
	if (empty($usmito)){
		$res = true;
	}else{
		$res = false;
	}
	return $res;
}

//Revisa si el input de tags está o no vacío.
function emptyTags($tags){
	if (empty($tags)){
		$res = true;
	}else{
		$res = false;
	}
	return $res;
}

//Publica el Usmito.
function postUsmito($conn, $user, $usmito, $priv){
	$query = "INSERT INTO usmitos(usuario, mensaje, privacidad) VALUES (?, ?, ?);";
	$sql = mysqli_stmt_init($conn);
	
	if(!mysqli_stmt_prepare($sql, $query)){
		header("location: ../index.php?error=queryfailed");
		exit();
	}

	mysqli_stmt_bind_param($sql, "sss", $user, $usmito, $priv);
	mysqli_stmt_execute($sql);
	mysqli_stmt_close($sql);
	$idRow = mysqli_insert_id($conn);
	header("location: ../index.php?error=none");

	//Retorna id del usmito
	return $idRow;
}

//Publica los tags uno por uno (foreach).
function pushTags($conn, $tags, $postId){
	$query = "INSERT INTO tags(tag, id_usmito) VALUES (?, ?);";
	$sql = mysqli_stmt_init($conn);
	if(!mysqli_stmt_prepare($sql, $query)){
		header("location: ../index.php?error=queryfailed");
		exit();
	}

	mysqli_stmt_bind_param($sql, "si", $tag, $postId);

	$explodedTags = explode(',', $tags);
	foreach ($explodedTags as $tag) {
		mysqli_stmt_execute($sql);
	}	
	mysqli_stmt_close($sql);
	header("location: ../index.php?error=none");
	exit();
}

// Ingresa la descripción del usuario que desea modificar su descripción.
function insertarDescripcion($conn, $desc, $user){
	$query = "UPDATE usmers SET descripcion = ? WHERE usuario = ?";
	$sql = mysqli_stmt_init($conn);
	
	if(!mysqli_stmt_prepare($sql, $query)){
		header("location: ../editprofile.php?error=queryfailed");
		exit();
	}

	mysqli_stmt_bind_param($sql, "ss", $desc, $user);
	mysqli_stmt_execute($sql);
	mysqli_stmt_close($sql);
}

// Ingresa el nuevo nombre del usuario.
function modificarNombre($conn, $nombre, $user){
	$query = "UPDATE usmers SET nombre = ? WHERE usuario = ?";
	$sql = mysqli_stmt_init($conn);
	
	if(!mysqli_stmt_prepare($sql, $query)){
		header("location: ../editprofile.php?error=queryfailed");
		exit();
	}

	mysqli_stmt_bind_param($sql, "ss", $nombre, $user);
	mysqli_stmt_execute($sql);
	mysqli_stmt_close($sql);

}

// Modifica sitio web del usuario
function modificarWeb($conn, $web, $user){
	$query = "UPDATE usmers SET sitio_web = ? WHERE usuario = ?";
	$sql = mysqli_stmt_init($conn);
	
	if(!mysqli_stmt_prepare($sql, $query)){
		header("location: ../editprofile.php?error=queryfailed");
		exit();
	}

	mysqli_stmt_bind_param($sql, "ss", $web, $user);
	mysqli_stmt_execute($sql);
	mysqli_stmt_close($sql);
}

?>