<script>
    export let title = 'Влияние проходимого расстояния на здоровье';
    export let author = "Камень Иванович";
    export let projectImageSrc = "/images/project_images/follow_project_card.png";
</script>

<div class="project-card">
    <div class="img-wrapper">
        <img size="100%, 20%" src="{projectImageSrc}" class="img" alt="Картинка проекта">
    </div>

    <div class="title">
        <h2 class="project-title">{title}</h2>
    </div>

    <div class="user">
        <p>{author}</p>
    </div>
</div>


<style>

    .title {
        margin-top: 10%;
    }

    .img {
        object-fit: cover;
        height: 194px;
        width: 223px;

    }

    .img-wrapper {
        width: 100%;
        height: 60%;
        text-align: center;
        margin-bottom: 1%;
    }

    .project-title {
        font-size: calc(16px + (18 - 16) * ((100vw - 300px) / (1440 - 300)));
    }

    .project-card {
        font-family: "Helvetica Norm";
        display: flex;
        flex-direction: column;
        max-width: 223px;
        padding-right: 25px;
        padding-bottom: 2%;
    }

    .user {
        margin-top: 4%;
        display: flex;
        align-items: center;
    }

    .user p {
        --plain-font-size: calc(14px + (16 - 14) * ((100vw - 300px) / (1440 - 300)));
        text-align: center;;
    }

    .project-title {
        --plain-font-size: calc(24px + (32 - 24) * ((100vw - 300px) / (1440 - 300)));
        padding-top: 5%;
    }
</style>