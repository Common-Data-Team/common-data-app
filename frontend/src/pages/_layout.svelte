<script>
    import PageTransition from './_components/PageTransition.svelte';
    import {selfUrl} from './_api.js';
</script>

<main>
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
        max-width: 600px;
        margin-bottom: 50px;
    }

    @media (max-width: 768px) {
        img { 
            max-width: 300px;
        }
    }
</style>