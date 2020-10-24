<script>
	import Page from './components/Page.svelte';
	import {fade} from 'svelte/transition';
	import {CurrentPage} from './stores';
	let pages = [
			[{type: "ShortText"}, {type: "ShortText"}],
			[{type: "MultipleChoice"}, {type: "MultipleChoice"}],
	];
</script>

<main>
	<p>{$CurrentPage}</p>
	<div class="animation-box">
		{#each pages as page}
			{#if $CurrentPage === pages.indexOf(page)}
				<div class="page-wrapper">
					<Page questions={page}/>
				</div>
			{/if}
		{/each}
	</div>

</main>

<style>
	main {
		width: 100%;
		height: 99%;
	}
	.page-wrapper {
		position: absolute;
	}
	.animation-box {
		/*position: relative;*/
		/*height: 50%;*/
		width: 100%;
	}

</style>