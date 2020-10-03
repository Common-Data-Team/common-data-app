<script>
    import {user, sendForm} from "../_api.js";
    import {goto, url} from "@sveltech/routify";
    import {getContext} from 'svelte';
    import Input from '../_components/Input.svelte'

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
    <h1>Регистрация</h1>
    <div class="social-networks">
        <ul>
        {#each Object.entries(socialNetworks) as [sn, url]}
            <li><a href={url}>{sn}</a></li>
        {/each}
        </ul>
    </div>
    <form bind:this={form}>
        <label class:showError>{errorMessage}</label>

<!--        <Input class="neomorphic-input" bind:this={email} placeholder="Электронная почта" name="username" type="email"/>-->
<!--        <Input class="neomorphic-input" bind:this={password} placeholder="Пароль" name="password" type="password"/>-->
<!--        <Input class="neomorphic-input" bind:this={password2} placeholder="Подтверждение пароля" name="password" type="password"/>-->
        <button type="button" on:click={submit}>Зарегистрироваться</button>
    </form>
    <p>Уже зарегистрированы? <a href='./signin'>Войдите</a></p>
</div>

<style>
    .component {
        width: 100%;
        flex-direction: row;
        justify-items: flex-start;
    }

</style>
