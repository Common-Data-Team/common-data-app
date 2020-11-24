<script>
    import ProjectPage from '../_components/ProjectPage.svelte';
    import ProjectAbout from '../_components/ProjectAbout.svelte';
    import Editor from '../_components/Editor.svelte';
    import {params} from '@roxi/routify';
    import {getData, authorizedRequest, cache} from '../../_api.js';
    import ProjectMenu from "../_components/ProjectMenu.svelte";
    let {title, participants_target, questionnaire, markdown, description, project_img, tags} = cache.get('projects/'+$params.project_link);

    async function EditProject() {
        const response = await authorizedRequest('projects/'+$params.project_link+'/edit', 'PUT',
                {title, participants_target, questionnaire, markdown, description, project_img, tags});
    }

    let promise = getData('projects/' + $params.project_link);
</script>
{#await $promise}
    <h1>Загрузка...</h1>
{:then data}
    <ProjectPage {...data} on:update={EditProject}/>
    <ProjectMenu/>
    <Editor markdown={data.description} bind:description={description}/>
{/await}