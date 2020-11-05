<script>
  import Page from './components/Page.svelte';
  let pages = [0,];

</script>

<main>
  {#each pages as page}
    <Page/>
  {/each}
  <button on:click={() => {pages = pages.concat(Page)}}>Новая страница</button>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>