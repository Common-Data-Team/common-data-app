<script>
    export let name = 'Miltiple Choice';
    export let options = ['1', '2', '3', '4'];
</script>

<h1>{name}</h1>
{#each options as option}
    <input type="checkbox" value={option}>{option}
{/each}