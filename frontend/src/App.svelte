<script>
	import router from "page"
	import Register from './components/Register.svelte'    

	let page

	router('/register', () => page = Register)

	router.start()

</script>

<svelte:head>
	<title>{page}</title>
</svelte:head>
<h1>
	Common Data
</h1>

<svelte:component this={page} />