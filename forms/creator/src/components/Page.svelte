<script>
  import Question from './Question.svelte';
  import {fade} from 'svelte/transition';
  export let thisDestroyer;
  export let questions;
  export let number;
  function destroyer(i){
    questions.splice(i, 1);
    questions = questions;
  }
</script>

<div class="component" in:fade>
  <h1>Страница {number}</h1>
  <button on:click={thisDestroyer}>Удалить страницу</button>
  {#each Array.from(questions.entries()) as [i, _]}
    <Question bind:instance={questions[i]} destroyer={() => destroyer(i)}/>
  {/each}
  <button on:click={() => {
    questions = questions.concat({type: "OneChoice", content: {question: "", options: []}})
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
    margin-bottom: 40px;
  }

</style>