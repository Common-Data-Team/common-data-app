<script>

</script>

<main>
    <div class = "return"> 
        <p class="arrow">→</p>
        <div class="chaif">Главная</div>
    </div>
    <div class = "profile">
        <div class="main-block">
                <h2 class="pr">Профиль</h2>
                <a href="/" class="edit"><br>Редактировать</a>   
        </div> 
        <div class="user_info">
            <div class="user">
                <img src="/images/user_images/user.jpg" class="photo" alt="user_photo"/>
                <h2 class="title"> Даня Драгун </h2>
            </div>
            <div class="self">
                <h2 class="title"> О себе </h2>
                <p> 23 y.o. designer from San Francisco </p>
            </div>
            <div class="catigories">
                <h2 class="title">Предпочтения</h2>
                <div class="tags">
                    <p class="tag-href">Медицина<a href="/"class="close">&times;</a></p>
                    <p class="tag-href">Наука<a href="/" class="close">&times;</a></p>
                    <p  class="tag-href">Бытовое <a href="/" class="close">&times;</a> </p>
                </div>
            </div>
            <div clsaa="exexperience">
                <h2 class="title">Участие в проектах:</h2>
                <div class="exexperience-tags">
                    <li>
                        <ul><a href="/" class="ex-tag">Карта ночного неба</a></ul>
                        <ul><a href="/" class="ex-tag"><br>Влияние проходимого расстояния на здоровье</a></ul>
                        <ul><a href="/" class="ex-tag"><br>Облысение. Исследование</a></ul>
                        <ul><a href="/" class="ex-tag"><br>Длительность жизни обуви</a></ul>
                    </li>
                </div>
            </div>
        </div>
        <!--
        <div class="sections">
            <a href="/" class="sec-teg"><p>Информация</p></a>
            <a href="/" class="sec-teg"><p>Достижения</p></a>
        </div>
        -->
    </div>
</main>
<style>
    .profile {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
    }
    .return {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
    }
    /*main_block*/
    /*Привет пздц*/
    .arrow{ 

        font-family: "SF Pro Display";
        font-size: 32px;
        text-align: center;

        color: #282828;
        transform: rotate(-180deg);
        align-self: center;
        margin-right: 2%;
    }

    .chaif {
        position: static;
        width: 77px;
        height: 24px;
        left: 53px;
        top: 7px;

        /* just text */
        font-family: "Helvetica Norm";
        font-style: normal;
        font-weight: normal;
        --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
        line-height: 24px;
        /* identical to box height */
        display: flex;
        align-items: center;

        /* Inside Auto Layout */
        flex: none;
        order: 1;
        align-self: center;
        flex-grow: 0;
        margin: 16px 0px;
    }
    .edit {
        font-style: normal;
        font-weight: normal;
        --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
        line-height: 19px;
        text-decoration-line: underline;
    }
    /*user-info*/
    .user_info {
        display: flex;
        flex-direction: column;
        margin-right: 15% ;
        margin-left: 15%;
    }

    .user {
        margin-bottom: 10%;
    }
    .self {
        margin-bottom: 10%;
    }
    .catigories {
        margin-bottom: 10%;
    }
    .tags {
        display: flex;
        align-items: center;
        margin-top: 3%;
    }  
    .close {
        margin-left: 4px;
        color: #F9F9F9;
        text-decoration: none;
        text-align: center;
    }
    .tag-href {
        background-color: #282828;
        border-radius: 20px;
        text-align: center;
        padding: 0.5em 0.5em;
        margin-right: 2%;
        margin-left: 0%;
        color: #F9F9F9;
    }
    .exexperience-tags {
        margin-top: 2%;
    }
    .ex-tag {
        text-decoration: none;
        --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
    }

    .photo {
        width: 128px;
        height: 128px;
        border-radius: 50%;
        margin-bottom: 5%;
    }

    li {
        list-style-type: none;
        margin-bottom: 30%;
    }

    ul {
        padding: 0;
        margin-block-start: 0em;
        margin-block-end: 0em;
        padding: 0;
        margin: 0;
        padding-inline-start: 0px;
    }

    /*
    .sections {
        display:flex;
        flex-direction: column;
    }
    .sec-teg {
        margin-top: 5%;
        text-decoration: none;
        font-size: 16px;
        line-height: 19px;
        color: #545454;
    }
    */

    @media (max-width: 768px) {
        .profile {
            flex-direction: column;
        }

        .user_info {
            margin-right: 0%;
            margin-left: 0%;
            max-width: 90%;
            margin-top: 5%;
        }
    }

</style>