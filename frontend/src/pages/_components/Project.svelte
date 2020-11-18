<script>
  export let title = 'Влияние проходимого расстояния на здоровье';
  export let tags = ['Наука', 'Медицина'];
  export let progress = 42;
  export let author = "Камень Иванович";
  export let userImageSrc = "/images/user_images/user.jpg";
  export let project_img = "/images/project_images/Rectangle 4.png";
  export let project_link = '';
</script>

<div class="project-card">
  <div class="img-wrapper">
    <img size="100%, 20%" src="{project_img}" class="img" alt="Картинка проекта">
  </div>
  <div class="title">
    <h2 class="project-title">{title}</h2>
  </div>
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
    <img src="{userImageSrc}" class="user-img" alt="Аватарка"/>
    <p>{author}</p>
  </div>
</div>


<style>

  .title {
    padding-top: 2%;
    max-height: 60px;
    padding-bottom: 1%;
  }

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

  .project-title {
    --plain-font-size: calc(24px + (32 - 24) * ((100vw - 300px) / (1440 - 300)));
    padding-top: 2%;
  }

</style>