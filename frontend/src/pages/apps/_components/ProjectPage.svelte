<script>
    export let title, participants_target, creation_date, participants_count, project_img, tags, leaders;
</script>

<main>
<img src={project_img} alt="project_img" class="project_img">
<div class="info_block">
<h1 class="title">{title}</h1>
<div class="bar">
        <div class="progress" style="width: {participants_count}%"></div>
</div>
<p class="progress_title">{participants_count} человек приняло участие</p>
<p class="target_title">из {participants_target} запрошенных</p>
<div class="tags_block">
    {#each tags as tag}
        <div class="tag"><p>{tag.name}</p></div>
    {/each}
</div>
<div class="leader_block">
<img src={leaders[0].user.avatar} alt="leader_ava">
<p>{leaders[0].user.fio}</p>
</div>
<p class="date">{creation_date.slice(8, 10)}.{creation_date.slice(5, 7)} - ???</p>
<p class="date_title">время сбора</p>
<button class="enter_button">Принять участие</button>
<div class="subscribe_block">
<img src='/images/button_images/Subscribe.svg' alt="">
<p>Подписаться на обновления</p>
</div>
</div>
</main>
<style>
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
    .tags_block {
        display: flex;
        flex-wrap: wrap;
        margin: 30px 10px 0 0;
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
    .leader_block {
        display: flex;
        align-items: center;
        margin: 20px 0 0 0;
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
</style>