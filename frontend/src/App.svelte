<script>
    import {Router} from "@sveltech/routify";
    import {routes} from "../.routify/routes";
</script>

<style global>
    @import "../static/global.css";
    #routify-app{
        height: 100%;
        width: 100%;
    }
</style>

<Router {routes}/>