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
  export let type;
  export let content;
  let selected;
</script>

<h1>{selected}</h1>
<select bind:value={selected}>
  {#each Object.entries(components) as [comp_name, [object, name]]}
    <option value="{comp_name}">{name}</option>
  {/each}
</select>