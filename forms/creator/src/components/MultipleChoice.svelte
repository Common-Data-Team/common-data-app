<script>
  import {Checkbox} from "svelte-mui";
  export let question = 'Выберите несколько';
  export let options = ['1', '2'];
  let group = [];
</script>

<h2>{question}</h2>
{#each options as option}
  <div class="option-block">
    <Checkbox style="width: 40px" color="#1355FF"/>
    <label>
    <input value={option}>
    </label>
  </div>
{/each}

<style>
  .option-block {
    display: flex;
    justify-items: flex-start;
    /*align-items: flex-start;*/
  }
  input {

  }
</style>