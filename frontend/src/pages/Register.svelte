<script>	
	let src = "logo.svg"
</script>

<main>
	<img {src} class="logo-img" alt="logo">

	<div class = "registration">
		<div class="text-div"><h1 class="text">РЕГИСТРАЦИЯ:</h1></div>
		<div class="social-form">
			Через соцсети:<br>
			<div class="social-btns"><a href="/">facebook</a><br>
			<a href="/">twitter</a><br>
			<a href="/">vkontakte</a>
			</div>
		</div>
		<div class="reg-form">
			<form>
				<div class="checkbox-class">
					Я хочу... <br>
					<label class="checkbox-transform">
						<input type=checkbox value="Получать данные"><span class="pseudocheckbox">Получать данные</span>
					</label>
					<label>
						<input type=checkbox value="Делиться данными">
						<span class="pseudocheckbox">Делиться данными</span>
					</label>
				</div>
				<div class="input-class">
					<input type="text" placeholder="Имя пользователя" id="input-form">
					<input type="email" placeholder="E-mail" id="input-form">
					<input type="password" placeholder="Пароль" id="input-form">
				</div>
				<div class="radio-2">
					<label class="radio-class"><input type="radio">Я принимаю <a href="/">пользовательское соглашение</a></label>
				</div>
				<div class="btn-class">
					<button>Далее</button>
					<button class="enter-btn">Войти</button>
				</div>
			</form>
			</div>
	</div>

</main>

<style>

	.text-div {
		padding-right: 15%;
		font-family: Helvetica Neue;
	}

	div {
		display: inline-block;
	}

	.enter-btn {
		background-color: #F9F9F9;
		color: #1355FF;
	}

	.reg-form {
		margin-top: 5%;
		display: inline-block;
		vertical-align: top;
		width: 40%;
	}

	.social-btns {
		margin-top: 10%;
	}

	.social-form {
		margin-top: 5%;
		font-family: Helvetica Norm;
		font-size: 20px;
		vertical-align: top;
		padding-right: 5%;
	}

	#input-form {
		margin-bottom: 5%;
		font-size:20px;
		display:block;
		border:none;
		width: 444px;
		border-bottom:1px solid #282828;
		background-color: #F9F9F9;
	}

	.input-class {
		margin-top: 5%;
	}

	.radio-class {
		font-size: 14px;
	}

	.btn-class {
		width: 400px;
		margin-bottom: 2%;
		margin-left: 1%;
		display: flex;
	}

	.radio-2 {
		width: 400px;
		margin-bottom: 2%;
		margin-left: 1%;
	}

	button {
		margin-left: 1%;
	}

	.checkbox-class {
		margin-left: 1%;
		font-size: 20px;
		width: 432px;
		font-family: Helvetica Norm;
	}

	.social-form a {
		color: #545454;
		font-family: Helvetica Norm;
		text-decoration: none;
		font-size: 20px;
	}
	
	.social-form a:hover {
		color: #1355FF;
	}

</style>