<script>
  import {getCookie, dataStore, apiUrl} from '../../_api.js';
  import {fade} from 'svelte/transition';
  import {goto} from '@roxi/routify'
  import Menu from '../../_components/Menu.svelte'
  import MenuItem from '../../_components/MenuItem.svelte'
  export let tags;
  export let edit = false;

  async function getTags() {
    const response = await fetch(apiUrl + 'tags/all');
    const data = await response.json();
    return data;
  }

  function deleteTag(name) {
    if (edit) {
      tags = tags.filter(e => e.name !== name);
      $dataStore.tags = tags;
    }
  }
  let response = getTags();

</script>
<div class="tags_block">
  {#if edit}
    <Menu origin="top left" width=150 dy=40 class="menu">
      <div slot="activation">
        <div class="tag " in:fade><p>Добавить тэг</p></div>
      </div>
      {#await response}
        <p>qwe</p>
      {:then tag_names}
        {#each tag_names as tag_name}
          {#if !tags.some(e => e.name === tag_name)}
            <MenuItem top_margin="100"
              on:click="{() => {tags = [...tags, {name: tag_name}]; $dataStore.tags = tags; console.log(tags.includes({name:'AI' }))}}">{tag_name}</MenuItem>
          {/if}
        {/each}
      {/await}
    </Menu>
  {:else}
    {#if tags.length === 0}
      <div class="tag"><p>Тэгов нет</p></div>
    {/if}
  {/if}
  {#each tags as tag, ind}
    <div on:click={() => deleteTag(tag.name)} class="tag">
      <p>{tag.name}</p>
    </div>
  {/each}
</div>

<style>
  .tags_block {
    display: flex;
    flex-wrap: wrap;
    margin: 15px 10px 0 0;
  }

  .tag {
    background-color: #282828;
    border-radius: 18px;
    text-align: center;
    padding: 0.375em 0.75em;
    margin: 0 10px 5px 0;
    text-decoration: none;
    transition: 2s;
  }

  .tag:hover {
    cursor: pointer;
  }

  .tag p {
    color: #F9F9F9;
    font-style: normal;
    font-weight: 300;
    font-size: 14px;
    line-height: 17px;
  }
</style>