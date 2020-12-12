<script>
  import {Checkbox} from "svelte-mui";

  export let question = 'Выберите несколько';
  export let options = [];
  export let answer;
  answer = answer ? answer : [];
</script>

<h2>{question}</h2>
{#each options as option}
  <!--TODO убрать костыль-->
  {#if option !== ""}
    <Checkbox bind:group={answer} value={option} color="#1355FF">
      <span>{option}</span>
    </Checkbox>
  {/if}
{/each}