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
  export let type;
  export let content = {};
</script>

<div class="component">
  <select bind:value={type}>
    {#each Object.entries(components) as [component_str, {name, component_js}]}
      <option value="{component_str}">{name}</option>
    {/each}
  </select>
  <svelte:component this={components[type].component}/>
</div>

<style>
  select {
    width: 200px;
  }

  .component {
    max-width: 800px;
  }

</style>