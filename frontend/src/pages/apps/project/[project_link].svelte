<script>
    import ProjectPage from '../_components/ProjectPage.svelte';
    import ProjectAbout from '../_components/ProjectAbout.svelte';
    import Editor from '../_components/Editor.svelte';
    import {params} from '@roxi/routify';
    import {getData, authorizedRequest, dataStore} from '../../_api.js';
    import ProjectMenu from "../_components/ProjectMenu.svelte";

    async function EditProject() {
        let data;
        dataStore.subscribe(value => {
           data = value;
        });
        let {title, participants_target, questionnaire, markdown, description, project_img, tags} = data;
        console.log(tags);
        const response = await authorizedRequest('projects/'+$params.project_link+'/edit', 'PUT',
                {title, participants_target, questionnaire, markdown, description, project_img, tags});
        console.log(response);
    }
    let edit = false;
    let promise = getData('projects/' + $params.project_link);
</script>
{#await $promise}
    <h1>Загрузка...</h1>
{:then data}
    <ProjectPage {...data} on:update={EditProject} bind:edit={edit}/>
    <ProjectMenu/>
    <Editor markdown={data.description} bind:edit={edit}/>
{/await}