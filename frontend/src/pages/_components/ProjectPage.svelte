<script>
    import { Textfield } from 'svelte-mui';
    import marked from 'marked';
    import Footer from './Footer.svelte';
    import Tag from './Tag.svelte';
    
    export let name = 'project_name';
    export let projectImageSrc = "/images/project_images/main_project.png";
    export let userImageSrc = "/images/user_images/user.jpg";
    export let author = "Камень Иванович";

    export let author_id = 123;
    export let user_id = 123;

    export let target = 5000;
    export let participants = 2500;

    export let tags = [
        {
            tag_name: 'Наука',
            tag_href: '/science'
        }
    ]

    let markdown = "# Example Title\n\n- this\n- is\n- a list\n\n![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)";
    let progress = participants / target * 100;
    
</script>

{#if author_id == user_id}
    <div class="project-block-content">
        <div class="project-description">
            <div class="img-wrapper">
                <img size="100%, 20%" src="{projectImageSrc}" class="img" alt="Картинка проекта">
            </div>
            <div class="text-description" >
                <Textfield
                    autocomplete="off"
                    label='Название проекта'
                    value={name}
                    bind:name
                />
                <Textfield
                    autocomplete="off"
                    label='Необходимое количество пользователей'
                    value={target}
                    type=number
                    bind:name
                />
            </div>
        </div>
    
        <div class='project-info'>
            <textarea bind:value={markdown} placeholder="Enter markdown here"/>
            <div class="preview">{@html marked(markdown)}</div>
        </div>
    
        <button class='take-part-btn'>Сохранить</button>
    </div>
{:else}
    <div class="project-block-content">
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
        <div class='project-info'>
            <div>{@html marked(markdown)}</div>
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
		width: 70%;
	}

	textarea {
		font-family: monospace, Roboto;
		height: 200px;
		border: none;
		margin: 0;
	}

	.preview {
		height: 75%;
		padding: 2rem;
		border-top: solid 2px #282828;
	}

	:global(body) {
		padding: 0;
	}
</style>