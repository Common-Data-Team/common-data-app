<script>
	import Page from './components/Page.svelte';
	import {fade} from 'svelte/transition';
	let pages = [
			[{type: "ShortText"}, {type: "ShortText"}],
	];
	let page_number = 0;
</script>

<main>
<!--	<h1>{page}</h1>-->
	{#each pages as page}
		<h2>{pages.indexOf(page)}</h2>
		{#if page_number === pages.indexOf(page)}
			<div>
				<Page questions={page}/>
			</div>
		{/if}
	{/each}
	<button on:click={() => page++}>+</button>
	<button on:click={() => page--}>-</button>
</main>

<style>

</style>