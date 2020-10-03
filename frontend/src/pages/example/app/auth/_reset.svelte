<script>
    import PageTransition from '../_components/PageTransition.svelte';
</script>

<main>
    <slot decorator={PageTransition}/>
</main>

<style>
    main {
        position: absolute;
        width: 100%;
        height: 100%;
    }
</style>