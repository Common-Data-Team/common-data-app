<script>
    import Project from './_components/User_project.svelte';
    import Input from 'global_components/Input.svelte'
    import {params, goto} from '@roxi/routify';
    import { authorizedRequest, getCookie, getData } from '../../../_api.js';
    import { fly } from 'svelte/transition'
    import { onMount } from 'svelte';
    let screenWidth;

    export let user_projects_page = '/apps/user465_projects';
    export let user_profile_page = '/apps/user465';
    export let visible = false;
    let title = '';
    let participants_target = '';
    let auth = getCookie('user_id') === $params.user_id;

async function createProject() {
    const response = await authorizedRequest('projects/create', 'Post', {title, description: '', participants_target});
    console.log(response[0].project_link);
    // if (response[0].project_img === null) response[0].project_img = '/images/project_images/follow_project_card.png';
    promise = getData('users/'+ $params.user_id);
    visible = false;
}

let promise = getData('users/'+ $params.user_id);
</script>

<svelte:head>
    <title>Мои проекты</title>
</svelte:head>
<svelte:window bind:innerWidth={screenWidth} />
{#if visible}
<div id="window" on:click={(e) => {
    if (event.target.closest('.dialog') === null && visible) visible = false;
}}>
        <div class="dialog" transition:fly="{{ y: 200, duration: 800 }}">
            <h1>Новый проект</h1>
            <hr/>
            <Input class="dialog-input" bind:this={title} span="Название проекта" type="text"/>
            <Input class="dialog-input" bind:this={participants_target} span="Сколько человек требуется опросить?" type="number"/>
            <button on:click={createProject}>Создать проект</button>
        </div>
</div>
{/if}
<main>
{#await $promise}
    <h1>Загрузка...</h1>
{:then {as_leader}}
    <div class = "profile">
        <div class="main-block">
            <h2 class="pr">Проекты</h2>
        </div> 
        <div class="user_info">
            <section id='card_section' style="--columns-amount: {Math.floor((Math.min(screenWidth, 500) - 30) / 223)}">
                {#if auth}
                <div  class="new-project-btn" on:click={() => {
                    visible = true;
                }}><div class="project-card">
                    <div class="img-wrapper">
                      <img size="100%, 20%" src="/images/project_images/new_project.svg" class="img" alt="Картинка проекта">
                    </div>
                  
                    <div class="title">
                      <h2 class="project-title">Новый проект</h2>
                    </div>
                </div></div>
                    {/if}
                {#each as_leader.projects as card}
                    <Project {...card}></Project>
                {/each}
            </section>
        </div>
    </div>
{/await}
</main>
<style>
    section {
        min-width: 466px;
    }

    #window {
        position: absolute;
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        z-index: 100;
    }

    .dialog {
        width: 450px;
        background-color: #FFFFFF;
        border-radius: 10px;
        box-shadow: 0px 0px 103px 0px #A097A0;
        padding: 30px 30px 35px 30px;
        z-index: 1000;
    }

    .dialog :global(.dialog-input) {
        margin: 15px 0;
        width: 100%;
    }

    .dialog button {
        margin-top: 3px;
        font-size: 18px;
    }

    .new-project-btn {
        background-color: transparent;
        text-align: left;
        padding: 0;
        margin: 0;
        width: 223px;
        outline: none;
    }

    .new-project-btn:hover {
        cursor: pointer;
    }
    .project-card {
        height: 100%;
    }
    .img {
        object-fit: cover;
        height: 194px;
        width: 223px;
    }

    .project-title {
        font-family: "Helvetica Norm";
        font-size: calc(16px + (18 - 16) * ((100vw - 300px) / (1440 - 300)));
        padding-top: 5%;
        padding-bottom: 5%;
    }
    
    .img-wrapper {
        text-align: center;
    }

    .right-menu a {
        color: #545454;
        font-family: "Helvetica Norm";
        font-size: 20px;
        display: flex;
        flex-direction: column;
        text-align: right;
        text-decoration: none;
    }

    .profile {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
    }


    .pr {
        padding-bottom: 5%;
        font-size: 40px;
    }

    main {
        margin-left: 5%;
    }

    .edit {
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        margin-top: 15%;
        text-decoration-line: underline;
    }

    .user_info {
        display: flex;
        flex-direction: column;
        width: 40%;
        margin-right: 15%;
        margin-left: 20%;
    }
    @media (max-width: 1100px) {
        .user_info {
            margin-left: 5%;
        }
    }
    @media (min-width: 500px) {
         section {
        display: grid;
        justify-items: left;
        grid-template-columns: repeat(var(--columns-amount), 1fr);
        height: 100%;
        width: 100%;
    }
    }
    @media (max-width: 870px) {

        .profile {
            flex-direction: column;
        }

        .user_info {
            margin-right: 0%;
            margin-left: 0%;
            max-width: 90%;
            margin-top: 5%;
        }
    }
    @media (max-width: 500px) {
        main {
            margin: 0;
            width: 223px;
            padding: 20px;
        }
        section {
            min-width: 223px !important;
            display: flex !important;
            flex-direction: column;
        }

        #window {
            align-items: center;
        }

        .dialog {
            padding: 20px 15px;
            margin: 10px;
        }
    }
</style>