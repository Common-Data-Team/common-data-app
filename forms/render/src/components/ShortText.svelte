<script>
  import { Textfield } from 'svelte-mui';
  export let question = 'Введите текст';
  export let label = 'Короткий текст';

  let value = "";
</script>

<h2>{question}</h2>
<Textfield bind:value {label}/>
