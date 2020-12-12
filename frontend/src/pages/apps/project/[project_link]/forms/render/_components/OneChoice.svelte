<script>
  import {Radio} from 'svelte-mui';

  export let question = 'Choose one';
  export let answer = [];
  export let options = ['1', '2', '3', '4'];
</script>

<h2>{question}</h2>
{#each options as option}
  {#if option !== ""}
    <Radio color="#1355FF" ripple bind:group={answer} value={option}>
      <span>{option}</span>
    </Radio>
  {/if}
{/each}