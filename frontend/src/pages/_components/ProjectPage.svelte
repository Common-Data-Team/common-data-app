<script>
    import Footer from './Footer.svelte';
    
    export let name = 'project_name';
    export let projectImageSrc = "./images/project_images/follow_project_card.png";

    export let target = 5000;
    export let participants = 2500;

    let progress = participants / target * 100;
    
</script>

<div class="project-description">
    <img href={projectImageSrc} alt="Картинка проекта" />
    <div class="text-description" >
        <div class="bar">
            <div class="progress" style="width: {progress}%"></div>
        </div>
    </div>
</div>

<Footer></Footer>

<style>
    .bar {
        width: 80%;
        height: 6px;
        background: #9B9B9B;
    }

    .progress {
        background: black;
        height: 6px;
    }
</style>