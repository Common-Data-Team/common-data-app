<script>
    import {goto} from "@sveltech/routify"
    import {checkStoreAndCoockie, clearStoreAndCookie} from "./_api";
    import Project from './_components/Project.svelte';
    let current = 'user';
    let data = [
        {
            title: 'Плитка из камня',
            tags: ['Наука', 'Медицина'],
            progress: 42,
            author: "Камень Камень",
            userImageSrc: "/images/user_images/user.jpg",
            projectImageSrc: "/images/project_images/Rectangle 4.png"
        },
        {
            title: 'Влияние проходимого расстояния на здоровье',
            tags: ['Наука', 'Медицина'],
            progress: 92,
            author: "Камень Иванович",
            userImageSrc: "/images/user_images/user.jpg",
            projectImageSrc: "/images/project_images/Rectangle 4.png"
        },
        {
            title: 'Влияние проходимого расстояния на здоровье',
            tags: ['Наука', 'Медицина'],
            progress: 80,
            author: "Камень Иванович",
            userImageSrc: "/images/user_images/user.jpg",
            projectImageSrc: "/images/project_images/Rectangle 4.png"
        },
    ]

    let auth = checkStoreAndCoockie();
    function logout() {
        auth = false;
        clearStoreAndCookie();
    }

</script>

<svelte:head>
    <title>Common Data</title>
    <link rel="shortcut icon" href="/favicon.svg" type="image/svg+xml">
</svelte:head>

<main>
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
                <div class="about-buttons">
                    <a href="./auth/signin"><button id="auth-buttons" onclick="./auth/signin">Регистрация</button></a>
                </div>
            </div>
        </div>
    {/if}
    {#if auth}
        <button on:click={logout}>Выйти</button>
    {/if}
    <div class="menu-block">
        <button>Все</button>
        <button>Бытовое</button>
        <button>Социальное</button>
        <button>Наука</button>
        <button>Медицина</button>
        <button>Нейросети</button>
    </div>
    <div class="popular-block">
        <div class="block-title">
            <h2>ПОПУЛЯРНОЕ СЕЙЧАС</h2>
            <p class="arrow">→</p>
        </div>
        <div class="сard-block">
            {#each data as card}
                <Project {...card}/>
            {/each}
        </div>
    </div>
</main>

<footer>
    <img src="white_logo.svg" class="logo-white" alt="logo-white"/>
    <div class="column-block">
        <h3>О НАС</h3>
        <ul>
            <a href="vk.com">
                <li>проектам</li>
            </a>
            <a href="vk.com">
                <li>пользователям</li>
            </a>
        </ul>
    </div>
    <div class="column-block">
        <h3>СВЯЗАТЬСЯ С НАМИ</h3>
        <ul>
            <a href="vk.com">
                <li>help@commondata.ru</li>
            </a>
            <a href="vk.com">
                <li>+7 (901) 723-04-47</li>
            </a>
        </ul>
    </div>
    <div class="column-block">
        <h3>СОЦСЕТИ</h3>
        <ul>
            <a href="https://vk.com">
                <li>facebook</li>
            </a>
            <a href="vk.com">
                <li>telegram</li>
            </a>
            <a href="vk.com">
                <li>vkontakte</li>
            </a>
        </ul>
    </div>
</footer>

<style>

    .btn-about {
        display: flex;
    }

    .btn-about button {
        width: 178px;
    }

    main {
        margin-left: 5%;
    }

    .arrow {
        font-family: "SF Pro Display";
        text-align: center;
        margin-left: 1%;
    }

    #auth-buttons {
        font-size: 20px;
        max-width: 211px;
    }

    #project-block {
        display: none;
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

    .about-buttons {
        display: flex;
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
        box-shadow: inset 0px 0px 0px 3px #282828;
        border-radius: 0;
        outline: none;
    }

    button:active {
        background-color: #E8E8E8;
        box-shadow: inset 0px 0px 0px 2px  #282828;
        border-radius: 0;
        color: #282828;
        outline: none;
    }

    button:focus {
        outline: none;
    }

    .about-buttons button:focus, .about-buttons button:checked, .about-buttons button:active, .about-buttons button:hover {
        background-color: #282828;
        outline: none;
        color: #F9F9F9;
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
    }

    .menu-block {
        display: flex;
        margin-bottom: 3%;
    }

    .menu-block button {
        box-shadow: none;
        border: none;
        background: transparent;
        text-align: center;
        color: #282828;
        --plain-font-size: calc(14px + (16 - 14) * ((100vw - 300px) / (1440 - 300)));
        margin-right: 1%;
        max-width: 10%;
    }

    .menu-block button:hover {
        color: #F9F9F9;
        background-color: #282828;
        border-radius: 0;
    }

    .logo {
        max-width: 890px;
        max-height: 119px;
        margin-bottom: 3%;
        margin-top: 3%;
    }

    .popular-block {
        flex-direction: column;
        display: flex;
    }

    .сard-block {
        display: flex;
    }

    .block-title {
        display: flex;
        align-items: center;
        --plain-font-size: calc(24px + (32 - 24) * ((100vw - 300px) / (1440 - 300)));
        padding-bottom: 1%;
    }

    footer {
        flex: 0 0 auto;
        display: flex;
        bottom: 0;
        padding: 5% 0;
        margin-top: 5%;
        width: 100%;
        background: #282828;
        justify-content: center;
        align-items: stretch;
    }

    .logo-white {
        max-width: 285px;
        margin-right: 15%;
    }

    a {
        color: #BDBDBD;
        font-family: "Helvetica Norm";
        --plain-font-size: calc(12px + (14 - 12) * ((100vw - 300px) / (1440 - 300)));
        text-decoration: none;
    }

    .tags {
        display: flex;
    }

    .user {
        margin-top: 5%;
        display: flex;
        align-items: center;
    }

    button {
		display: block;
	}

    .user p {
        --plain-font-size: calc(14px + (16 - 14) * ((100vw - 300px) / (1440 - 300)));
        text-align: center;
        margin-left: 2%;
    }

    .user-img {
        width: 36px;
        height: 36px;
        border-radius: 50%;
    }

    .tag-href {
        background-color: #282828;
        border-radius: 18px;
        text-align: center;
        padding: 0.6em 0.6em;
        margin: 5%;
        margin-right: 2%;
        margin-left: 0%;
        color: #F9F9F9;
    }

    .tag-href:hover {
        background-color: #1355FF;
        color: #F9F9F9;
    }

    a:hover {
        color: #1355FF;
    }

    .percent-title {
        --plain-font-size: calc(12px + (14 - 12) * ((100vw - 300px) / (1440 - 300)));
        padding-bottom: 2%;
    }

    .column-block {
        margin-right: 10%;
    }

    h3 {
        color: #F9F9F9;
        --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
        font-family: "Helvetica Neue";
    }

    .project-title {
        --plain-font-size: calc(24px + (32 - 24) * ((100vw - 300px) / (1440 - 300)));
        padding-top: 2%;
    }

    .project-card {
        display: flex;
        flex-direction: column;
        max-width: 20%;
        margin-right: 5%;
    }

    .horizontal .progress-track {
        position: relative;
        max-width: 80%;
        max-height: 5px;
        border-radius: 6px;
        background: #DADADA;
    }

    .horizontal .progress-fill {
        position: relative;
        background: #3d3434;
        height: 5px;
        border-radius: 6px;
        max-width: 42%;
        color: #fff;
    }

    .project-image {
        max-width: 350px;
        max-height: 268px;
    }

    li {
        list-style-type: none;
    }

    ul {
        padding: 0;
    }

    @media (max-width: 768px) {
        footer {
            flex-direction: column;
        }

        .logo-white {
            max-width: 200px;
            margin-left: 5%;
            margin-bottom: 5%;
        }

        .сard-block {
            max-width: 90%;
            margin-bottom: 5%;
        }

        .description {
            max-width: 90%;
        }

        .description h2 {
            margin-top: 2%;
        }

        .log-out-block {
            flex-direction: column;
        }

        .сard-block {
            flex-direction: column;
        }

        .column-block {
            margin-left: 5%;
        }

        .popular-block {
            flex-direction: column;
        }

        .log-out-text {
            max-width: 90%;
        }
    }

</style>