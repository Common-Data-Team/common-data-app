<script context="module">
  import FileUpload from './FileUpload.svelte';
  import LongText from './LongText.svelte';
  import MultipleChoice from './MultipleChoice.svelte';
  import Picture from './Picture.svelte';
  import ShortText from './ShortText.svelte';
  import Statement from './Statement.svelte';
  import OneChoice from './OneChoice.svelte';

  let components = {
    OneChoice: [OneChoice, 'Один из списка'],
    MultipleChoice: [MultipleChoice, 'Несколько из списка'],
    ShortText: [ShortText, 'Короткий ответ'],
    // FileUpload: [FileUpload, 'Загрузка файла'],
    // LongText: [LongText, 'Развернутый ответ'],
    // Picture: [Picture, 'Картинка'],
    // Statement: [Statement, 'Утверждение'],
  };

</script>

<script>
  export let questions = [''];
  questions = questions || [{type: "Statement", content: {statement: "Упсс, это пустая страница :)"}}];

  let selected;

</script>

<div class="component">
  {#each questions as question}
    <select value={selected}>
      {#each Object.entries(components) as [_, [object, name]]}
        <option>{name}</option>
      {/each}
    </select>
    <svelte:component this={components[question.type]} {...question.content || {}}/>
  {/each}
</div>
<div>
  <button>Новый вопрос</button>
</div>


<style>
  .component {
    width: 100%;
    height: 100%;
  }

</style>