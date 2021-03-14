<script>
  import ProjectPage from './_components/ProjectPage.svelte';
  import ProjectAbout from './_components/ProjectAbout.svelte';
  import Editor from './_components/Editor.svelte';
  import {params} from '@roxi/routify';
  import {getData, authorizedRequest, dataStore} from '../../../_api.js';
  import {EditProject} from './_apiEdit';

  let edit = false;
  let promise = getData('projects/' + $params.project_link);
</script>
{#await $promise}
  <h1>Загрузка...</h1>
{:then data}
  <!--Сделать нормальную структуру-->
  <ProjectPage {...data} on:update={() => EditProject($params.project_link)} bind:edit={edit}/>
  <nav>
    <a class="active">Описание</a>
    <a>FAQ</a>
    <a>Обновления</a>
    <a>Комментарии</a>
  </nav>
  <Editor bind:edit={edit}/>
{/await}

<style>
  nav {
    margin: 40px 0 0 3%;
    display: flex;
  }

  a {
    margin: 0 40px 0 0;
    font-size: 18px;
    color: #282828;
    line-height: 24px;
    padding: 7px;
  }

  a:hover {
    cursor: pointer;
  }

  .active {
    border-bottom: 1px solid #282828;
  }
  @media (max-width: 600px) {
    a {
      display: none;
    }
    .active {
      display: block;
    }
  }
</style>