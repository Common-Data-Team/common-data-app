<script>
    let scoops = 1;
    export let name = 'One Choice';
    export let options = ['1', '2', '3', '4'];
</script>

<h1>{name}</h1>
{#each options as option}
    <input type="radio" bind:group={scoops} value={option}>{option}
{/each}