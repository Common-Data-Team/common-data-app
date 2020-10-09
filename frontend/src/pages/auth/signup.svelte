<script>
    import {user, sendForm, selfUrl} from "../_api.js";
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
        let error = await sendForm(false, email.value, password.value);
        if (error) {
            errorMessage = error;
            return;
        }
        $goto(selfUrl, {}, false);
    }
</script>

<svelte:head>
    <title>Регистрация</title>
</svelte:head>

<div class="component">
    <h2>РЕГИСТРАЦИЯ:</h2>
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
            <div>
                <p class="label">Я хочу...</p>
                <div class="checkboxes-block">
                    <Checkbox id=0 text="Делиться данными"/>
                    <Checkbox id=1 text="Получать данные"/>
                </div>
            </div>
            <div class="inputs-block">
                <p class="error-label" class:showError>{errorMessage}</p>
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
        width: 90%;
        display: flex;
        flex-direction: row;
        margin-left: 5%;
    }

    .checkboxes-block {
        margin-top: 1%;
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
        margin-left: 15%;
        width: 220px;
        --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
    }

    form {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 400px;
        width: 550px;
        margin-right: 5%;
    }
    .button-block {
        display: flex;
        justify-content: flex-start;
    }

    button {
        padding: 2%;
        --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
        outline: none;
        border-radius: 0;
    }

    button:active, button:focus, button:hover {
        outline: none;
        background-color: #282828;
        border-radius: 0;
    }

    .registration-p, .registration-a {
        --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
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
    .error-label {
        text-align: center;
        align-self: center;
        margin-bottom: 1%;
        opacity: 0;
        transition: opacity ease 0.5s;
        --plain-font-size: calc(16px + (18 - 16) * ((100vw - 300px) / (1440 - 300)));
        color: red;
    }
    .showError{
        opacity: 1;
    }

    @media (max-width: 768px) {
        .component {
            flex-direction: column;
        }
        .right-block {
            flex-direction: column;
        }
        
        .social-networks {
            margin-left: 0;
            margin-top: 5%;
        }

        ul {
            margin-block-start: 0.5em;
        }

        .error-label {
            text-align: right;
            align-self: flex-start;
        }

        form {
            width: 95%;
        }
    }

</style>
