<script>
  import Option from './Option.svelte';
  export let component;
  export let question = 'Выберите несколько';
  export let options = ["1", ];
  let group = [];
</script>

<label>
  <input class="question" value="{question}">
</label>
{#each Array.from(options.entries()) as [i, option]}
  <div class="option-block">
    <svelte:component this={component} style="width: 40px; margin-right: -10px" color="#1355FF"/>
    <Option bind:value={options[i]}/>
    <button on:click={() => {options.splice(i, 1); options = options}}>Удалить опцию</button>
  </div>
{/each}
<button on:click={() => options = options.concat("")}>Новая опция</button>

<style>
  .option-block {
    display: flex;
    justify-items: flex-start;
  }

  .question {
    font-weight: bold;
  }

</style>