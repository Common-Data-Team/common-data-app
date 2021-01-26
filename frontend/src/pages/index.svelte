<script>
  import { goto } from '@roxi/routify';
  import {clearStoreAndCookie, getCookie, getData} from "./_api";
  import Project from './_components/Project.svelte';
  import Footer from './_components/Footer.svelte';
  import Menu from '_components/Menu.svelte'
  import MenuItem from '_components/MenuItem.svelte'

  let current_tag = 'all';
  let screenWidth;
  let current = 'user';
  let data = [
    {
      title: 'Плитка из камня.',
      tags: ['Наука', 'Медицина'],
      progress: 42,
      author: "Камень Камень",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/default.jpg",
      projectImageSrc: "/images/project_images/Rectangle 4.png"
    },
    {
      title: 'Влияние проходимого расстояния на здоровье',
      tags: ['Наука', 'Медицина'],
      progress: 92,
      author: "Камень Иванович",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/default.jpg",
      projectImageSrc: "/images/project_images/star_project.png"
    },
    {
      title: 'Влияние проходимого расстояния на здоровье',
      tags: ['Наука', 'Медицина'],
      progress: 80,
      author: "Камень Иванович",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/default.jpg",
      projectImageSrc: "/images/project_images/follow_project_card.png"
    },

    {
      title: 'Плитка из камня',
      tags: ['Наука', 'Медицина'],
      progress: 42,
      author: "Камень Камень",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/default.jpg",
      projectImageSrc: "/images/project_images/Rectangle 4.png"
    },
    {
      title: 'Влияние проходимого расстояния на здоровье',
      tags: ['Наука', 'Медицина'],
      progress: 92,
      author: "Камень Иванович",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/default.jpg",
      projectImageSrc: "/images/project_images/star_project.png"
    },
    {
      title: 'Влияние проходимого расстояния на здоровье',
      tags: ['Наука', 'Медицина'],
      progress: 80,
      author: "Камень Иванович",
      description: "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.",
      userImageSrc: "/images/user_images/default.jpg",
      projectImageSrc: "/images/project_images/follow_project_card.png"
    }
  ]

  let auth = getCookie('access_token');

  function logout() {
    auth = false;
    clearStoreAndCookie();
  }

  const promise = getData('projects/all');
</script>

<svelte:head>
  <title>Common Data</title>
  <meta name="yandex-verification" content="e2935006109ebd77" />
</svelte:head>
<svelte:window bind:innerWidth={screenWidth}/>

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
            >Пользователям
            </button>
            <button
                class:active="{current === 'project'}"
                on:click="{() => current = 'project'}"
            >Проектам
            </button>
          </div>
          {#if current == 'user'}
            <div class="users-block">
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
            <div class="users-block">
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
          <div class="auth-buttons-block">
            <button class="auth-buttons" onclick={() => $goto('./auth/signup')}>Регистрация</button>
            <button class="auth-buttons mobile-only" onclick={() => $goto('./auth/signin')}>Войти</button>
          </div>
        </div>
      </div>
    {/if}

    <div class="auth-menu">
            <div class="menu-block">
            <button
                class:active="{current_tag === 'all'}"
                on:click="{() => current_tag = 'all'}"
            >Все</button>
                <button class:active="{current_tag === 'Бытовое'}"
                on:click="{() => current_tag = 'Бытовое'}">Бытовое</button>
                <button class:active="{current_tag === 'Наука'}"
                on:click="{() => current_tag = 'Наука'}">Наука</button>
                <button class:active="{current_tag === 'Медицина'}"
                on:click="{() => current_tag = 'Медицина'}">Медицина</button>
                <button class:active="{current_tag === 'Нейросети'}"
                on:click="{() => current_tag = 'Нейросети'}">Нейросети</button>
            </div>
            <div class="user-buttons-menu">
              {#if auth}
                <Menu>
                  <img src="/images/user_images/default.jpg" class="user-image-menu" slot="activation"/>
                  <MenuItem>Достижения</MenuItem>
                  <MenuItem on:click={() => $goto('../apps/user/'+getCookie('user_id'))}>Профиль</MenuItem>
                  <hr/>
                  <MenuItem on:click={logout}>Выход</MenuItem>
                </Menu>
            {/if}
            {#if !auth}
                <div class="not-user-buttons-menu desktop-only">
                    <a href='./auth/signin'>вход</a>
                    <a href='./auth/signup'>регистрация</a>
                </div>
            {/if}
            </div>
    </div>

    <div class="popular-block">
      <div class="block-title">
        <h2>ПРОЕКТЫ</h2>
        <p class="arrow">→</p>
      </div>
      <section style="--columns-amount: {Math.floor((Math.min(screenWidth, 1200) - 110) / 350)}">
        {#await $promise}
        <p>Загрузка...</p>
        {:then data}
          {#each data as card}
                <Project {...card}></Project>
          {/each}
        {/await}
      </section>
    </div>
<!--
    {#if auth}
      <div class="popular-block">
        <div class="block-title">
          <h2>ВЫ ОТСЛЕЖИВАЕТЕ</h2>
          <p class="arrow">→</p>
        </div>
        <section style="--columns-amount: {Math.floor((Math.min(screenWidth, 1200) - 30) / 500)}">
            {#each data as card}
                <FollowProject {...card}></FollowProject>
            {/each}
        </section>
      </div>
    {/if}

    <div class="popular-block">
      <div class="block-title">
        <h2>НОВЫЕ ПРОЕКТЫ</h2>
        <p class="arrow">→</p>
      </div>
      <section style="--columns-amount: {Math.floor((Math.min(screenWidth, 1200) - 30) / 223)}">
        {#each data as card}
            <NewProject {...card}></NewProject>
        {/each}
      </section>
    </div>
    -->
  </div>
</main>
<Footer/>

<style>
  hr {
    margin: 0;
  }
  main {
    padding-left: 5%;
  }

  .btn-about {
    display: flex;
  }

  .btn-about button {
    width: 178px;
  }

  section {
    display: grid;
    justify-items: left;
    grid-template-columns: repeat(var(--columns-amount), 1fr);
    height: 100%;
    width: 100%;
  }

  .arrow {
    font-family: "SF Pro Display";
    text-align: center;
    margin-left: 1%;
  }

  .auth-buttons-block {
    width: 100%;
    display: flex;
    padding-right: 20px;
  }

  .auth-buttons {
    width: 211px;
    height: 43px;
    font-size: 20px;
    background-color: #282828;
    color: #f9f9f9;
    text-align: center;
    margin-right: 10px;
  }

  .not-user-buttons-menu {
    display: flex;
    flex-direction: column;
    text-align: right;
  }

  .not-user-buttons-menu a {
    color: #282828;
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
    box-shadow: inset 0px 0px 0px 1px #282828;
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
    max-width: 95%;
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

  .user-buttons-menu {
    margin-left: auto;
  }

  .auth-menu {
    display: flex;
    max-width: 90%;
  }

  .menu-block {
    display: flex;
  }

  .user-image-menu {
    width: 41px;
    height: 41px;
    border-radius: 50%;
  }


  .auth-menu button {
    border: none;
    padding: 0.188em 0.625em;
  }

  button {
    display: block;
  }

  a:hover {
    color: #1355FF;
  }

  .mobile-only {
    display: none;
  }

  @media (max-width: 768px) {

    main {
      padding-right: 5%;
    }

    .btn-about {
      margin: 5px 0 10px 0;
    }

    .popular-block {
      max-width: 768px;
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

    .popular-block {
      flex-direction: column;
    }

    .log-out-text {
      max-width: 90%;
    }
    .menu-block {
      width: auto;
      overflow-x: scroll;
      margin: 20px 0 10px 0;
    }

    .auth-buttons {
      width: 40vw;
      min-width: 100px;
      font-size: min(5vw, 20px);
      margin-top: 20px;
    }

    .mobile-only {
      display: block;
    }

    .desktop-only {
      display: none;
    }
  }

</style>
