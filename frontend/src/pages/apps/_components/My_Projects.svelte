<script>
    import Project from './Project.svelte';
    export let user_name = "Даня";
    export let user_surname = "Драгун";
    export let user_projects_page = '/user465_projects';
    export let user_profile_page = '/apps/user465';
    let full_name = user_name + " " + user_surname;
    let my_projects = [
    {
      title: 'Облысение. Что мы узнали благодаря вам',
      tags: ['Наука', 'Медицина'],
      progress: 42,
      author: "Камень Камень",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/user.jpg",
      projectImageSrc: "/images/project_images/follow_project_card.png"
    },
    {
      title: 'Ходьба оказалась вредной?',
      tags: ['Медицина'],
      progress: 92,
      author: "Камень Иванович",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/user.jpg",
      projectImageSrc: "/images/project_images/follow_project_card.png"
    },
    {
      title: 'Ходьба оказалась вредной?',
      tags: ['Медицина'],
      progress: 92,
      author: "Камень Иванович",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/user.jpg",
      projectImageSrc: "/images/project_images/follow_project_card.png"
    },
    {
      title: 'Ходьба оказалась вредной?',
      tags: ['Медицина'],
      progress: 92,
      author: "Камень Иванович",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/user.jpg",
      projectImageSrc: "/images/project_images/follow_project_card.png"
    }
  ]
</script>

<main>
    <a href="/" class="return-link">
        <div class = "return"> 
            <p class="arrow">→</p>
            <div class="chaif">Главная</div>
        </div>
    </a>
    <div class = "profile">
        <div class="main-block">
                <h2 class="pr">Профиль</h2>
                <a href="/" class="edit">Редактировать</a>
        </div> 
        <div class="user_info">
            <div class="container">
                <div class="cards">
                  {#each my_projects as card}
                    <Project {...card}></Project>
                  {/each}
                </div>
              </div>
        </div>
        <div class="right-menu">
            <a href={user_profile_page}>Информация</a>
            <a href="/info">Достижения</a>
            <u><a href={user_projects_page}>Мои проекты</a></u>
        </div>
    </div>
</main>
<style>
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