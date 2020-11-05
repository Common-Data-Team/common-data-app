<script context="module">
  import FileUpload from './FileUpload.svelte';
  import LongText from './LongText.svelte';
  import MultipleChoice from './MultipleChoice.svelte';
  import Picture from './Picture.svelte';
  import ShortText from './ShortText.svelte';
  import Statement from './Statement.svelte';
  import OneChoice from './OneChoice.svelte';

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

<script>
  export let questions;
  questions = questions || [{type: "Statement", content: {statement: "Упсс, это пустая страница :)"}}];
</script>


<div class="component">
  {#each Object.entries(questions) as [i, question]}
    <svelte:component this={components[question.type]} {...question.content || {}}/>
    {#if (+i) !== questions.length - 1}
      <hr>
    {/if}
  {/each}
</div>


<style>
  .component {
    width: 100%;
    height: 100%;
  }

  hr {
    color: #999999;
    margin-top: 25px;
  }

</style>