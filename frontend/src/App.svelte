<script>
    import {Router} from "@sveltech/routify";
    import {routes} from "../.routify/routes";
</script>

<svelte:head>
    <link rel="shortcut icon" href="/flavicon.svg" type="image/svg+xml">
</svelte:head>

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