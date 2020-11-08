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
  {#each Array.from(questions.entries()) as [i, {type, content}]}
    <Question {type} {content}/>
<!--    <button on:click={() => {options.splice(i, 1); options = options}}>Удалить опцию</button>-->
    <button on:click={() => {questions.splice(i, 1); questions=questions}}>Удалить вопрос</button>
  {/each}
</div>
<div>
  <button on:click={() => {
    questions = questions.concat({
      type: "MultipleChoice",
      content: {question: 'Что добавить в мороженое?',
                options: ['Ваниль', 'Шоколад', 'Маршмеллоу']}})
  }}>Новый вопрос</button>
</div>


<style>
  .component {
    display: flex;
    flex-flow: column nowrap;
    width: 100%;
    height: 100%;
    align-items: center;
    border: 1px solid #666666;
    border-radius: 30px;
  }

</style>