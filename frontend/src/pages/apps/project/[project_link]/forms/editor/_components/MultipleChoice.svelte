<script>
  import {Checkbox} from 'svelte-mui';
  import Choice from './Choice.svelte';

  export let content;
  let group = [];
</script>

<Choice
  bind:question={content.question}
  bind:options={content.options}
  {group}
  component={Checkbox}
/>