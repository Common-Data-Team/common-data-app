<script>
	import Page from './components/Page.svelte';
	let pages = [];
	let page = 0;
</script>

<main>
	<Page/>
	<button on:click={() => page++}>+</button>
	<button on:click={() => page--}>-</button>
</main>

<style>

</style>