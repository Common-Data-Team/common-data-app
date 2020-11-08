<script>
    import { Dialog, Textfield } from 'svelte-mui';
    import Project from './Project.svelte';

    let screenWidth;

    export let user_projects_page = '/apps/user465_projects';
    export let user_profile_page = '/apps/user465';
    export let visible = false;
    export let project_name = '';
    export let project_description = '';

    export let data = [
    {
      title: 'Плитка из камня',
      tags: ['Наука', 'Медицина'],
      progress: 42,
      author: "Камень Камень",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/user.jpg",
      projectImageSrc: "/images/project_images/Rectangle 4.png"
    },
    {
      title: 'Влияние проходимого расстояния на здоровье',
      tags: ['Наука', 'Медицина'],
      progress: 92,
      author: "Камень Иванович",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/user.jpg",
      projectImageSrc: "/images/project_images/star_project.png"
    },
    {
      title: 'Влияние проходимого расстояния на здоровье',
      tags: ['Наука', 'Медицина'],
      progress: 80,
      author: "Камень Иванович",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/user.jpg",
      projectImageSrc: "/images/project_images/follow_project_card.png"
    },

    {
      title: 'Плитка из камня',
      tags: ['Наука', 'Медицина'],
      progress: 42,
      author: "Камень Камень",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/user.jpg",
      projectImageSrc: "/images/project_images/Rectangle 4.png"
    },
    {
      title: 'Влияние проходимого расстояния на здоровье',
      tags: ['Наука', 'Медицина'],
      progress: 92,
      author: "Камень Иванович",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/user.jpg",
      projectImageSrc: "/images/project_images/star_project.png"
    },
    {
      title: 'Влияние проходимого расстояния на здоровье',
      tags: ['Наука', 'Медицина'],
      progress: 80,
      author: "Камень Иванович",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/user.jpg",
      projectImageSrc: "/images/project_images/follow_project_card.png"
    }
  ]
</script>

<svelte:head>
    <title>Мои проекты</title>
</svelte:head>
<svelte:window bind:innerWidth={screenWidth}/>

<Dialog width="290" bind:visible>
    <div slot="title">Новый проект</div>

    <Textfield
        name="Название проекта"
        autocomplete="off"
        required
        bind:value={project_name}
        label="Название проекта"
        message="Введите название проекта"
    />

    <div slot="actions" class="actions center">
        <button disabled>Создать проект</button>
    </div>
</Dialog>

<main>
    <a href="/" class="return-link">
        <div class = "return"> 
            <p class="arrow">→</p>
            <div class="chaif">Главная</div>
        </div>
    </a>
    <div class = "profile">
        <div class="main-block">
                <h2 class="pr">Проекты</h2>
        </div> 
        <div class="user_info">
            <section style="--columns-amount: {Math.floor((Math.min(screenWidth, 500) - 30) / 223)}">
                <button on:click={() => {
                    visible = true;
                }} class="new-project-btn"><div class="project-card">
                    <div class="img-wrapper">
                      <img size="100%, 20%" src="/images/project_images/new_project.svg" class="img" alt="Картинка проекта">
                    </div>
                  
                    <div class="title">
                      <h2 class="project-title">Новый проект</h2>
                    </div>
                </div></button>
                {#each data as card}
                    <Project {...card}></Project>
                {/each}
            </section>
        </div>
        <div class="right-menu">
            <a href={user_profile_page}>Информация</a>
            <a href="/info" disabled>Достижения</a>
            <u><a href={user_projects_page}>Мои проекты</a></u>
        </div>
    </div>
</main>
<style>

    .new-project-btn {
        background-color: transparent;
        text-align: left;
        padding: 0;
        margin: 0;
    }

    .new-project-btn {
        outline: none;
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
        width: 100%;
        text-align: center;
    }

    section {
        display: grid;
        justify-items: left;
        grid-template-columns: repeat(var(--columns-amount), 1fr);
        height: 100%;
        width: 100%;
    }

    .right-menu {
        margin-right: 5%;
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

    .return {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        margin-top: 2%;
        margin-bottom: 2%;
    }

    .return-link {
        text-decoration: none;
    }

    .return-link:hover {
        color: #282828;
    }

    .pr {
        padding-bottom: 5%;
        font-size: 40px;
    }

    main {
        margin-left: 5%;
    }

    .arrow{ 

        font-family: "SF Pro Display";
        font-size: 32px;
        text-align: center;

        color: #282828;
        transform: rotate(-180deg);
        align-self: center;
        margin-right: 2%;
    }

    .chaif {
        position: static;
        width: 77px;
        height: 24px;
        left: 53px;
        top: 7px;
        font-family: "Helvetica Norm";
        font-style: normal;
        font-weight: normal;
        line-height: 24px;
        display: flex;
        align-items: center;
        flex: none;
        order: 1;
        align-self: center;
        flex-grow: 0;
        margin: 16px 0px;
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

    @media (max-width: 768px) {

        main {
            width: 95%;
        }
        .profile {
            flex-direction: column;
        }

        .user_info {
            margin-right: 0%;
            margin-left: 0%;
            max-width: 90%;
            margin-top: 5%;
        }

        .right-menu {
            display: none;
        }
    }

</style>