<script>
  import FileUpload from './FileUpload.svelte';
  import LongText from './LongText.svelte';
  import MultipleChoice from './MultipleChoice.svelte';
  import Picture from './Picture.svelte';
  import ShortText from './ShortText.svelte';
  import Statement from './Statement.svelte';
  import OneChoice from './OneChoice.svelte';

  export let questions;
  questions = questions || [{type: "OneChoice"}];

  let components = {
    FileUpload: FileUpload,
    LongText: LongText,
    MultipleChoice: MultipleChoice,
    Picture: Picture,
    ShortText: ShortText,
    Statement: Statement,
    OneChoice: OneChoice
  };

</script>


<div class="component">
  {#each questions as question}
    <svelte:component this={components[question.type]}/>
  {/each}
</div>


<style>
  .component {
    width: 100%;
    height: 100%;
  }

</style>