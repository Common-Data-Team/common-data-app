<script>
    export let title = 'Влияние проходимого расстояния на здоровье';
    export let tags = ['Наука', 'Медицина'];
    export let author = "Камень Иванович";
    export let description = "В ходе нового исследования специалисты из Университета Эдинбурга выяснили, что причина облысения заложена в генах, причём тех, что передаются по материнской линии.";
    export let userImageSrc = "/images/user_images/user.jpg";
    export let projectImageSrc = "/images/project_images/follow_project_card.png";
</script>

<div class="project-card">
    <div class="img-wrapper">
        <img size="100%, 20%" src="{projectImageSrc}" class="img" alt="Картинка проекта">
    </div>

    <div class="tags">
        {#each tags as tag}
            <a href="/" class="tag-href">{tag}</a>
        {/each}
    </div>
    <div class="title">
        <h2 class="project-title">{title}</h2>
    </div>

    <div class="project-description">
        <p class="project-description">{description}</p>
    </div>

    <div class="user">
        <img src="{userImageSrc}" class="user-img" alt="Аватарка"/>
        <p>{author}</p>
    </div>
</div>


<style>

    .title {
        padding-top: 1%;
    }

    .img {
        object-fit: cover;
        height: 375px;
        width: 600px;

    }

    .img-wrapper {
        width: 100%;
        height: 60%;
        text-align: center;
        margin-bottom: 3%;
    }

    .project-description {
        margin-top: 1%;
    }

    .project-title {
        --plain-font-size: calc(24px + (32 - 24) * ((100vw - 300px) / (1440 - 300)));
    }

    .project-card {
        display: flex;
        flex-direction: column;
        max-width: 600px;
        padding-right: 25px;
        padding-bottom: 5%;
    }

    .user-img {
        width: 36px;
        height: 36px;
        border-radius: 50%;
    }

    a {
        color: #BDBDBD;
        font-family: "Helvetica Norm";
        --plain-font-size: calc(12px + (14 - 12) * ((100vw - 300px) / (1440 - 300)));
        text-decoration: none;
    }

    .tags {
        display: flex;
    }

    .user {
        margin-top: 4%;
        display: flex;
        align-items: center;
    }

    .user p {
        --plain-font-size: calc(14px + (16 - 14) * ((100vw - 300px) / (1440 - 300)));
        text-align: center;
        margin-left: 2%;
    }

    .user-img {
        width: 36px;
        height: 36px;
        border-radius: 50%;
    }

    .tag-href {
        background-color: #282828;
        border-radius: 18px;
        text-align: center;
        padding: 0.375em 0.75em;
        margin: 1%;
        margin-right: 2%;
        margin-left: 0%;
        color: #F9F9F9;
    }

    .tag-href:hover {
        background-color: #1355FF;
        color: #F9F9F9;
    }

    a:hover {
        color: #1355FF;
    }

    .project-title {
        --plain-font-size: calc(24px + (32 - 24) * ((100vw - 300px) / (1440 - 300)));
        padding-top: 2%;
    }
    
</style>