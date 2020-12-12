<script>
  import { goto } from '@roxi/routify'
  import Tags from '../apps/_components/Tags.svelte'
  export let title = 'Влияние проходимого расстояния на здоровье';
  export let tags = ['Наука', 'Медицина'];
  export let participants_count = 42;
  export let leaders = [];
  export let userImageSrc = "/images/user_images/default.jpg";
  export let project_img = "/images/project_images/Rectangle 4.png";
  export let project_link = '';
</script>

<div class="project-card">
  <div class="img-wrapper" on:click={$goto('apps/project/'+project_link)}>
    <img size="100%, 20%" src="/{project_img}.png" class="img" alt="Картинка проекта">
  </div>
  <div class="title" on:click={$goto('apps/project/'+project_link)}>
    <h2 class="project-title">{title}</h2>
  </div>
  <Tags {tags}/>
  <p class="percent-title">Собрано {participants_count}%</p>

  <div class="bar">
    <div class="progress" style="width: {participants_count}%"></div>
  </div>

  <div class="user" on:click={$goto('apps/user/'+leaders[0].user.id)}>
    <img src="/{leaders[0].user.avatar}.jpg" class="user-img" alt="Аватарка"/>
    <p>{leaders[0].user.fio}</p>
  </div>
</div>


<style>

  .title {
    max-height: 60px;
    padding: 6px 0 0 0;
  }

  .img {
    max-height: 100%;
    width: 100%;
    object-fit: cover;
  }

  .img-wrapper {
    width: 100%;
    height: 60%;
    text-align: center;
  }

  .bar {
    width: 80%;
    height: 4px;
    background: #9B9B9B;
  }

  .progress {
    background: black;
    height: 4px;
  }

  .project-title {
    --plain-font-size: calc(24px + (32 - 24) * ((100vw - 300px) / (1440 - 300)));
  }

  .project-card {
    display: flex;
    flex-direction: column;
    width: 350px;
    padding-right: 25px;
    padding-bottom: 5%;
  }
  .title:hover, .img-wrapper:hover, .user:hover {
    cursor: pointer;
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
    padding: 0.375em 0.75em;
    margin: 4px 2% 10px 0;
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
    margin: 5px 0 0 0;
  }

  .project-title {
    --plain-font-size: calc(24px + (32 - 24) * ((100vw - 300px) / (1440 - 300)));
    padding-top: 2%;
  }

</style>