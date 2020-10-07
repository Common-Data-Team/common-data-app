<script>
    import {user, sendForm} from "../_api.js";
    import {goto, url} from "@sveltech/routify";
    import {getContext} from 'svelte';
    import Input from '../_components/Input.svelte'
    import Checkbox from '../_components/Checkbox.svelte'

    let socialNetworks = {facebook: 'https://facebook.com', twitter: 'https://twitter.com', vkontakte: 'https://vk.com'};
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

<div class="component">
    <h1>РЕГИСТРАЦИЯ:</h1>
    <div class="right-block">
        <div class="social-networks">
            <p>Через соцсети </p>
            <ul>
            {#each Object.entries(socialNetworks) as [sn, url]}
                <li><a href={url}>{sn}</a></li>
            {/each}
            </ul>
        </div>
        <form bind:this={form}>
    <!--        <label class:showError>{errorMessage}</label>-->
                <label class="label">Я хочу...</label>
                <div class="checkboxes-block">
                    <Checkbox id=0 text="Делиться данными"/>
                    <Checkbox id=1 text="Получать данные"/>
                </div>
                <Input class="neomorphic-input" bind:this={email} placeholder="Электронная почта" name="username" type="email"/>
                <Input class="neomorphic-input" bind:this={password} placeholder="Пароль" name="password" type="password"/>
                <Input class="neomorphic-input" bind:this={password2} placeholder="Подтверждение пароля" name="password" type="password"/>

            <div class="button-block">
                <button type="button" on:click={submit}>Зарегистрироваться</button>
                <p>Уже зарегистрированы? <a href='./signin'>Войдите</a></p>
            </div>
        </form>
    </div>
</div>

<style>
    h1 {
        padding: 0;
        margin: 0;
    }
    .component {
        height: 80%;
        width: 100%;
        margin-top: 30px;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
    .checkboxes-block {
        display: flex;
        flex-direction: row;
    }
    .right-block {
        display: flex;
        flex-direction: row;
        justify-content: flex-end;
    }

    .social-networks {
        margin-right: 65px;
    }
    form {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 500px;
        width: 400px;
        margin-right: 100px;
    }
</style>
