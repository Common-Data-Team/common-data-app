<script>
    export let user_name = "Даня";
    export let user_surname = "Драгун";
    export let user_avatar_link = "/images/user_images/user.jpg";
    export let tags = [
        {
            tag_name: "Здоровье",
            tag_href: "/health"
        },
        {
            tag_name: "Наука",
            tag_href: "/health"
        },
        {
            tag_name: "Здоровье",
            tag_href: "/health"
        },
        {
            tag_name: "Здоровье",
            tag_href: "/health"
        },
        {
            tag_name: "Здоровье",
            tag_href: "/health"
        },
        {
            tag_name: "Здоровье",
            tag_href: "/health"
        },
        {
            tag_name: "Здоровье",
            tag_href: "/health"
        }
    ];
    export let about = '23 y.o. designer from San Francisco';
    export let projects = [
        {
            title: "Карта ночного неба",
            project_href: "/project325"
        },
        {
            title: "Влияние проходимого расстояния на здоровье",
            project_href: "/project"
        }
    ]

    let full_name = user_name + " " + user_surname;
</script>

<main>
    <a href="/" class="return-link">
        <div class = "return"> 
            <p class="arrow">→</p>
            <div class="chaif">Главная</div>
        </div>
    </a>
    <div class = "profile">
        <div class="main-block">
                <h2 class="pr">Профиль</h2>
                <a href="/" class="edit">Редактировать</a>   
        </div> 
        <div class="user_info">
            <div class="user">
                <img src={user_avatar_link} class="photo" alt="user_photo"/>
                <h2 class="title" id="name">{full_name}</h2>
            </div>
            <div class="self">
                <h2 class="title"> О себе:</h2>
                <p>{about}</p>
            </div>
            <div class="catigories">
                <h2 class="title">Предпочтения</h2>
                <div class="tag-container">
                    <div class="tags">
                        {#each tags as tag}
                            <a href={tag.tag_href} class="tag-href">{tag.tag_name}</a>
                        {/each}
                    </div>
                </div>
            </div>
            <div clsaa="exexperience">
                <h2 class="title">Участие в проектах:</h2>
                <div class="exexperience-tags">
                    <li>
                        {#each projects as project}
                            <ul><a href={project.project_href} class="ex-tag">{project.title}</a></ul>
                        {/each}
                    </li>
                </div>
            </div>
        </div>
        <div class="right-menu">
            <u><a href="/apps/profile_info">Информация</a></u>
            <a href="/info">Достижения</a>
        </div>
    </div>
</main>
<style>

    .tag-container {
        margin-top: 2%;
        max-width: 70%;
        text-align: left;
    }

    .tag-href {
        background-color: #282828;
        border-radius: 18px;
        text-align: center;
        padding: 0.375em 0.75em;
        margin-right: 2%;
        margin-left: 0%;
        color: #F9F9F9;
        text-decoration: none;
        margin-top: 2%;
    }

    .ex-tag {
        text-decoration: none;
    }

    .tags {
        display: flex;
        justify-content: left;
        align-items: left;
        flex-wrap: wrap;
    }

    .right-menu {
        margin-right: 5%;
    }

    .right-menu a {
        color: #545454;
        font-family: "Helvetica Norm";
        font-size: 20px;
        display: flex;
        flex-direction: column;
        text-align: right;
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

    .return-link {
        text-decoration: none;
    }

    .return-link:hover {
        color: #282828;
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
        width: 40%;
        margin-right: 15%;
        margin-left: 20%;
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

    .exexperience-tags {
        margin-top: 2%;
    }
    .ex-tag {
        text-decoration: none;
    }

    .photo {
        object-fit: cover;
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

        .right-menu {
            display: none;
        }
    }

</style>