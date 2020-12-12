<svelte:options accessors={true}/>
<script context="module">
  import MultipleChoice from './MultipleChoice.svelte';
  import OneChoice from './OneChoice.svelte';
  import ShortText from './ShortText.svelte';

  // import FileUpload from './FileUpload.svelte';
  // import LongText from './LongText.svelte';
  // import Picture from './Picture.svelte';
  // import Statement from './Statement.svelte';

  let components = {
    OneChoice: {component: OneChoice, name: 'Один из списка'},
    MultipleChoice: {component: MultipleChoice, name: 'Несколько из списка'},
    ShortText: {component: ShortText, name: 'Короткий ответ'},
    // FileUpload: [FileUpload, 'Загрузка файла'],
    // LongText: [LongText, 'Развернутый ответ'],
    // Picture: [Picture, 'Картинка'],
    // Statement: [Statement, 'Утверждение'],
  };
  // export function destroy(){
  //
  // }
</script>

<script>
  import {fade} from 'svelte/transition'
  // {type: "Statement", content: {statement: "Упсс, это пустая страница :)"}
  export let instance;
  export let destroyer = () => {};
</script>

<div class="component" in:fade>
  <div class="panel">
    <select bind:value={instance.type}>
      {#each Object.entries(components) as [component_str, {name, component_js}]}
        <option value="{component_str}">{name}</option>
      {/each}
    </select>
    <button on:click={destroyer}>Удалить вопрос</button>
  </div>
  <svelte:component this={components[instance.type].component}
                    bind:content={instance.content}/>
</div>

<style>
  select {
    width: 200px;
  }

  .component {
    width: 80%;
    max-width: 1000px;
    display: flex;
    flex-flow: column nowrap;
    align-items: center;
    border: 1px solid #888888;
    border-radius: 10px;
    margin: 10px;
    padding: 10px;
  }

  .panel {
    display: flex;
  }
</style>