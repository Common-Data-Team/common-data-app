<script>
  import {fade} from 'svelte/transition';

  import Page from './components/Page.svelte';
  import MultipleChoice from './components/MultipleChoice.svelte';

  let answers = {};
  let pages = [
    undefined,
    [{
      type: "MultipleChoice",
      content: {question: 'Что добавить в мороженое?', options: ['Ваниль', 'Шоколад', 'Маршмеллоу']}
    },
    {
      type: "MultipleChoice",
      content: {question: 'Что добавить в мороженое?', options: ['Ваниль', 'Шоколад', 'Маршмеллоу']}
    }],
    [{type: "ShortText", content: {question: 'Как вас зовут?', placeholder: 'Иван Иванов'}},],
    [{type: "OneChoice", content: {question: 'У вас хорошее настроение?', options: ['Да', 'Бывало и лучше', 'Нет']}}],
  ];

  let currentPage = 0;
  $: percent = currentPage * 100 / (pages.length - 1);

  function updatePage(value) {
    let updated = currentPage + value;
    if (-1 < updated && updated < pages.length) {
      currentPage += value;
    }
  }

  function handleKeys(event) {
    if (['ArrowRight', 'Enter', 'ArrowDown'].indexOf(event.key) >= 0) {
      updatePage(+1)
    } else if (['ArrowUp', 'ArrowLeft'].indexOf(event.key) >= 0) {
      updatePage(-1)
    }
  }

</script>

<svelte:window on:keydown={handleKeys}/>
<main>
  <div class="animation-box">
    {#each pages as page}
      {#if currentPage === pages.indexOf(page)}
        <div class="page-wrapper" transition:fade>
          <Page questions={page}/>
          {#if currentPage === pages.length - 1}
            <button class="submit-button">Отправить</button>
          {/if}
        </div>
      {/if}
    {/each}
  </div>

  <div class="bottom-block">
    <p class="created-on">Сделано на <a class="commondata-link" href="https://commondata.ru">Common Data</a></p>
    <div>
      <p class="progress-title">Прогресс: {Math.round(percent)}%</p>
      <div class="progress-bar">
        <div class="filled-progress-bar" style="width: {percent}%"></div>
      </div>
    </div>
    <button class="switch-page-button" on:click={() => updatePage(-1)}>
      <svg width="30" height="30px">
        <line x1="0" x2="15" y1="25" y2="7"></line>
        <line x1="30" x2="15" y1="25" y2="7"></line>
      </svg>
    </button>
    <button class="switch-page-button" on:click={() => updatePage(+1)}>
      <svg width="30" height="30px">
        <line x1="0" x2="15" y1="7" y2="25"></line>
        <line x1="30" x2="15" y1="7" y2="25"></line>
      </svg>
    </button>
  </div>

</main>

<style>
  main {
    width: 100%;
    height: 100%;
  }

  line {
    color: black;
    stroke: currentColor;
    stroke-width: 1px;
  }

  button {
    appearance: none;
    background: none;
    margin: 0;
    border: none;
    transition: all ease 0.5s;
  }

  .progress-title {
    padding: 0;
    margin: 0 0 5px 0;
  }

  .created-on {
    margin-right: 20px;
    cursor: default;
  }

  .commondata-link {
    color: #0b7dda;
    transition: color 0.7s ease;
  }

  .commondata-link:hover {
    text-decoration: none;
    color: #1355FF;
  }

  .page-wrapper {
    position: absolute;
    display: flex;
    flex-direction: column;
    width: 60%;
    margin-top: -100px;
  }

  .animation-box {
    width: 100%;
    height: 100%;
    display: grid;
    place-items: center;
  }

  .submit-button {
    background: transparent;
    padding: 10px;
    border-radius: 5px;
    border: 2px solid #0b7dda;
    color: #0b7dda;
    margin-top: 20px;
    align-self: flex-end;
    width: 120px;
  }

  .submit-button:hover {
    background: #0b7dda;
    color: white;
  }

  .submit-button:focus {
    background: #1355FF;
    color: white;
  }

  .bottom-block {
    position: absolute;
    bottom: 50px;
    right: 50px;
    display: flex;
    align-items: center;
  }

  .switch-page-button:hover {
    background: rgba(60, 60, 60, 0.2);
  }

  .progress-bar {
    border: 1px solid grey;
    width: 150px;
    height: 4px;
    border-radius: 5px;
    margin-right: 20px;
  }

  .filled-progress-bar {
    background: #666666;
    height: 100%;
    transition: width ease-in 0.5s;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
  }

</style>