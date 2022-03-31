<!-- Sidebar del feed -->
<div class="ancho-sidebar">
	<nav class="sidebar">
		<div class="sidebar-item">
			<a href="mylists.php">Mis listas</a>
		</div>
		<div class="sidebar-item">
			<a href="tags.php">Mis tags</a>
		</div>
	</nav>
	<nav class="trending">
		<h2>Tendencias</h2>
		<?php
		//Permite ver los trendings gracias a la vista TRENDING
		require_once 'includes/database.inc.php';
		$querytrend = "SELECT * FROM TRENDING";
		$sqltrend = mysqli_query($conn, $querytrend);
		$i = 0;
		while(($ttags = mysqli_fetch_array($sqltrend, MYSQLI_ASSOC)) && $i<10){
			?>
			<div class="trend">
				<span><?php echo $i+1?>.</span>
				<a href="tags.php?tag=<?php echo $ttags['tag']?>"><?php echo $ttags['tag']?></a>
			</div>
		<?php
		$i++;
		}
		?>
	</nav>
</div>