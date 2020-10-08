<script>

</script>

<main>
    <div class = "return"> 
        <p class="arrow">→</p>
        <div class="chaif">Главная</div>
    </div>
    <div class = "profile">
        <div class="main-block">
                <h1 class="pr">Профиль</h1>
                <a href="/" class="edit"><br>Редактировать</a>   
        </div> 
        <div class="user_info">
            <div class="user">
                <img src="/" class="photo" alt="user_photo"/>
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
                    <a href="/" class="ex-tag">Карта ночного неба</a>
                    <p><a href="/" class="ex-tag"><br>Влияние проходимого расстояния на здоровье</a></p>
                    <p><a href="/" class="ex-tag"><br>Облысение. Исследование</a></p>
                    <p><a href="/" class="ex-tag"><br>Длительность жизни обуви</a></p>
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
        align-items:flex-start;
    }
    /*main_block*/
    /*Привет пздц*/
    .arrow {
        order: 1;
        width: 37px;
        height: 38px;
        left: 37px;
        top: 38px;

        font-family: SF Pro Display;
        font-style: normal;
        font-weight: 300;
        font-size: 32px;
        line-height: 38px;
        text-align: center;

        color: #000000;

        transform: rotate(-180deg);

        /* Inside Auto Layout */
        flex: none;
        order: 0;
        align-self: center;
        flex-grow: 0;
        margin: 16px 0px;
    }
    .chaif {
        position: static;
        width: 77px;
        height: 24px;
        left: 53px;
        top: 7px;

        /* just text */
        font-family: Helvetica Neue;
        font-style: normal;
        font-weight: normal;
        font-size: 20px;
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
        position: absolute;
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        line-height: 19px;
        text-decoration-line: underline;
    }
    /*user-info*/
    .user_info {
        display: flex;
        flex-direction: column;
        margin-right: 15% ;
        margin-left: 25%;
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
        font-size: 120%
    }
    .exexperience-tags {
        margin-top: 3%;
    }
    .ex-tag {
        text-decoration: none;
        font-size: 20px;
        line-height: 24px;
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

</style>