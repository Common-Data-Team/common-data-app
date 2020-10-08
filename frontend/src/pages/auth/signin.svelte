<script>
    import {goto, url} from "@sveltech/routify";
    import {getContext} from 'svelte';
    import Input from '../_components/Input.svelte'
    import {user, sendForm, selfUrl} from "../_api"

    let apiUrl = getContext('apiUrl');
    let form;
    let email;
    let password;
    let errorMessage = null;
    let socialNetworks = {
        facebook: 'https://facebook.com',
        twitter: 'https://twitter.com',
        vkontakte: 'https://vk.com'
    };
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

    async function submit() {
        if (!validateForm()) return;
        showError = false;
        let error = await sendForm(true, email.value, password.value);
        if (error) {
            errorMessage = error;
            return;
        }
        $goto(selfUrl, {}, false);

    }


</script>

<div class="component">
    <h1>ВХОД:</h1>
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
            <div class="inputs-block">
                <p class="error-label" class:showError>{errorMessage}</p>
                <Input bind:this={email} span="E-mail" name="username" type="email"/>
                <Input bind:this={password} span="Пароль" name="password" type="password"/>
            </div>
            <div class="button-block">
                <button type="button" on:click={submit}>Войти</button>
                <div class="p-wrapper"><p class="registration-p">Нет аккаунта? <a class="registration-a"
                                                                                  href='./signup'>Зарегистрируйтесь</a>
                </p></div>
            </div>
        </form>
    </div>
</div>

<style>
    .component {
        height: 50%;
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
        height: 150px;
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
        height: 250px;
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

    .error-label {
        background: #F45B69;
        padding: 6px;
        text-align: center;
        align-self: center;
        margin-bottom: 5px;
        opacity: 0;
        transition: opacity ease 0.5s;
        color: white;


    }

    .showError {
        opacity: 1;
    }
</style>
