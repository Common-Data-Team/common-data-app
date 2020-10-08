<script>
    import PageTransition from './_components/PageTransition.svelte';
    import {selfUrl} from './_api.js';
</script>

<main>
<!--    <slot decorator={PageTransition}/>-->
    <a href="{selfUrl}">
        <img src="/logo.svg" alt="Common data">
    </a>
    <slot decorator={PageTransition}/>
</main>

<style>
    main {
        max-width: 1440px;
        position: absolute;
        width: 95%;
        height: 95%;
        margin-top: 24px;
    }
    img {
        width: 600px;
        margin-bottom: 50px;
        /*max-width;*/
    }
</style>