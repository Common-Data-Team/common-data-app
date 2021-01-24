<script>
    import {slide} from 'svelte/transition'
    let menu_visibility = false;
</script>

<div class="menu">
    <div on:click={() => menu_visibility = !menu_visibility}>
    <slot name="activation"></slot>
    </div>
    {#if menu_visibility}
        <div class="menu-list" transition:slide>
            <slot/>
        </div>
    {/if}
</div>

<style>
    .menu {
        position: relative;
    }

    .menu:hover {
        cursor: pointer;
    }

    .menu-list {
        background-color: #FFFFFF;
        position: absolute;
        top: 60px;
        right: 0;
        width: 320px;
        text-align: left;
        padding: 0;
        border-radius: 3px;
        box-shadow: 0 3px 3px -2px rgb(0 0 0 / 20%), 0 3px 4px 0 rgb(0 0 0 / 14%), 0 1px 8px 0 rgb(0 0 0 / 12%);
    }
</style>