<div class="post-form">
	<section>
		<h3>Escribir una respuesta</h3>
		<form action="includes/reply.inc.php" method="post">
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
<!-- Plantilla para respuestas. No se ocupó. -->