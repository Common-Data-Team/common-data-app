<script>
  import { fade } from 'svelte/transition';
  import Option from './Option.svelte';

  export let component;
  export let question = 'Выберите несколько';
  export let options = [];
  export let group = [];

  function destroyer(i){
    options = options.filter(item => options.indexOf(item) !== i);
  }

</script>

<label>
  <input class="question" placeholder="Новый вопрос">
</label>

{#each Array.from(options.entries()) as [i, option]}
  <div class="option-block">
    <svelte:component this={component} style="width: 40px; margin-right: -10px" color="#1355FF"/>
    <div class="option-wrapper" in:fade|local>
      <Option bind:value={options[i]} destroyer={() => destroyer(i)}/>
    </div>
  </div>
{/each}
<button class="plus" on:click={() => options = options.concat("")}>
  <svg width="17" height="17">
    <line x1="9" y1="0" x2="9" y2="17"></line>
    <line x1="0" y1="9" x2="17" y2="9"></line>
  </svg>
</button>

<style>
  .option-wrapper {
    display: flex;
  }

  .option-block {
    display: flex;
  }

  .question {
    font-weight: bold;
    border: none;
  }

  line {
    color: black;
    stroke: currentColor;
    stroke-width: 1px;
  }

  .plus {
    padding: 8px;
  }
</style>