<script>
    export let title = 'Влияние проходимого расстояния на здоровье';
    export let tags = ['Наука', 'Медицина'];
    export let progress = 42;
    export let author = "Камень Иванович";
    export let userImageSrc = "/images/user_images/user.jpg";
    export let projectImageSrc = "/images/project_images/Rectangle 4.png";
</script>

<div class="project-card">
    <img src="{projectImageSrc}" class="project-image" alt="project-image"/>
    <h2 class="project-title">{title}</h2>
    <div class="tags">
        {#each tags as tag}
            <a href="/" class="tag-href">{tag}</a>
        {/each}
    </div>
    <p class="percent-title">Собрано {progress}%</p>
    <div class="progress-bar horizontal">
        <div class="progress-track">
            <div class="progress-fill" style="--progress: {progress}%">
            </div>
        </div>
    </div>
    <div class="user">
        <img src="{userImageSrc}" class="user-img" alt="user-img"/>
        <p>{author}</p>
    </div>
</div>


<style>
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
        max-width: 20%;
        margin-right: 5%;
    }

    .horizontal .progress-track {
        position: relative;
        max-width: 80%;
        max-height: 5px;
        border-radius: 6px;
        background: #DADADA;
    }

    .horizontal .progress-fill {
        position: relative;
        background: #3d3434;
        height: 5px;
        border-radius: 6px;
        max-width: var(--progress);
        color: #fff;
    }

    .project-image {
        max-width: 350px;
        max-height: 268px;
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

    .project-card {
        display: flex;
        flex-direction: column;
        max-width: 20%;
        margin-right: 5%;
    }

    .horizontal .progress-track {
        position: relative;
        max-width: 80%;
        max-height: 5px;
        border-radius: 6px;
        background: #DADADA;
    }

    .horizontal .progress-fill {
        position: relative;
        background: #3d3434;
        height: 5px;
        border-radius: 6px;
        max-width: 42%;
        color: #fff;
    }

    .project-image {
        max-width: 350px;
        max-height: 268px;
    }

    li {
        list-style-type: none;
    }

    ul {
        padding: 0;
    }
</style>