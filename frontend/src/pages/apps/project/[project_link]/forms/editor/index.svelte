<script>
  import {writable} from 'svelte/store';
  import Page from './_components/Page.svelte';
  import {goto} from '@roxi/routify';
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

  function save(){
  //  TODO fetch save
    $goto('../../');
  }
</script>

<main>
  <a class="back-button" href="../">&#8592; К проекту</a>
  <a class="view-button" href="./render">Превью <img class="eye" src="/images/button_images/eye.svg"></a>
  {#each Array.from($pagesStore.entries()) as [i, questions]}
    <Page number={i+1} bind:questions={$pagesStore[i]} thisDestroyer={() => destroyer(i)}/>
  {/each}
  <div class="button-block">
    <button class="forms_button" on:click={creator}>Новая страница</button>
    <button class="save_button" on:click={save}>Сохранить форму</button>
  </div>
</main>

<style>
  main {
    width: 99%;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  a {
    text-decoration: none;
    border-radius: 20px;
    border: 1px solid black;
    padding: 0.7em;
    background: white;
    position: fixed;
    font-size: 1em;
    transition: all ease 0.7s;
  }
  .back-button{
    top: 10px;
    left: 10px;
  }
  .view-button {
    top: 10px;
    right: 10px;
  }
  a:hover {
    border-color: #0b7dda;
  }

  .eye {
    width: 12px;
  }

  .save_button {
    background: #0b7dda;
    color: white;
    padding: 1em;
    border-radius: 10px;
    border: 1px solid transparent;
    margin-top: 20px;
    transition: all ease 0.7s;
  }
  .save_button:hover {
    color: #0b7dda;
    border-color: #0b7dda;
    background: white;
  }

  .button-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    height: 200px;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>