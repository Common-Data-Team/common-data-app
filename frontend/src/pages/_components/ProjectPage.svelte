<script>
    import Footer from './Footer.svelte';
    import Tag from './Tag.svelte';
    
    export let name = 'project_name';
    export let projectImageSrc = "/images/project_images/main_project.png";
    export let userImageSrc = "/images/user_images/user.jpg";
    export let author = "Камень Иванович";

    export let target = 5000;
    export let participants = 2500;

    export let tags = [
        {
            tag_name: 'Наука',
            tag_href: '/science'
        }
    ]

    let progress = participants / target * 100;
    
</script>

<div class="project-description">
    <div class="img-wrapper">
        <img size="100%, 20%" src="{projectImageSrc}" class="img" alt="Картинка проекта">
    </div>
    <div class="text-description" >
        <h2>{name}</h2>
        <div class="bar">
            <div class="progress" style="width: {progress}%"></div>
        </div>
        <p><strong>{participants}</strong> человек приняло участие</p>
        <p class="target">из {target} запрошенных</p>
        <div class="tag-container">
            <div class="tags">
                {#each tags as tag}
                    <Tag {...tag}></Tag>
                {/each}
            </div>
        </div>
        <div class="user">
            <img src="{userImageSrc}" class="user-img" alt="Аватарка"/>
            <p>{author}</p>
        </div>
        <button class='take-part-btn'>Принять участие</button>
    </div>
</div>

<Footer></Footer>

<style>

    .take-part-btn {
        margin-top: 5%;
        width: 274px;
        height: 50px;
        font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
        background: #282828;
    }

    .tag-container {
        margin-top: 5%;
        max-width: 70%;
        text-align: left;
    }
    .user-img {
        width: 36px;
        height: 36px;
        border-radius: 50%;
    } 

    .user {
        margin-top: 3%;
        display: flex;
        align-items: center;
    }

    .user p {
        --plain-font-size: calc(14px + (16 - 14) * ((100vw - 300px) / (1440 - 300)));
        text-align: center;
        margin-left: 2%;
    }
    .text-description {
        width: 30%;
        margin-left: 5%;
    }

    .tags {
        display: flex;
        justify-content: left;
        align-items: left;
        flex-wrap: wrap;
    }

    .target {
        font-size: calc(14px + (16 - 14) * ((100vw - 300px) / (1440 - 300)))
    }

    .project-description {
        display: flex;
        margin-left: 5%;
    }

    .img-wrapper {
        text-align: center;
    }

    .img {
        max-height: 629px;
        max-width: 428px;
    }

    .bar {
        width: 80%;
        height: 6px;
        margin-top: 2%;
        margin-bottom: 2%;
        background: #9B9B9B;
    }

    .progress {
        background: black;
        height: 6px;
    }
</style>