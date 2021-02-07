<script>
  import Checkbox from 'global_components/Checkbox.svelte';
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