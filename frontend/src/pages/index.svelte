<script>
    import {checkStoreAndCoockie, clearStoreAndCookie} from "./_api";
    import Project from './_components/Project.svelte';
    import FollowProject from './_components/Follow_Project.svelte';
    import NewProject from './_components/New_Project.svelte';
    import Footer from './_components/Footer.svelte';
    let current = 'user';
    let data = [
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
    ]

    let follow_projects = [
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

    let new_projects = [
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
            projectImageSrc: "/images/project_images/star_project.png"
        },
        {
            title: 'Ходьба оказалась вредной?',
            tags: ['Медицина'],
            progress: 92,
            author: "Камень Иванович",
            description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
            userImageSrc: "/images/user_images/user.jpg",
            projectImageSrc: "/images/project_images/Rectangle 4.png"
        }
    ]

    let auth = checkStoreAndCoockie();
    function logout() {
        auth = false;
        clearStoreAndCookie();
    }

</script>

<svelte:head>
    <title>Common Data</title>
</svelte:head>

<main>
    <div class="main-content-block">
        {#if !auth}
            <div class="log-out-block">
                <h2 class="log-out-text">ПЛАТФОРМА КРАУДСОРСИНГА ДАННЫХ ДЛЯ ПРОЕКТОВ И ИССЛЕДОВАНИЙ</h2>
                <div class="description">
                    <h2>КТО МЫ?</h2>
                    <p>Common data — это сервис, в котором пользователь может безопасно делиться своими данными с
                        исследовательскими и гражданскими проектами, ценности которых он разделяет.</p>
                    <h2>ПОЧЕМУ МЫ?</h2>
                    <div class="btn-about">
                        <button
                        class:active="{current === 'user'}"
                        on:click="{() => current = 'user'}"
                    >Пользователям</button>
                    <button
                        class:active="{current === 'project'}"
                        on:click="{() => current = 'project'}"
                    >Проектам</button>
                    </div>
                    {#if current == 'user'}
                    <div id="users-block">
                        <div class="point-block">
                            <h2>01</h2>
                            <p>Участвуйте в том, что для вас интересно и важно. Мы будем рекомендовать проекты, которые
                                    могут вам понравиться.</p>
                        </div>
                        <div class="point-block">
                            <h2>02</h2>
                            <p>Вы знаете, как и для чего будут использоваться ваши данные. Мы будем сообщать, что
                                    происходит с вашими данными, и каких результатов достигли проекты благодаря вам. </p>
                        </div>
                        <div class="point-block">
                            <h2>03</h2>
                            <p>Вам не нужно беспокоиться об анонимности и безопасности ваших данных. Мы об этом
                                    позаботимся!</p>
                        </div>
                    </div>
                    {:else}
                    <div id="users-block">
                        <div class="point-block">
                            <h2>01</h2>
                            <p>Формируйте датасеты. Мы поможем вам составить форму для сбора данных, предоставим место
                                    для хранения и инструменты.</p>
                        </div>
                        <div class="point-block">
                            <h2>02</h2>
                            <p>Привлекайте людей в ваш проект. Наши алгоритмы порекомендуют ваш проект именно тем
                                    пользователям, которым он может быть интересен.</p>
                        </div>
                        <div class="point-block">
                            <h2>03</h2>
                            <p>Находите единомышленников и новые идеи. Смотрите результаты и модели исследований по
                                    вашей теме от других участников.</p>
                        </div>
                    </div>
                    {/if}
                    <a href="./auth/signup"><button class="auth-buttons" onclick="./auth/signin">Регистрация</button></a>
                </div>
            </div>
        {/if}

        <!--
        <div class="auth-menu">
                <div class="menu-block">
                    <button 
                        class:menu-active="{selected_tag === 'all'}" 
                        on:click="{() => selected_tag = 'all'}">Все</button>
                    <button class:active="{selected_tag === 'bit'}" on:click="{() => selected_tag = 'bit'}">Бытовое</button>
                    <button>Наука</button>
                    <button>Медицина</button>
                    <button>Нейросети</button>
                </div>
                {#if auth}
                    <div class="user-buttons-menu">
                        <img src="/images/user_images/user.jpg" class="user-image-menu"/>
                    </div>
                {/if}
                {#if !auth} 
                    <div class="not-user-buttons-menu">
                        <a href='./auth/signin'>вход</a>
                        <a href='./auth/signup'>регистрация</a>
                    </div>
                {/if}
        </div>
        -->
        <div class="popular-block">
            <div class="block-title">
                <h2>ПОПУЛЯРНОЕ СЕЙЧАС</h2>
                <p class="arrow">→</p>
            </div>
            <div class="container">
                <div class="cards">
                  {#each data as card}
                    <Project {...card}></Project>
                  {/each}
                </div>
            </div>
        </div>

        {#if auth}
        <div class="popular-block">
            <div class="block-title">
                <h2>ВЫ ОТСЛЕЖИВАЕТЕ</h2>
                <p class="arrow">→</p>
            </div>
            <div class="container">
                <div class="cards">
                  {#each follow_projects as card}
                    <FollowProject {...card}></FollowProject>
                  {/each}
                </div>
            </div>
        </div>
        {/if}

        <div class="popular-block">
            <div class="block-title">
                <h2>НОВЫЕ ПРОЕКТЫ</h2>
                <p class="arrow">→</p>
            </div>
            <div class="container">
                <div class="cards">
                  {#each new_projects as card}
                    <NewProject {...card}></NewProject>
                  {/each}
                </div>
            </div>
        </div>
    </div>
</main>

<Footer></Footer>

<style>

    main {
        padding-left: 5%;
    }

    .btn-about {
        display: flex;
    }

    .btn-about button {
        width: 178px;
    }

    .arrow {
        font-family: "SF Pro Display";
        text-align: center;
        margin-left: 1%;
    }

    .auth-buttons {
        width: 211px;
        height: 43px;
        font-size: 20px;
        background-color: #282828;
        color: #f9f9f9;
        text-align: center;
    }

    .description {
        display: flex;
        flex-direction: column;
        max-width: 537px;
    }

    .description h2 {
        margin-bottom: 1%;
    }

    .description p {
        margin-bottom: 5%;
        --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
    }

    .log-out-block {
        display: flex;
        margin-bottom: 2%;
    }

    button {
        margin-top: 2%;
        background: transparent;
        text-align: center;
        color: #282828;
        max-width: 178px;
        border: 1px solid #282828;
        border-radius: 0;
        --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
    }

    button:hover {
        box-shadow: inset 0px 0px 0px 2px #282828;
        border-radius: 0;
        outline: none;
    }

    button:active {
        background-color: #E8E8E8;
        box-shadow: inset 0px 0px 0px 1px  #282828;
        border-radius: 0;
        color: #282828;
        outline: none;
    }

    button:focus {
        outline: none;
    }
  
	.active {
        background-color: #282828;
        outline: none;
        color: #F9F9F9;
	}

    .point-block {
        display: flex;
        align-items: stretch;
        margin-top: 5%;
    }

    .point-block p {
        max-width: 300px;
    }

    .point-block h2 {
        padding-right: 2%;
        font-size: calc(38px + (40 - 38) * ((100vw - 300px) / (1440 - 300)));
    }

    .log-out-text {
        max-width: 40%;
        padding-right: 2%;
    }

    .popular-block {
        max-width: 1130px;
        flex-direction: column;
        display: flex;
    }

    .block-title {
        display: flex;
        align-items: center;
        --plain-font-size: calc(24px + (32 - 24) * ((100vw - 300px) / (1440 - 300)));
        padding-bottom: 1%;
        padding-top: 5%;
    }

    a {
        color: #BDBDBD;
        font-family: "Helvetica Norm";
        --plain-font-size: calc(12px + (14 - 12) * ((100vw - 300px) / (1440 - 300)));
        text-decoration: none;
    }

    button {
		display: block;
    }

    a:hover {
        color: #1355FF;
    }

    .container {
        max-width: 1200px;
        text-align: left;
    }
    .cards {
        display: flex;
        justify-content: left;
        align-items: left;
        flex-wrap: wrap;
    }
    
    @media (max-width: 768px) {
        .description {
            max-width: 90%;
        }

        .description h2 {
            margin-top: 2%;
        }

        .log-out-block {
            flex-direction: column;
        }

        .popular-block {
            flex-direction: column;
        }

        .log-out-text {
            max-width: 90%;
        }
    }

</style>