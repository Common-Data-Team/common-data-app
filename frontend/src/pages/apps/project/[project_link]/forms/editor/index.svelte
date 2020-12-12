<script>
  import {writable} from 'svelte/store';
  import Page from './components/Page.svelte';

  let saved = JSON.parse(localStorage.getItem("pagesStore"));
  let pagesStore = writable(saved || [
    [
      {type: "OneChoice", content: {question: 'Выберите один', options: []}},
    ],
  ]);
  pagesStore.subscribe(val => localStorage.setItem("pagesStore", JSON.stringify(val)));

  function destroyer(i) {
    $pagesStore.splice(i, 1);
    $pagesStore = $pagesStore;
  }

  function creator() {
    $pagesStore = $pagesStore.concat([[
      {type: "OneChoice", content: {question: "", options: []}}
    ]]);
  }
</script>

<main>
  {#each Array.from($pagesStore.entries()) as [i, questions]}
    <Page number={i+1} bind:questions={$pagesStore[i]} thisDestroyer={() => destroyer(i)}/>
  {/each}
  <button class="forms_button" on:click={creator}>Новая страница</button>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    width: 1200px;
    min-width: 500px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }
  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>