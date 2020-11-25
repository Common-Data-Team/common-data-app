<script>
    import Project from '../../_components/Project.svelte';
    import { Dialog, Textfield } from 'svelte-mui';
    import {params, goto} from '@roxi/routify';
    import { authorizedRequest, getCookie, getData } from '../../../_api.js';
    import { onMount } from 'svelte';
    let screenWidth;

    export let user_projects_page = '/apps/user465_projects';
    export let user_profile_page = '/apps/user465';
    export let visible = false;
    let title = '';
    let description = '';
    let participants_target = '';
    let auth = getCookie('user_id') === $params.user_id;
function textareaIncrease(event) {
    let elem = event.target;
    if (elem.scrollTop > 0) {
        elem.style.height = elem.scrollHeight + 'px';
    }
}

async function createProject() {
    const response = await authorizedRequest('projects/create', 'Post', {title, description, participants_target});
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
<svelte:window bind:innerWidth={screenWidth}/>

<Dialog width="490" bind:visible>
    <div slot="title">Новый проект</div>

    <Textfield
        name="Название проекта"
        autocomplete="off"
        bind:value={title}
        label="Название проекта"
    />
<!--    TODO сделать улетающий label для textarea-->
    <textarea class="description_input" placeholder="Описание проекта" on:keyup={textareaIncrease} bind:value={description}></textarea>
    <div class="focus-line"></div>
    <Textfield
        name="Сколько человек требуется опросить?"
        autocomplete="off"
        bind:value={participants_target}
        label="Сколько человек требуется опросить?"
    />
    <div slot="actions" class="actions center">
        <button on:click={createProject}>Создать проект</button>
    </div>
</Dialog>

<main>
{#await $promise}
    <h1>Загрузка...</h1>
{:then {as_leader}}
    <div class = "profile">
        <div class="main-block">
                <h2 class="pr">Проекты</h2>
            {#if auth}
        <a href="/" class="edit">Редактировать</a>
          {/if}
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

    .description_input {
        width: 100%;
        border: 0;
        border-bottom: 1px solid #999999;
        background-color: transparent;
        resize: vertical;
        font-size: 17px;
        height: 25px;
        font-family: Roboto, 'Segoe UI', sans-serif;
        font-weight: 400;
        color: #333;
        padding: 0;
    }
    .description_input:focus {
        outline: none;
    }
    .description_input::placeholder {
        padding: 5px 0 0 0;
        font-size: 15px;
        color: #ababab;
    }
    .description_input:focus ~ .focus-line {
		transform: scaleX(1);
		opacity: 1;
	}
    .focus-line {
		height: 2px;
		-webkit-transform: scaleX(0);
		transform: scaleX(0);
		transition: transform 0.18s cubic-bezier(0.4, 0, 0.2, 1),
			opacity 0.18s cubic-bezier(0.4, 0, 0.2, 1),
			-webkit-transform 0.18s cubic-bezier(0.4, 0, 0.2, 1);
		transition: transform 0.18s cubic-bezier(0.4, 0, 0.2, 1),
			opacity 0.18s cubic-bezier(0.4, 0, 0.2, 1);
		opacity: 0;
		z-index: 2;
		background: #1976d2;
        margin: -5px 0 0 0;
        width: 100%;
	}
    section {
        min-width: 466px;
    }
    .new-project-btn {
        background-color: transparent;
        text-align: left;
        padding: 0;
        margin: 0;
        width: 223px;
    }

    .new-project-btn {
        outline: none;
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
        }
        section {
            min-width: 223px !important;
            display: flex !important;
            flex-direction: column;
        }
    }
</style>