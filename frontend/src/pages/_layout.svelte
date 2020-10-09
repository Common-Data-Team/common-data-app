<script>
    import PageTransition from './_components/PageTransition.svelte';
    import {selfUrl} from './_api.js';
</script>

<svelte:head>
    <link rel="shortcut icon" href="/favicon.svg" type="image/svg+xml">
</svelte:head>

<main>
    <a href="{selfUrl}" class="logo-class">
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
        margin-bottom: 3%;
    }

    @media (max-width: 768px) {
        img { 
            max-width: 300px;
        }
    }
</style>