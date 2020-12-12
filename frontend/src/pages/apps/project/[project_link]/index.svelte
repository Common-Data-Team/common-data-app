<script>
  import ProjectPage from '../../_components/ProjectPage.svelte';
  import ProjectAbout from '../../_components/ProjectAbout.svelte';
  import Editor from '../../_components/Editor.svelte';
  import {params} from '@roxi/routify';
  import {getData, authorizedRequest, dataStore} from '../../../_api.js';
  import ProjectMenu from "../../_components/ProjectMenu.svelte";
  import {EditProject} from './_apiEdit';

  let edit = false;
  let promise = getData('projects/' + $params.project_link);
</script>
{#await $promise}
  <h1>Загрузка...</h1>
{:then data}
  <!--Сделать нормальную структуру-->
  <ProjectPage {...data} on:update={() => EditProject($params.project_link)} bind:edit={edit}/>
  <ProjectMenu/>
  <Editor bind:edit={edit}/>
{/await}