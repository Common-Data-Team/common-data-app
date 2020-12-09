<script>
    import { getCookie, dataStore, apiUrl } from '../../_api.js';
    import { fade } from 'svelte/transition';
    import { goto } from '@roxi/routify'
    import { Menu, Menuitem }  from 'svelte-mui';
    export let tags;
    export let edit = false;
    async function getTags() {
        const response = await fetch(apiUrl + 'tags/all');
        const data = await response.json();
        console.log(data);
        return data;
    }

    let response = getTags();
</script>
<div class="tags_block">
    {#if edit}
    <Menu origin="top left" width=150 dy=40 class="menu">
        <div slot="activator">
        <div class="tag" in:fade><p>Добавить тэг</p></div>
        </div>
        {#await response}
        <p>qwe</p>
            {:then tag_names}
            {#each tag_names as tag_name}
            <Menuitem on:click="{() => {tags = [...tags, {name: tag_name}]; $dataStore.tags = tags}}">{tag_name}</Menuitem>
            {/each}
            {/await}
    </Menu>
    {:else}
        {#if tags.length === 0}
            <div class="tag"><p>Тэгов нет</p></div>
        {/if}
    {/if}
    {#each tags as tag, ind}
        <div class="tag">
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
    }
    .tag p {
        color: #F9F9F9;
        font-style: normal;
        font-weight: 300;
        font-size: 14px;
        line-height: 17px;
    }
</style>