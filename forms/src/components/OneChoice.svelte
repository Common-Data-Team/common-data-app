<script>
    import { Radio } from 'svelte-mui';

    let group = 'Green';
    export let options = ['1', '2', '3', '4'];
</script>

{#each options as option}
    <Radio color="#1355FF" ripple=true bind:group value={option}>
        <span>{option}</span>
    </Radio>
{/each}