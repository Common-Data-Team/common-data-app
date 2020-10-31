<script>
    import { Radio } from 'svelte-mui';

    export let question = 'Choose one';
    export let group = null;
    export let options = ['1', '2', '3', '4'];
</script>

<h2>{question}</h2>
{#each options as option}
    <Radio color="#1355FF" ripple bind:group value={option}>
        <span>{option}</span>
    </Radio>
{/each}