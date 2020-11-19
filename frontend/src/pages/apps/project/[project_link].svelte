<script>
    import ProjectPage from '../_components/ProjectPage.svelte';
    import { onMount, getContext } from 'svelte';
    import { params } from '@roxi/routify';
    let apiUrl = getContext('apiUrl');
    async function getData() {
       const response = await fetch(apiUrl+'projects/' + $params.project_link).then(res => res.json());
       console.log(response);
        if (response.project_img === null) response.project_img = '/images/project_images/main_project.png';
        if (response.leaders[0].user.avatar === null) response.leaders[0].user.avatar = '/images/user_images/user.jpg';
       return response;
    }
</script>
{#await getData()}
    <h1>Загрузка...</h1>
{:then data}
<ProjectPage {...data}/>
{/await}