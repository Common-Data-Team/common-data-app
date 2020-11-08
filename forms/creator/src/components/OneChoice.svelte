<script>
  import {Radio} from 'svelte-mui';
  import Choice from './Choice.svelte';

  export let question = 'Выберите несколько';
  export let options = ["1", ];
  let group = [];
</script>

<Choice {question} {options} {group} component={Radio}/>


