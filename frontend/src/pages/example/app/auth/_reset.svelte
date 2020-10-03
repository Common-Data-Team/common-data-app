<script>
    import PageTransition from '../_components/PageTransition.svelte';
</script>

<main>
<!--    <slot decorator={PageTransition}/>-->
    <img src="/logo.svg" alt="Common data">
    <slot/>
</main>

<style>
    main {
        max-width: 1440px;
        position: absolute;
        width: 95%;
        height: 100%;
        margin-top: 24px;
    }
    img {
        width: 80%;
    }
</style>