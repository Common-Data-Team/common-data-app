<script>
 
</script>

<main>

</main>

<footer>
    <div class="flex">
    <img src="white_logo.svg" class="logo-white" alt="logo-white" />
    <div class="column-block">
        <h3>О НАС</h3>
        <ul>
            <li>проектам</li>
            <li>пользователям</li>
        </ul>
    </div>
    <div class="column-block">
        <h3>СВЯЗАТЬСЯ С НАМИ</h3>
        <ul>
            <li>help@commondata.ru</li>
            <li>+7 (901) 723-04-47</li>
        </ul>
    </div>
    <div class="column-block">
        <h3>СОЦСЕТИ</h3>
        <ul>
            <li>facebook</li>
            <li>telegram</li>
            <li>vkontakte</li>
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
        max-width: 40%;
        padding-left: 5%;
        padding-right: 10%;
    }

    .column-block {
        flex: 1 1 0%;
        max-width: 20%;
        padding-left: 5%;
        padding-right: 5%;
    }

    h3 {
        color: #F9F9F9;
        --nav-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
        font-family: "Helvetica Neue";
    }

    li {
        list-style-type: none;
        color: #BDBDBD;
        font-family: "Helvetica Norm";--nav-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
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