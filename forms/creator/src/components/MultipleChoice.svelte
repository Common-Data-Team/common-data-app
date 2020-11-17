<script>
  import {Checkbox} from 'svelte-mui';
  import Choice from './Choice.svelte';
  export let content = {};
  let {question, options} = content;
  question = question || 'Выберите несколько';
  options = options || ["", ];
  let group = [];
</script>

<Choice {question} {options} {group} component={Checkbox}/>