<?php 

function emptyInputSignUp($user, $name, $pwd1, $pwd2, $born, $gndr){
	if (empty($user) || empty($name) || empty($pwd1) || empty($pwd2) || empty($born) || empty($gndr)) {
		$res = true;
	}else{
		$res = false;
	}

	return $res;
}

function invalidPwd($pwd1, $pwd2){
	if ($pwd1 !== $pwd2) {
		$res = true;
	}else{
		$res = false;
	}
	return $res;
}

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

function emptyInputLogin($user, $pwd){
	if (empty($user) || empty($pwd)) {
		$res = true;
	}else{
		$res = false;
	}
	return $res;
}

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

?>