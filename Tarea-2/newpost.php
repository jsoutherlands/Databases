<div class="post-form">
	<h2>Usmear</h2>
	<section>
		<form action="includes/newpost.inc.php" method="post">
			<textarea name="usmito" placeholder="¿En qué estás pensando?"></textarea>
			<div>
				<input type="text" name="tags" placeholder="Ingresa tags relacionados. ¡Recuerda separar por comas!">
				<select name="privacidad">
					<option value="Público">Público</option>
					<option value="Amigos Cercanos">Amigos Cercanos</option>
				</select>
				<button type="submit" name="submit">Publicar</button>
			</div>
		</form>
	</section>
</div>