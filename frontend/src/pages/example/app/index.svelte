<script>
    import {authorizedRequest, user} from "./_api";
    import {goto, url} from "@sveltech/routify";
    import {onMount} from "svelte";
    import Group from './_components/Group.svelte';
    import Task from './_components/Task.svelte';
    // let res, err;
    // onMount(async () => {
    //     [res, err] = await authorizedRequest("users/profile", "GET");
        // alert
        // if (err !== null) {
        //     $goto("./auth/signup", {}, false);
        // }
    // });
    import {getContext} from 'svelte';
    let theme = getContext('theme');
    let tasks = [
        {title: "Моя новая задача 1"},
        {title: "Моя новая задача 2"},
        {title: "Моя новая задача 3"},
        {title: "Моя новая задача 4"},
    ];
</script>
<!--{#await res}-->
<!--    <h1>Wait...</h1>-->
<!--{:then awaited}-->
<!--    <h1>-->
<!--        {JSON.stringify(res)}-->
<!--    </h1>-->
<!--{/await}-->
<button on:click={() => $theme = $theme === "light" ? "dark": "light"}>
        {#if $theme === "light"}
   			<img src="static/images/moon.svg" alt="Moon">
        {:else}
   			<img src="static/images/sun.svg" alt="Sun">
        {/if}

</button>

<main class="{$theme}">
<Group {tasks}/>
</main>

<style>
    .dark {
        --background-color: #262626;
    }
    .light {
        --background-color: #D0DBE5;
    }

    main {
        background: var(--background-color);
        position: absolute;
        width: 100%;
        height: 100%;
        display: grid;
        place-items: center;
    }
</style>