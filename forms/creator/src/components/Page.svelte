<script>
  import Question from './Question.svelte';

  export let questions =
      [
        {
          type: "MultipleChoice",
          content: {question: 'Что добавить в мороженое?', options: ['Ваниль', 'Шоколад', 'Маршмеллоу']}
        },
        {
          type: "MultipleChoice",
          content: {question: 'Что добавить в мороженое?', options: ['Ваниль', 'Шоколад', 'Маршмеллоу']}
        }
      ];

  // questions = questions || [{type: "Statement", content: {statement: "Упсс, это пустая страница :)"}}];

  let selected;

</script>

<div class="component">
  {#each questions as {type, content}}
    <Question {type} {content}/>
  {/each}
</div>
<div>
  <button>Новый вопрос</button>
</div>


<style>
  .component {
    display: flex;
    flex-flow: column nowrap;
    width: 100%;
    height: 100%;
  }

</style>