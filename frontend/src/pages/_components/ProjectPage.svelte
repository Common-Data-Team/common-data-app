<script>
    import { Textfield } from 'svelte-mui';
    import marked from 'marked';
    import Footer from './Footer.svelte';
    import Tag from './Tag.svelte';
    
    export let project_data = {
        project_id: 0,
        author_id: 0,
        title: 'Project_Name',
        projectImgSrc: "./images/project_images/main_project.png",
        project_description: "Какое-то значение",
        project_participants_count: 2500,
        project_participant_target: 5000,
        project_create_date: "08-11-2020",
        project_status: "active",
        project_page: "Project.svelte",
        project_markdown: "# Example Title\n\n- this\n- is\n- a list\n\n![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)",
        tags: [
            {
                tag_name: 'Наука',
                tag_href: '/science'
            }
        ]
    }

    export let user_data = {
        user_id: 0,
        user_name: "Камень Иванович",
        email: "kamen.ivanovich@gmail.com",
        about: "Я каменщик, работаю три дня",
        userImageSrc: "./images/user_images/user.jpg",
        user_projects_page: "/apps/user465_projects",
        user_profile_page: "/apps/user465",
        tags: [
            {
                tag_name: 'Наука',
                tag_href: '/science'
            }
        ],
        user_projects: [
            {
                project_id: 0
            }
        ],
        participant_projects: [
            {
                project_id: 0
            }
        ],
        followed_projects: [
            {
                project_id: 0
            }
        ]
    }

    let name = "project_data.title"
    let progress = project_data.project_participants_count / project_data.project_participant_target * 100;
    
</script>

{#if project_data.author_id == user_data.user_id}
    <div class="project-block-content">
        <div class="project-description">
            <div class="img-wrapper">
                <img size="100%, 20%" src="{project_data.projectImageSrc}" class="img" alt="Картинка проекта">
            </div>
            <div class="text-description" >
                <Textfield
                    autocomplete="off"
                    label='Название проекта'
                    value={project_data.title}
                    bind:name
                />
                <Textfield
                    autocomplete="off"
                    label='Необходимое количество пользователей'
                    value={project_data.target}
                    type=number
                    bind:name
                />
            </div>
        </div>
    
        <div class='project-info'>
            <textarea bind:value={project_data.project_markdown} placeholder="Enter markdown here"/>
            <div class="preview">{@html marked(project_data.project_markdown)}</div>
        </div>
    
        <button class='take-part-btn'>Сохранить</button>
    </div>
{:else}
    <div class="project-block-content">
        <div class="project-description">
            <div class="img-wrapper">
                <img size="100%, 20%" src="{project_data.projectImageSrc}" class="img" alt="Картинка проекта">
            </div>
            <div class="text-description" >
                <h2>{name}</h2>
                <div class="bar">
                    <div class="progress" style="width: {progress}%"></div>
                </div>
                <p><strong>{project_data.project_participants_count}</strong> человек приняло участие</p>
                <p class="target">из {project_data.project_participant_target} запрошенных</p>
                <div class="tag-container">
                    <div class="tags">
                        {#each project_data.tags as tag}
                            <Tag {...tag}></Tag>
                        {/each}
                    </div>
                </div>
                <div class="user">
                    <img src="{user_data.userImageSrc}" class="user-img" alt="Аватарка"/>
                    <p>{user_data.user_name}</p>
                </div>
                <button class='take-part-btn'>Принять участие</button>
            </div>
        </div> 
        <div class='project-info'>
            <div>{@html marked(project_data.project_markdown)}</div>
        </div>
    </div>
{/if}

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

    .project-block-content {
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
    }

    .project-info {
        max-width: 100%;
        display: flex;
        margin-top: 5%;
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

    textarea, .preview {
		box-sizing: border-box;
		display: block;
	}

	textarea {
        width: 30%;
		font-family: monospace, Roboto;
		height: 500px;
		border: none;
		margin: 0;
	}

	.preview {
        width: 65%;
		height: 75%;
		padding: 2rem;
	}

	:global(body) {
		padding: 0;
	}
</style>