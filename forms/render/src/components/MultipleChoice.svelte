<script>
  import {Checkbox} from "svelte-mui";
  export let question = 'Выберите несколько';
  export let options = [];
  let group = [];
</script>

<h2>{question}</h2>
{#each options as option}
  <Checkbox color="#1355FF">
    <span>{option}</span>
  </Checkbox>
{/each}