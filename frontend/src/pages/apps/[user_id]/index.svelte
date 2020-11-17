<script>
  import {ready, url, params} from '@roxi/routify';
  import {getContext} from 'svelte';
  import {writable} from "svelte/store";
  import { getCookie } from '../../_api.js';

  let apiUrl = getContext('apiUrl');
  let fio, email, avatar, about, tags;
  function getData(id) {
    id = id.slice(4);
    const store = writable(new Promise(() => {}));

    const load = async () => {
      let auth = false;
      if (getCookie('user_id') === id) auth = true;
      const response = await fetch(apiUrl + `users/${id}`);
      const data = await response.json();
      console.log(data);
      if (data.about === null) data.about = 'Напишите о себе!';
      if (data.avatar === null) data.avatar = '/images/user_images/user.jpg';
      data.auth = auth;
      if (data.tags.length === 0) data.tags.push({name: 'Пока нет('});
      store.set(Promise.resolve(data));
      $ready();
    };
    load();
    return store;
  }
  const promise = getData($params.user_id);
</script>

<main>
  <div class="profile">
    {#await $promise}
      <h1>Загрузка...</h1>
    {:then {fio, avatar, about, tags, as_member, auth}}
      <div class="main-block">
        <h2 class="pr">Профиль</h2>
        {#if auth}
        <a href="/" class="edit">Редактировать</a>
          {/if}
      </div>
      <div class="user_info">
        <div class="user">
          <img src={avatar} class="photo" alt="user_photo"/>
          <h2 class="title" id="name">{fio}</h2>
        </div>
        <div class="self">
          <h2 class="title"> О себе:</h2>
          <p>{about}</p>
        </div>
        <div class="catigories">
          <h2 class="title">Предпочтения</h2>
          <div class="tag-container">
            <div class="tags">
              {#each tags as tag}
                <a class="tag-href">{tag.name}</a>
              {/each}
            </div>
          </div>
        </div>
        <div clsaa="exexperience">
          <h2 class="title">Участие в проектах:</h2>
          <div class="experience-tags">
            <li>
            {#if as_member.projects.length === 0}
            <ul>Пока проектов нет.</ul>
              {:else}
              {#each as_member.projects as project}
                <ul><a href={project.project_href} class="ex-tag">{project.title}</a></ul>
              {/each}
              {/if}
            </li>
          </div>
        </div>
      </div>

    {/await}
  </div>
</main>
<style>

  .tag-container {
    margin-top: 2%;
    max-width: 70%;
    text-align: left;
  }


  .tag-href {
    background-color: #282828;
    border-radius: 18px;
    text-align: center;
    padding: 0.375em 0.75em;
    margin-right: 2%;
    margin-left: 0;
    color: #F9F9F9;
    text-decoration: none;
    margin-top: 2%;
  }

  .ex-tag {
    text-decoration: none;
  }

  .tags {
    display: flex;
    justify-content: left;
    align-items: left;
    flex-wrap: wrap;
  }

  #name {
    padding-top: 3%;
  }

  .title {
    font-size: 24px;
  }

  .profile {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    width: 60%;
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
  }

  .user {
    margin-bottom: 10%;
  }

  .self {
    margin-bottom: 10%;
  }

  .catigories {
    margin-bottom: 10%;
  }

  .experience-tags {
    margin-top: 2%;
  }

  .ex-tag {
    text-decoration: none;
  }

  .photo {
    object-fit: cover;
    width: 128px;
    height: 128px;
    border-radius: 50%;
    margin-bottom: 1%;
  }

  li {
    list-style-type: none;
    margin-bottom: 30%;
  }

  ul {
    padding: 0;
    margin-block-start: 0em;
    margin-block-end: 0em;
    padding: 0;
    margin: 0;
    padding-inline-start: 0px;
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