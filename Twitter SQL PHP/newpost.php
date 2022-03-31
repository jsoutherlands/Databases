<div class="post-form">
	<h2>Usmear</h2>
	<section>
		<form action="includes/newpost.inc.php" method="post">
			<textarea name="usmito" maxlength="279" placeholder="¿En qué estás pensando?"></textarea>
			<div>
				<span>Ingresa tus tags a continuación:</span>
			</div>
			<div class="tag-container" data-name="tag-container">
			</div>
			<script src="js/tags.js"></script>
			<div>
				<select name="privacidad">
					<option value="Público">Público</option>
					<option value="Amigos Cercanos">Amigos Cercanos</option>
				</select>
				<button type="submit" name="submit" >Publicar</button>
			</div>
		</form>
	</section>
</div>
<!-- Plantilla de nueva publicación -->