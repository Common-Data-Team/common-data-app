<script>
  import {fade} from 'svelte/transition';
  import Option from './Option.svelte';

  export let component;
  export let question = 'Выберите несколько';
  export let options = [];
  export let group = [];

  if (options.slice(-1)[0] !== "" || options.length === 0) {
    options = options.concat("");
  }
  function creator() {
    options = options.concat("");
  }

  function destroyer(i) {
    options.splice(i, 1);
    options = options;
  }

  function onFocus() {
    creator();
  }
  function onBlur(){
    options = options.filter(item => item !== "");
    creator();
  }

</script>

<!--<svelte:window on:keydown={event => event.key === 'Enter' ? creator(): false}/>-->
<!--TODO Сделать переключение фокуса по Enter-->
<label>
  <input class="question forms_input" placeholder="Новый вопрос">
</label>

{#each Array.from(options.entries()) as [i, option]}
  <div class="option-block">
    <svelte:component this={component} style="width: 40px; margin-right: -10px" color="#1355FF"/>
    <div class="option-wrapper" in:fade|local>
      <Option bind:value={options[i]} destroyer={() => destroyer(i)} {onFocus} {onBlur}/>
    </div>
  </div>
{/each}
<!--<button class="plus" on:click={create}>-->
<!--  <svg width="17" height="17">-->
<!--    <line x1="9" y1="0" x2="9" y2="17"></line>-->
<!--    <line x1="0" y1="9" x2="17" y2="9"></line>-->
<!--  </svg>-->
<!--</button>-->

<style>
  .option-wrapper {
    display: flex;
  }

  .option-block {
    display: flex;
    justify-content: flex-start;
    width: 300px;
  }

  .question {
    font-weight: bold;
    margin: 10px 0 5px 0;
    padding: 5px;
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