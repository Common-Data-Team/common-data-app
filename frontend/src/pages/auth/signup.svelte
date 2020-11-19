<script>
  import {user, submitForm, selfUrl} from "../_api.js";
  import {goto, url} from "@roxi/routify";
  import {getContext} from 'svelte';
  import Input from '../_components/Input.svelte'
  import Checkbox from "svelte-checkbox";

  let checked = false;

  let socialNetworks = {
    facebook: 'https://facebook.com',
    twitter: 'https://twitter.com',
    vkontakte: 'https://vk.com'
  };
  let apiUrl = getContext('apiUrl');
  let form;
  let name;
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

  async function handleClick() {
    if (!validateForm()) return;
    showError = false;
    let error = await submitForm(false, email.value, password.value);
    alert(error)
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
      <div class="inputs-block">
        <Input bind:this={name} span="Имя и фамилия" name="name" type="text"/>
        <Input bind:this={email} span="E-mail" name="username" type="email"/>
        <Input bind:this={password} span="Пароль" name="password" type="password"/>
        <Input bind:this={password2} span="Подтверждение пароля" name="password" type="password"/>
      </div>
      <div class="privacy-policy">
        <Checkbox size="1.5rem" secondaryColor="#282828" primaryColor="#1355FF"></Checkbox>
        <span class="text-login01">Я принимаю <a
          style='text-decoration: underline;'>
                    пользовательское соглашение</a></span>
      </div>
      <p class="error-label" class:showError>{errorMessage}</p>
      <div class="button-block">
        <button type="button" on:click={handleClick}>Регистрация</button>
        <div class="p-wrapper"><p class="registration-p"><a class="registration-a" href='./signin'>Авторизация</a></p>
        </div>
      </div>
    </form>
  </div>
</div>

<style>

    .privacy-policy {
        display: flex;
        text-align: center;
    }

    .text-login01 {
        cursor: pointer;
        margin-right: 3%;
        margin-left: 3%;
        font-family: "Helvetica Norm", sans-serif;
        text-align: center;
        align-self: center;
    }

    .component {
        height: 70%;
        width: 90%;
        display: flex;
        flex-direction: row;
        margin-left: 5%;
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
        font-size: 16px;
        padding: 2%;
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

    .showError {
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
