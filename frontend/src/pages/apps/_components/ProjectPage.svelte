<script>
  import {onMount, createEventDispatcher} from 'svelte';
  import {getCookie, dataStore, apiUrl} from '../../_api.js';
  import {fade} from 'svelte/transition';
  import {goto, url} from '@roxi/routify'
  import {Menu, Menuitem} from 'svelte-mui';
  import Tags from './Tags.svelte'

  export let title, participants_target, creation_date, participants_count, project_img, tags, leaders;
  let auth = false;
  export let edit = false;
  onMount(async () => {
    leaders.forEach(leader => {
      if (getCookie('user_id') === leader.user.id + '') auth = true;
    });
    console.log(tags);
  });
  const dispatch = createEventDispatcher();
</script>

<main>
  <div class="project_img">
  <img src={'/'+project_img+'.png'} alt="project_img">
  </div>
  <div class="info_block">
    {#if edit}
      <input class="title" bind:value={$dataStore.title} in:fade>
    {:else}
      <h1 class="title">{$dataStore.title}</h1>
    {/if}
    <div class="bar">
      <div class="progress" style="width: {participants_count}%"></div>
    </div>
    <p class="progress_title">{participants_count} человек приняло участие</p>
    <p class="target_title">из
      {#if edit}<input type="number" class="target_title input_target" bind:value={$dataStore.participants_target}
                       in:fade>{:else}{$dataStore.participants_target}{/if} запрошенных</p>
    <Tags {edit} {tags}/>
    <div class="leader_block" on:click={() => $goto("../../user/"+leaders[0].user.id)}>
      <img src={'/'+leaders[0].user.avatar+'.jpg'} alt="leader_ava">
      <p>{leaders[0].user.fio}</p>
    </div>
    <p class="date">{creation_date.slice(8, 10)}.{creation_date.slice(5, 7)} - ???</p>
    <p class="date_title">время сбора</p>
<!--    <a href='./forms/render' class="enter_button">Принять участие</a>-->
    <button disabled={edit} on:click={() => $goto('./forms/render')} class="enter_button">Принять участие</button>
    <div class="subscribe_block">
      <img src='/images/button_images/subscribe.svg' alt="">
      <p>Подписаться на обновления</p>
    </div>
    <div class="edit_block">
    {#if auth}
      {#if edit}
        <a on:click="{() => {edit = false; dispatch('update')}}" class="edit">Сохранить</a>
      {:else}
        <a on:click={() => edit = true} class="edit">Редактировать</a>
      {/if}
        <a href={$url("./forms/editor")} class="edit">Изменить форму</a>
    {/if}
    </div>
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
    margin: 0 30px 0 3%;
  }

  .project_img img {
    object-fit: cover;
    width: 800px;
  }

  .info_block {
    display: flex;
    flex-direction: column;
    max-width: 350px;
    padding: 0 10px 0 0;
  }

  .title {
    font-style: normal;
    font-weight: bold;
    font-size: 32px;
    margin: 5px 0;
  }

  .bar {
    min-width: 200px;
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
    font-family: "Helvetica Neue";
  }

  .leader_block {
    display: flex;
    align-items: center;
    margin: 15px 0 0 0;
  }

  .leader_block:hover {
    cursor: pointer;
  }

  .leader_block img {
    width: 37px;
    height: 37px;
    border-radius: 37px;
    margin: 0 10px 0 0;
    border: 1px solid #E0E0E0;
  }

  .leader_block p {
    margin: 0;
    font-size: 18px;
    line-height: 19px;
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
    font-weight: 300;
    font-size: 20px;
    line-height: 24px;
    width: 300px;
    min-width: 200px;
    margin: 30px 0 0 0;
    transition: all ease 0.7s;
  }

  .enter_button:disabled {
    background: #444444;
    color: #bbbbbb;
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
  .edit_block {
    display: flex;
  }
  .edit {
    font-style: normal;
    font-weight: normal;
    font-size: 16px;
    text-decoration-line: underline;
    margin: 10px 20px 0 0;
  }

  .edit:hover {
    cursor: pointer;
  }
  @media (max-width: 1000px) {
    main {
      flex-direction: column;
    }
    .project_img img{
    min-width: 250px;
    width: 100%;
    height: auto;
    max-width: 500px;
  }
  .info_block {
    width: 100%;
    padding: 0 15px 0 3%;
    margin: 0;
  }

  }
</style>