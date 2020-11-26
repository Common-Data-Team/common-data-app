<script>
    import { onMount, createEventDispatcher } from 'svelte';
    import { getCookie, dataStore } from '../../_api.js';
    import { fade } from 'svelte/transition';
    export let title, participants_target, creation_date, participants_count, project_img, tags, leaders;
    let auth = false;
    export let edit = false;
    console.log(project_img);
    onMount(() => {
        console.log(leaders);
        leaders.forEach(leader => {
            if (getCookie('user_id') === leader.user.id+'') auth = true;
        });
    });

    const dispatch = createEventDispatcher();
</script>

<main>
<img src={'/'+project_img+'.png'} alt="project_img" class="project_img">
<div class="info_block">
    {#if edit}
    <input class="title" bind:value={title} on:keyup={() => $dataStore.title = title} in:fade>
        {:else}
    <h1 class="title">{title}</h1>
        {/if}
<div class="bar">
        <div class="progress" style="width: {participants_count}%"></div>
</div>
<p class="progress_title">{participants_count} человек приняло участие</p>
<p class="target_title">из {#if edit}<input class="target_title input_target" bind:value={participants_target} in:fade on:keyup={() => $dataStore.participants_target = participants_target}>{:else}{participants_target}{/if} запрошенных</p>
<div class="tags_block">
    {#if edit}
        <div class="tag" in:fade><p>Добавить тэг</p></div>
    {:else}
        {#if tags.length === 0}
            <div class="tag"><p>Тэгов нет</p></div>
        {/if}
    {/if}
    {#each tags as tag, ind}
        <div class="tag">
                <p>{tag.name}</p>
        </div>
    {/each}
</div>
<div class="leader_block">
<img src={'/'+leaders[0].user.avatar+'.jpg'} alt="leader_ava">
<p>{leaders[0].user.fio}</p>
</div>
<p class="date">{creation_date.slice(8, 10)}.{creation_date.slice(5, 7)} - ???</p>
<p class="date_title">время сбора</p>
<button class="enter_button">Принять участие</button>
<div class="subscribe_block">
<img src='/images/button_images/subscribe.svg' alt="">
<p>Подписаться на обновления</p>
</div>
{#if auth}
    {#if edit}
    <a on:click="{() => {edit = false; dispatch('update')}}" class="edit">Сохранить</a>
    {:else}
    <a on:click={() => edit = true} class="edit">Редактировать</a>
    {/if}
{/if}
</div>
</main>
<style>
    input {
        background: transparent;
		border: 2px solid #000000;
		border-radius: 5px;
    }
    main {
        width: 100%;
        display: flex;
        margin: 20px 0 0 0;
    }
    p, h1 {
        color: #282828;
    }
    .project_img {
        margin: 0 50px 0 3%;
        width: auto;
        object-fit: cover;
    }
    .info_block {
        display: flex;
        flex-direction: column;
        max-width: 350px;
        margin: 0 50px 0 0;
    }
    .title {
        font-style: normal;
        font-weight: bold;
        font-size: 32px;
        margin: 5px 0;
    }
    .bar {
        min-width: 300px;
        width: 100%;
        height: 4px;
        background: #9B9B9B;
        margin: 10px 0;
    }
    .progress {
        background: #000000;
        height: 4px;
    }
    .progress_title {
        font-style: normal;
        font-weight: 500;
        font-size: 18px;
        line-height: 24px;
    }
    .target_title {
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 19px;
    }
    .input_target {
        width: 40px;
    }
    .tags_block {
        display: flex;
        flex-wrap: wrap;
        margin: 15px 10px 0 0;
    }
    .tag {
        background-color: #282828;
        border-radius: 18px;
        text-align: center;
        padding: 0.375em 0.75em;
        margin: 0 10px 5px 0;
        text-decoration: none;
    }
    .tag p {
        color: #F9F9F9;
        font-style: normal;
        font-weight: 300;
        font-size: 14px;
        line-height: 17px;
    }
    .input_tag {
        text-align: center;
        min-width: 100px;
        color: #FFFFFF;
        border: 0;
    }
    .leader_block {
        display: flex;
        align-items: center;
        margin: 15px 0 0 0;
    }
    .leader_block img {
        width: 37px;
        height: 37px;
        border-radius: 37px;
        margin: 0 30px 0 0;
        border: 1px solid #E0E0E0;
    }
    .date {
        font-weight: 400;
        font-size: 24px;
        line-height: 29px;
        margin: 20px 0 0 0;
    }
    .date_title {
        font-weight: 400;
        font-size: 16px;
        line-height: 19px;
    }
    .enter_button {
        background-color: #282828;
        padding: 12px 71px;
        font-weight: 300;
        font-size: 20px;
        line-height: 24px;
        width: 300px;
        margin: 30px 0 0 0;
    }
    .subscribe_block {
        display: flex;
        align-items: center;
        margin: 20px 0 0 0;
    }
    .subscribe_block:hover {
        cursor: pointer;
    }
    .subscribe_block p {
        font-weight: normal;
        font-size: 18px;
        line-height: 24px;
        margin: 0 0 0 20px;
    }
    .edit {
    font-style: normal;
    font-weight: normal;
    font-size: 16px;
    text-decoration-line: underline;
    margin: 10px 0 0 0;
  }
    .edit:hover {
        cursor: pointer;
    }
</style>