<script>
    export let title = 'Влияние проходимого расстояния на здоровье';
    export let tags = ['Наука', 'Медицина'];
    export let progress = 42;
    export let author = "Камень Иванович";
    export let userImageSrc = "/images/user_images/user.jpg";
    export let projectImageSrc = "/images/project_images/Rectangle 4.png";
</script>

<div class="project-card">
    <div class="img-wrapper">
        <img size="100%, 20%" src="{projectImageSrc}" class="img" alt="project-image">
    </div>
    <h2 class="project-title">{title}</h2>
    <div class="tags">
        {#each tags as tag}
            <a href="/" class="tag-href">{tag}</a>
        {/each}
    </div>
    <p class="percent-title">Собрано {progress}%</p>

    <div class="bar">
        <div class="progress" style="width: {progress}%"></div>
    </div>

    <div class="user">
        <img src="{userImageSrc}" class="user-img" alt="user-img"/>
        <p>{author}</p>
    </div>
</div>


<style>
    .img {
        max-height: 100%;
        max-width: 100%;
    }

    .img-wrapper {
        width: 100%;
        height: 60%;
        text-align: center;
    }

    .bar {
        width: 100%;
        height: 3px;
        background: #9B9B9B;
    }

    .progress {
        background: black;
        height: 3px;
    }

    .project-title {
        --plain-font-size: calc(24px + (32 - 24) * ((100vw - 300px) / (1440 - 300)));
        padding-top: 2%;
    }

    .tag-href {
        background-color: #282828;
        border-radius: 18px;
        text-align: center;
        padding: 0.6em 0.6em;
        margin: 5%;
        margin-right: 2%;
        margin-left: 0%;
        color: #F9F9F9;
    }

    .tag-href:hover {
        background-color: #1355FF;
        color: #F9F9F9;
    }

    .project-card {
        display: flex;
        flex-direction: column;
        width: 300px;
        margin: 0 10px;
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
        margin-top: 5%;
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
        padding: 0.6em 0.6em;
        margin: 5%;
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

    .percent-title {
        --plain-font-size: calc(12px + (14 - 12) * ((100vw - 300px) / (1440 - 300)));
        padding-bottom: 2%;
    }

    h3 {
        color: #F9F9F9;
        --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
        font-family: "Helvetica Neue";
    }

    .project-title {
        --plain-font-size: calc(24px + (32 - 24) * ((100vw - 300px) / (1440 - 300)));
        padding-top: 2%;
    }

    li {
        list-style-type: none;
    }

    ul {
        padding: 0;
    }
</style>