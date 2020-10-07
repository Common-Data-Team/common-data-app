<script>
    import {user, sendForm} from "../_api.js";
    import {goto, url} from "@sveltech/routify";
    import {getContext} from 'svelte';
    import Input from '../_components/Input.svelte'
    import Checkbox from '../_components/Checkbox.svelte'
    import RoundedCheckbox from '../_components/RoundedCheckbox.svelte'

    let socialNetworks = {
        facebook: 'https://facebook.com',
        twitter: 'https://twitter.com',
        vkontakte: 'https://vk.com'
    };
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
        if (password2.value === "") {
            errorMessage = "Пожалуйста, повторите пароль";
            return false;
        }
        if (password.value !== password2.value) {
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
        if (error) {
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
            <p>Через соцсети:</p>
            <ul>
                {#each Object.entries(socialNetworks) as [sn, url]}
                    <li><a class="social-link" href={url}>{sn}</a></li>
                {/each}
            </ul>
        </div>
        <form bind:this={form}>
            <!--        <label class:showError>{errorMessage}</label>-->
            <div>
                <label class="label">Я хочу...</label>
                <div class="checkboxes-block">
                    <Checkbox id=0 text="Делиться данными"/>
                    <Checkbox id=1 text="Получать данные"/>
                </div>
            </div>
            <div class="inputs-block">
                <Input bind:this={email} span="E-mail" name="username" type="email"/>
                <Input bind:this={password} span="Пароль" name="password" type="password"/>
                <Input bind:this={password2} span="Подтверждение пароля" name="password" type="password"/>
            </div>
            <RoundedCheckbox id=3 text="Я принимаю <a
            style='text-decoration: underline;
            font-size: min(calc(var(--plain-font-size) - 2px), 20px);'>
            пользовательское соглашение</a>"/>
            <div class="button-block">
                <button type="button" on:click={submit}>Регистрация</button>
                <div class="p-wrapper"><p class="registration-p">Уже зарегистрированы? <a class="registration-a" href='./signin'>Войдите</a></p></div>
            </div>
        </form>
    </div>
</div>

<style>
    .component {
        height: 70%;
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    .checkboxes-block {
        margin-top: 15px;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    .inputs-block {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 200px;
    }

    .right-block {
        display: flex;
        flex-direction: row;
        justify-content: flex-end;
    }

    .social-networks {
        margin-right: 30px;
        width: 220px;
    }

    form {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 500px;
        width: 550px;
        margin-right: 5%;
    }
    .button-block {
        display: flex;
        justify-content: flex-start;
    }

    button {
        padding: 15px;
    }

    .registration-p, .registration-a {
        font-size: calc(var(--plain-font-size) - 5px);
    }
    .p-wrapper {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        margin-left: 20px;
    }

    .registration-p {
        /*margin-left: 20px;*/
        /*margin-top: 5px;*/
    }

    ul {
        list-style: none;
        margin-left: 0;
        padding: 0;
    }

    .social-link {
        text-decoration: none;
        color: #545454;
    }

    .social-link:hover {
        color: #1355FF;
    }
</style>
