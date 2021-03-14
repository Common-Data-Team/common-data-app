<script>
  import Checkbox from 'global_components/Checkbox.svelte';

  export let question = 'Выберите несколько';
  export let options = [];
  export let answer;
  answer = answer ? answer : [];
</script>

<h2>{question}</h2>
<div class="choice-block">
  {#each options as option}
    <!--TODO убрать костыль-->
    {#if option !== ""}
      <Checkbox bind:group={answer} value={option} color="#1355FF">
        <span>{option}</span>
      </Checkbox>
    {/if}
  {/each}
</div>

<style>
  .choice-block {
    display: flex;
    flex-direction: column;
  }
</style>