<script>
  import Question from './Question.svelte';


  export let questions = [1, 2];

  // questions = questions || [{type: "Statement", content: {statement: "Упсс, это пустая страница :)"}}];

  let selected;

  function destroyer(destroy){
    questions = questions.filter(item => item !== destroy)
    console.log(JSON.stringify(questions))
  }
</script>

<div class="component">
  {#each Array.from(questions.entries()) as [i, _]}
    <Question bind:instance={questions[i]} destroyer={() => destroyer(questions[i])}/>
  {/each}
</div>
<div>
  <button on:click={() => {
    questions = questions.concat({})
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