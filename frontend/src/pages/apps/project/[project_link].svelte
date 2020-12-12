<script>
  import ProjectPage from '../_components/ProjectPage.svelte';
  import ProjectAbout from '../_components/ProjectAbout.svelte';
  import Editor from '../_components/Editor.svelte';
  import {params} from '@roxi/routify';
  import {getData, authorizedRequest, dataStore} from '../../_api.js';
  import ProjectMenu from "../_components/ProjectMenu.svelte";
  import {projectLink} from './stores';

  async function EditProject() {
    let {title, participants_target, questionnaire, markdown, description, project_img, tags} = $dataStore;
    const response = await authorizedRequest('projects/' + $params.project_link + '/edit', 'PUT',
      {title, participants_target, questionnaire, markdown, description, project_img, tags});
  }

  let edit = false;
  let promise = getData('projects/' + $params.project_link);
  $projectLink = $params.project_link;
</script>
{#await $promise}
  <h1>Загрузка...</h1>
{:then data}
  <ProjectPage {...data} on:update={EditProject} bind:edit={edit}/>
  <ProjectMenu/>
  <Editor bind:edit={edit}/>
{/await}