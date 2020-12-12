<script>
  import { Textfield } from 'svelte-mui';
  export let question = 'Введите текст';
  export let label = 'Начните вводить';
  export let answer = '';
</script>

<h2>{question}</h2>
<Textfield bind:value={answer} {label}/>
