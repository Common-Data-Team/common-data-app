<script>
import ProjectPage from '../_components/ProjectPage.svelte';
    import ProjectAbout from '../_components/ProjectAbout.svelte';
    import { params } from '@roxi/routify';
    import { getData } from '../../_api.js';

const promise = getData('projects/'+ $params.project_link);
</script>
{#await $promise}
    <h1>Загрузка...</h1>
{:then data}
<ProjectPage {...data}/>
<ProjectAbout description={data.description}/>
{/await}