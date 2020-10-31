<script>
    let user_name = "Даня";
    let user_surname = "Драгун";
    let tags = ['Медицина', 'Здоровье'];
    let about = '23 y.o. designer from San Francisco';
    let projects = ['Карта ночного неба', 'Влияние проходимого расстояния на здоровье'];

    let full_name = user_name + " " + user_surname;
</script>

<main>
    <div class = "return"> 
        <p class="arrow">→</p>
        <div class="chaif">Главная</div>
    </div>
    <div class = "profile">
        <div class="main-block">
                <h2 class="pr">Профиль</h2>
                <a href="/" class="edit">Редактировать</a>   
        </div> 
        <div class="user_info">
            <div class="user">
                <img src="/images/user_images/user.jpg" class="photo" alt="user_photo"/>
                <h2 class="title" id="name">{full_name}</h2>
            </div>
            <div class="self">
                <h2 class="title"> О себе:</h2>
                <p>{about}</p>
            </div>
            <div class="catigories">
                <h2 class="title">Предпочтения</h2>
                <div class="tags">
                </div>
            </div>
            <div clsaa="exexperience">
                <h2 class="title">Участие в проектах:</h2>
                <div class="exexperience-tags">
                    <li>
                        <ul><a href="/" class="ex-tag">Карта ночного неба</a></ul>
                        <ul><a href="/" class="ex-tag">Влияние проходимого расстояния на здоровье</a></ul>
                        <ul><a href="/" class="ex-tag">Облысение. Исследование</a></ul>
                        <ul><a href="/" class="ex-tag">Длительность жизни обуви</a></ul>
                    </li>
                </div>
            </div>
        </div>
        <div class="right-menu">
            <u><a href="/info">Информация</a></u>
            <a href="/info">Достижения</a>
        </div>
    </div>
</main>
<style>

    .right-menu a {
        color: #545454;
        font-family: "Helvetica Norm";
        font-size: 20px;
        display: flex;
        flex-direction: column;
        text-decoration: none;
    }

    #name {
        padding-top: 3%;
    }

    .title {
        font-size: 24px;
    }

    .profile {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
    }
    .return {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        margin-top: 2%;
        margin-bottom: 2%;
    }

    .pr {
        padding-bottom: 5%;
        font-size: 40px;
    }

    main {
        margin-left: 5%;
    }

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
        font-family: "Helvetica Norm";
        font-style: normal;
        font-weight: normal;
        line-height: 24px;
        display: flex;
        align-items: center;
        flex: none;
        order: 1;
        align-self: center;
        flex-grow: 0;
        margin: 16px 0px;
    }
    .edit {
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        margin-top: 15%;
        text-decoration-line: underline;
    }

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
        max-width: 10%;
    }  

    .exexperience-tags {
        margin-top: 2%;
    }
    .ex-tag {
        text-decoration: none;
    }

    .photo {
        width: 128px;
        height: 128px;
        border-radius: 50%;
        margin-bottom: 1%;
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

    @media (max-width: 768px) {

        main {
            width: 95%;
        }
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