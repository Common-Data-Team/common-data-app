<script>
    export let title, participants_target, creation_date, participants_count, project_img, leaders;
    let tags = [{name: 'Технологии'}, {name: 'Здоровье'}];
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
</div>
</main>
<style>
    main {
        margin: 20px 0 0 0;
        width: 100%;
        display: flex;
    }
    .project_img {
        margin: 0 50px 0 3%;
        width: 600px;
    }
    .info_block {
        display: flex;
        flex-direction: column;
        min-width: 300px;
    }
    .title {
        font-style: normal;
        font-weight: bold;
        font-size: 32px;
        margin: 5px 0;
    }
    .bar {
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
        margin: 30px 10px 0 0;
    }
    .tag {
        background-color: #282828;
        border-radius: 18px;
        text-align: center;
        padding: 0.375em 0.75em;
        margin: 0 10px 0 0;
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
</style>