<script>
 
</script>

<main>
    <div id="project-card">
        <img src="/images/project_images/Rectangle 4.png" class="project-image" alt="project-image" />
    </div>
</main>

<footer>
    <div class="flex">
    <img src="white_logo.svg" class="logo-white" alt="logo-white" />
    <div class="column-block">
        <h3>О НАС</h3>
        <ul>
            <a href="vk.com"><li>проектам</li></a>
            <a href="vk.com"><li>пользователям</li></a>
        </ul>
    </div>
    <div class="column-block">
        <h3>СВЯЗАТЬСЯ С НАМИ</h3>
        <ul>
            <a href="vk.com"><li>help@commondata.ru</li></a>
            <a href="vk.com"><li>+7 (901) 723-04-47</li></a>
        </ul>
    </div>
    <div class="column-block">
        <h3>СОЦСЕТИ</h3>
        <ul>
            <a href="vk.com"><li>facebook</li></a>
            <a href="vk.com"><li>telegram</li></a>
            <a href="vk.com"><li>vkontakte</li></a>
        </ul>
    </div>
    </div>
</footer>

<style>
    footer {
        position: absolute;
        bottom: 0;
        width: 100%;
        padding: 30px 0;
        margin-top: 100%;
        background: #282828;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }

    .flex {
        display: -ms-flexbox;	
        display: -webkit-flex;	
        display: -webkit-box;	
        display: flex;
        -ms-flex-pack: justify;	
        -webkit-justify-content: space-between;
        -webkit-box-pack: justify;	
        justify-content: space-between;
    }
    
    .logo-white {
        flex: 1 1 0%;
        max-width: 20%;
        padding-left: 5%;
        padding-right: 15%;
    }

    a {
        color: #BDBDBD;
        font-family: "Helvetica Norm";
        --plain-font-size: calc(12px + (14 - 12) * ((100vw - 300px) / (1440 - 300)));
        text-decoration: none;
    }

    a:hover { 
        color: #1355FF;
    }

    .column-block {
        flex: 1 1 0%;
        max-width: 20%;
        padding-left: 5%;
        padding-right: 5%;
    }

    h3 {
        color: #F9F9F9;
        --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
        font-family: "Helvetica Neue";
    }

    li {
        list-style-type: none;
    }

    ul {
        padding: 0;
    }

    @media (max-width: 768px) {
        .flex {
            flex-direction: column;
        }
    }

</style>