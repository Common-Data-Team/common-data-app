<script>
  import {fade} from 'svelte/transition';
  import Option from './Option.svelte';

  export let component;
  export let question;
  export let options = [];
  let group = [];
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
  <input class="question forms_input" placeholder="Новый вопрос" bind:value={question}>
</label>

{#each Array.from(options.entries()) as [i, option]}
  <div class="option-block">
    <svelte:component this={component} style="width: 40px; margin-right: -10px" color="#1355FF" {group} bind:title={options[i]}>
    <div class="option-wrapper" in:fade|local>
      <Option bind:value={options[i]} destroyer={() => destroyer(i)} {onFocus} {onBlur}/>
    </div>
    </svelte:component>
  </div>
{/each}

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
</style>