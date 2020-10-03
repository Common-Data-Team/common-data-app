<script>
    import {Router} from "@sveltech/routify";
    import {routes} from "../.routify/routes";
</script>

<style global>
    @import "../static/global.css";
    #routify-app{
        height: 100%;
        width: 100%;
        display: flex;
        align-items: center;
        flex-direction: column;
    }
</style>

<Router {routes}/>