<script>
    import {checkStoreAndCoockie, clearStoreAndCookie} from "./_api";
    let auth = checkStoreAndCoockie();
    function logout(){
        auth = false;
        clearStoreAndCookie();
    }
</script>

<main>
    {#if !auth}
    <div class="log-out-block">
        <h2 class="log-out-text">ПЛАТФОРМА КРАУДСОРСИНГА ДАННЫХ ДЛЯ ПРОЕКТОВ И ИССЛЕДОВАНИЙ</h2>
        <div class="description">
            <h2>КТО МЫ?</h2>
            <p>Common data — это сервис, в котором пользователь может безопасно делиться своими данными с исследовательскими и гражданскими проектами, ценности которых он разделяет.</p>
            <h2>ПОЧЕМУ</h2>
            <div class="about-buttons">
                <button onclick="(document.getElementById('users-block').style.display='block'); (document.getElementById('project-block').style.display='none');">Пользователям</button>
                <button onclick="(document.getElementById('project-block').style.display='block'); (document.getElementById('users-block').style.display='none')">Проектам</button>
                <div id="users-block">
                    <div class="point-block">
                        <h1>01</h1>
                        <p>Участвуйте в том, что для вас интересно и важно. Мы будем рекомендовать проекты, которые могут вам понравиться.</p>
                    </div>
                    <div class="point-block">
                        <h1>02</h1>
                        <p>Вы знаете, как и для чего будут использоваться ваши данные. Мы будем сообщать, что происходит с вашими данными, и каких результатов достигли проекты благодаря вам. </p>
                    </div>
                    <div class="point-block">
                        <h1>03</h1>
                        <p>Вам не нужно беспокоиться об анонимности и безопасности ваших данных. Мы об этом позаботимся!</p>
                    </div>
                </div>
                <div id="project-block">
                    <div class="point-block">
                        <h1>01</h1>
                        <p>Формируйте датасеты. Мы поможем вам составить форму для сбора данных, предоставим место для хранения и инструменты.</p>
                    </div>
                    <div class="point-block">
                        <h1>02</h1>
                        <p>Привлекайте людей в ваш проект. Наши алгоритмы порекомендуют ваш проект именно тем пользователям, которым он может быть интересен.</p>
                    </div>
                    <div class="point-block">
                        <h1>03</h1>
                        <p>Находите единомышленников и новые идеи. Смотрите результаты и модели исследований по вашей теме от других участников.</p>
                    </div>
                </div>
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
        <a href="./auth/signin">Вход</a>
        <a href="./auth/signup">Регистрация</a>
    </div>
    <div class="popular-block">
        <div class="block-title">
            <h2>ПОПУЛЯРНОЕ СЕЙЧАС</h2>
            <p class="arrow">→</p>
        </div>
        <div class="сard-block">
            <div class="project-card">
                <img src="/images/project_images/Rectangle 4.png" class="project-image" alt="project-image" />
                <h2 class="project-title">Влияние проходимого расстояния на здоровье</h2>
                <div class="tags">
                    <a href="/" class="tag-href">Наука</a>
                    <a href="/" class="tag-href">Медицина</a>
                </div>
                <p class="percent-title">Собрано 42%</p>
                <div class="progress-bar horizontal">
                    <div class="progress-track">
                      <div class="progress-fill">
                      </div>
                    </div>
                </div>
                <div class="user">
                    <img src="/images/user_images/user.jpg" class="user-img" alt="user-img" />
                    <p>Камень Иванович</p>
                </div>
            </div>
            <div class="project-card">
                <img src="/images/project_images/Rectangle 4.png" class="project-image" alt="project-image" />
                <h2 class="project-title">Влияние проходимого расстояния на здоровье</h2>
                <div class="tags">
                    <a href="/" class="tag-href">Здоровье</a>
                    <a href="/" class="tag-href">Медицина</a>
                </div>
                <p class="percent-title">Собрано 42%</p>
                <div class="progress-bar horizontal">
                    <div class="progress-track">
                      <div class="progress-fill">
                      </div>
                    </div>
                </div>
                <div class="user">
                    <img src="/images/user_images/user.jpg" class="user-img" alt="user-img" />
                    <p>Камень Иванович</p>
                </div>
            </div>
            <div class="project-card">
                <img src="/images/project_images/Rectangle 4.png" class="project-image" alt="project-image" />
                <h2 class="project-title">Влияние проходимого расстояния на здоровье</h2>
                <div class="tags">
                    <a href="/" class="tag-href">Здоровье</a>
                    <a href="/" class="tag-href">Медицина</a>
                </div>
                <p class="percent-title">Собрано 42%</p>
                <div class="progress-bar horizontal">
                    <div class="progress-track">
                      <div class="progress-fill">
                      </div>
                    </div>
                </div>
                <div class="user">
                    <img src="/images/user_images/user.jpg" class="user-img" alt="user-img" />
                    <p>Камень Иванович</p>
                </div>
            </div>
        </div>
        </div>
</main>

<footer>
        <img src="white_logo.svg" class="logo-white" alt="logo-white" />
        <div class="column-block">
            <h3>О НАС</h3>
            <ul>
                <a href="vk.com"><li>проектам</li></a>
                <a href="vk.com"><li>пользователям</li></a>
            </ul>
        </div>
        <div class="column-block">
            <h3>СВЯЗАТЬСЯ С НАМИ</h3>
            <ul>
                <a href="vk.com"><li>help@commondata.ru</li></a>
                <a href="vk.com"><li>+7 (901) 723-04-47</li></a>
            </ul>
        </div>
        <div class="column-block">
            <h3>СОЦСЕТИ</h3>
            <ul>
                <a href="https://vk.com"><li>facebook</li></a>
                <a href="vk.com"><li>telegram</li></a>
                <a href="vk.com"><li>vkontakte</li></a>
            </ul>
        </div>
</footer>

<style>

    .arrow {
        font-family: "SF Pro Display";
        text-align: center;
        margin-left: 1%;
    }

    #project-block {
        display: none;
    }

    .description {
        display: flex;
        flex-direction: column;
        max-width: 40%;
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
    }

    .about-buttons button {
        background: transparent;
        text-align: center;
        color: #282828;
        border: 1px solid #282828;
        border-radius: 0;
        --plain-font-size: calc(14px + (16 - 14) * ((100vw - 300px) / (1440 - 300)));
    }

    .about-buttons button:focus, .about-buttons button:active, .about-buttons button:hover {
        background-color: #282828;
        outline: none;
        color: #F9F9F9;
    }

    .point-block {
        display: flex;
        align-content: center;
        margin-top: 5%;
    }

    .point-block h1 {
        padding-right: 2%;
    }

    .log-out-text {
        max-width: 20%;
        padding-right: 10%;
    }

    .menu-block {
        display: flex;
        margin-bottom: 3%;
    }

    .menu-block button {
        background: transparent;
        text-align: center;
        color: #282828;
        --plain-font-size: calc(14px + (16 - 14) * ((100vw - 300px) / (1440 - 300)));
        margin-right: 1%;
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

        .column-block {
            margin-left: 5%;
        }

        .popular-block {
            flex-direction: column;
        }
    }

</style>