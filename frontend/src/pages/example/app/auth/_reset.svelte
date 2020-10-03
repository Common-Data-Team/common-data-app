<script>
    import PageTransition from '../_components/PageTransition.svelte';
</script>

<main>
<!--    <slot decorator={PageTransition}/>-->
    <img src="/logo.svg" alt="logo">
    <slot/>
</main>

<style>
    main {
        margin: 0 auto;
        max-width: 1440px;
        padding: 10px;
        position: absolute;
        width: 100%;
        height: 100%;
    }
    img {
        width: 80%;
    }
</style>