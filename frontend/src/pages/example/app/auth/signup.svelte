<script>
    import {user, sendForm} from "../_api.js";
    import {goto, url} from "@sveltech/routify";
    import {getContext} from 'svelte';
    import Input from '../_components/Input.svelte'

    let apiUrl = getContext('apiUrl');
    let form;
    let email;
    let password;
    let password2;
    let errorMessage = null;
    $: showError = !!errorMessage;

    function validateForm() {
        if (!email.input.checkValidity() || email.value === "") {
            errorMessage = "Пожалуйста, укажите почту";
            return false;
        }
        if (password.value === "") {
            errorMessage = "Пожалуйста, укажите пароль";
            return false;
        }
        if (password2.value === ""){
            errorMessage = "Пожалуйста, повторите пароль";
            return false;
        }
        if (password.value !== password2.value){
            errorMessage = "Пароли не совпадают";
            return false;
        }
        return true;
    }

    async function submit() {
        if (!validateForm()) return;
        showError = false;
        console.log(false)
        let error = await sendForm(false, email.value, password.value);
        if (error){
            errorMessage = error;
            return;
        }
        $goto($url('../../'));
    }
</script>


<main>
<div>
    <h1>Регистрация</h1>
    <form bind:this={form}>
        <label class:showError>{errorMessage}</label>
        <Input class="neomorphic-input" bind:this={email} placeholder="Электронная почта" name="username" type="email"/>
        <Input class="neomorphic-input" bind:this={password} placeholder="Пароль" name="password" type="password"/>
        <Input class="neomorphic-input" bind:this={password2} placeholder="Подтверждение пароля" name="password" type="password"/>
        <button type="button" on:click={submit}>Зарегистрироваться</button>
    </form>
    <p>Уже зарегистрированы? <a href='./signin'>Войдите</a></p>
</div>
</main>
<style>
    main {
        /*position: absolute;*/
        width: 100%;
        height: 100%;
        display: grid;
        place-items: center;
        background: #0bf5cc;
    }

    div {
        width: 400px;
        height: 500px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border-radius: 29px;
        background: #DBEBFB;
        box-shadow: 22px 22px 44px #7b848d,
                   -22px -22px 44px #ffffff;
    }

    .showError {
        opacity: 1;
    }

    form {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;
        height: 300px;
        width: 300px;
    }

    label {
        width: 250px;
        margin: 10px auto;
        padding: 5px;
        opacity: 0;
        transition: 0.5s ease;
        color: white;
        background: #E16684;
        border-radius: 20px;
        box-shadow: 0 0 15px #D7335C;
        text-align: center;
    }

    button {
        margin: 20px;
        padding: 10px 30px;
        border: none;
        color: #0A335C;
        border-radius: 29px;
        background: linear-gradient(145deg, #eafbff, #c5d4e2);
        box-shadow: 6px 6px 12px #7b848d,
                   -6px -6px 12px #ffffff;
    }

    :global(.neomorphic-input) {
        border-radius: 7px;
        border-bottom-color: transparent;
        background: #DBEBFB;
        box-shadow: inset 3px 3px 10px #7b848d,
                    inset -3px -3px 10px #ffffff;
    }
</style>
