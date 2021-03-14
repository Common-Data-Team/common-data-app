<script>
  import Radio from 'global_components/Radio.svelte';

  export let question = 'Choose one';
  export let answer = [];
  export let options = ['1', '2', '3', '4'];
</script>
<h2>{question}</h2>
<div class="choice-block">
  {#each options as option}
    {#if option !== ""}
      <Radio color="#1355FF" ripple bind:group={answer} value={option}>
        <span>{option}</span>
      </Radio>
    {/if}
  {/each}
</div>

<style>
  .choice-block {
    display: flex;
    flex-direction: column;
  }
</style>