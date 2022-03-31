<?php

/*
Se usa para cerrar la sesión dentro de PHP.
*/
session_start();
session_unset();
session_destroy();
header("location: ../index.php");
exit();
?>