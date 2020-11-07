<svelte:options accessors={true}/>
<script context="module">
  import OneChoice from './OneChoice.svelte';
  import MultipleChoice from './MultipleChoice.svelte';
  import ShortText from './ShortText.svelte';
  // import FileUpload from './FileUpload.svelte';
  // import LongText from './LongText.svelte';
  // import Picture from './Picture.svelte';
  // import Statement from './Statement.svelte';

  let components = {
    OneChoice: [OneChoice, 'Один из списка'],
    MultipleChoice: [MultipleChoice, 'Несколько из списка'],
    ShortText: [ShortText, 'Короткий ответ'],
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
  import {fade} from 'svelte/transition';
  export let type;
  export let content = {};
</script>

<h1>{type}</h1>
<select bind:value={type}>
  {#each Object.entries(components) as [comp_name, [object, name]]}
    <option value="{comp_name}">{name}</option>
  {/each}
</select>
<svelte:component this={components[type][0]} {content}/>

<style>
  select {
    width: 200px;
  }

</style>