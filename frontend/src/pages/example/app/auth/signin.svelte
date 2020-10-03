<script>
    import {goto, url} from "@sveltech/routify";
    import {getContext} from 'svelte';
    import Input from '../_components/Input.svelte'
    import {user, sendForm} from "../_api"

    let apiUrl = getContext('apiUrl');
    let form;
    let email;
    let password;
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
        return true;
    }

    async function submit(){
        if (!validateForm()) return;
        showError = false;
        let error = await sendForm(true, email.value, password.value);
        if (error){
            errorMessage = error;
            return;
        }
        $goto($url("../../"));
    }

</script>

<main>
<div>
    <h1>Вход</h1>
    <form bind:this={form}>
        <label class:showError>{errorMessage}</label>
        <Input class="neomorphic-input" bind:this={email} placeholder="Электронная почта" name="email" type="email"/>
        <Input class="neomorphic-input" bind:this={password} placeholder="Пароль" name="password" type="password"/>
        <button type="button" on:click={submit}>Войти</button>
    </form>
    <p>Нет аккаунта? <a href="./signup">Зарегистрируйтесь</a>
    </p>
</div>
</main>
<style>
    main {
        position: absolute;
        display: grid;
        height: 100%;
        width: 100%;
        place-items: center;
    }
    div {
        width: 400px;
        height: 460px;
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
        height: 290px;
        width: 300px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;
    }

    label {
        width: 250px;
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
