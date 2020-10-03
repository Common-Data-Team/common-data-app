<script>
    import {getContext} from 'svelte';
    import {draw, fade, scale} from 'svelte/transition';
    let theme = getContext('theme')
    export let key;
    export let title = "Моя задача";
    export let done = false;
    export let destroyFunction = () => {};
    let checkboxLabel;
    let checkboxInput;
    let component;

    $: plainColor = ($theme === "light") ? "#28486F" : "#B8B8B8";
    function destroy(){
        destroyFunction(key);
    }

</script>

<div transition:scale bind:this={component} class="{$theme} component" class:done class:undone={!done}>
    <input bind:this={checkboxInput} id="checkBox{key}" type="checkbox" class="checkbox-input" class:done class:undone={!done} bind:checked={done}>
    <label bind:this={checkboxLabel} class="checkbox-label" for="checkBox{key}"></label>
    <label class="title-label">
        {#if done}
            <svg class="line" width="270" height="2" viewBox="0 0 270 2" fill="none" xmlns="http://www.w3.org/2000/svg">
                <line transition:draw y1="1" x2="270" y2="1" stroke-opacity="0.4" stroke-width="2"/>
            </svg>
        {/if}
        <input type="text" class="title" bind:value={title}>
    </label>
    {#if done}
        <button class="trash-button" on:click="{destroy}">
        <svg transition:fade width="25" height="25" viewBox="0 0 25 25" fill="none"
             xmlns="http://www.w3.org/2000/svg">
            <path d="M3.125 6.25H5.20833H21.875" stroke="{plainColor}" stroke-width="2" stroke-linecap="round"
                  stroke-linejoin="round"/>
            <path d="M20.7916 6.25C20.7916 5.69771 20.3439 5.25 19.7916 5.25C19.2393 5.25 18.7916 5.69771 18.7916 6.25H20.7916ZM6.20825 6.25C6.20825 5.69771 5.76054 5.25 5.20825 5.25C4.65597 5.25 4.20825 5.69771 4.20825 6.25H6.20825ZM7.33325 6.25C7.33325 6.80228 7.78097 7.25 8.33325 7.25C8.88554 7.25 9.33325 6.80228 9.33325 6.25H7.33325ZM15.6666 6.25C15.6666 6.80228 16.1143 7.25 16.6666 7.25C17.2189 7.25 17.6666 6.80228 17.6666 6.25H15.6666ZM18.7916 6.25V20.8333H20.7916V6.25H18.7916ZM18.7916 20.8333C18.7916 21.4316 18.3066 21.9167 17.7083 21.9167V23.9167C19.4111 23.9167 20.7916 22.5362 20.7916 20.8333H18.7916ZM17.7083 21.9167H7.29159V23.9167H17.7083V21.9167ZM7.29159 21.9167C6.69328 21.9167 6.20825 21.4316 6.20825 20.8333H4.20825C4.20825 22.5362 5.58871 23.9167 7.29159 23.9167V21.9167ZM6.20825 20.8333V6.25H4.20825V20.8333H6.20825ZM9.33325 6.25V4.16666H7.33325V6.25H9.33325ZM9.33325 4.16666C9.33325 3.56835 9.81828 3.08333 10.4166 3.08333V1.08333C8.71371 1.08333 7.33325 2.46378 7.33325 4.16666H9.33325ZM10.4166 3.08333H14.5833V1.08333H10.4166V3.08333ZM14.5833 3.08333C15.1816 3.08333 15.6666 3.56835 15.6666 4.16666H17.6666C17.6666 2.46378 16.2861 1.08333 14.5833 1.08333V3.08333ZM15.6666 4.16666V6.25H17.6666V4.16666H15.6666Z"
                  fill="{plainColor}"/>
            <path d="M10.4167 11.4583V17.7083" stroke="{plainColor}" stroke-width="2" stroke-linecap="round"
                  stroke-linejoin="round"/>
            <path d="M14.5833 11.4583V17.7083" stroke="{plainColor}" stroke-width="2" stroke-linecap="round"
                  stroke-linejoin="round"/>
        </svg>
        </button>
    {/if}
</div>

<style>
    .dark {
        --background-undone: linear-gradient(91.7deg, rgba(53, 57, 62, 0.32) 0%, rgba(33, 38, 42, 0.26) 100%), #292E33;
        --background-done: #292E33;
        --shadow-undone: 5px 5px 22px #222222, -5px -5px 8px #343B42;
        --shadow-done: inset 7px 7px 7px #222222, inset -7px -7px 10px #343B42;;
        --lead-color: #E43B15;
        --plain-color: #B8B8B8;
        --stroke-color: #CBCBCB;
    }

    .light {
        --background-undone: linear-gradient(91.7deg, #F8FBFF 0%, rgba(208, 218, 227, 0.26) 100%), #E5EBF1;
        --background-done: #E5EBF1;
        --shadow-undone: 5px 5px 7px rgba(165, 165, 165, 0.4), -5px -5px 7px rgba(248, 248, 248, 0.76);
        --shadow-done: inset 7px 7px 7px rgba(0, 0, 0, 0.08), inset -7px -7px 6px rgba(248, 248, 248, 0.47);
        --lead-color: #FF5977;
        --plain-color: #28486F;
        --stroke-color: #000000;
    }

    .title {
        margin: 0;
        width: 280px;
    }

    .line {
        position: absolute;
        margin-top: 12px;
        fill: var(--stroke-color);
        stroke: var(--stroke-color);
    }
    .trash-button {
        padding: 0;
        margin: 0;
        background: transparent;
        border: none;
        cursor: pointer;
    }
    .trash-button:active {
        background: none;
    }
    .done {
        box-shadow: var(--shadow-done);
        background: var(--background-done);
    }

    .undone {
        box-shadow: var(--shadow-undone);
        background: var(--background-undone);
    }

    .component {
        border-radius: 9px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        width: 390px;
        height: 67px;
        margin: 18px auto;
    }


    .title {
        font-family: var(--lead-font-family);
        font-size: 18px;
        color: var(--plain-color);
        background: transparent;
        border: none;
        padding: 0;

    }

    .title:focus {
        outline: none;
    }

    .title-label {
        position: relative;
    }


    .checkbox-input:not(:checked),
    .checkbox-input:checked {
        display: none;
    }

    .checkbox-label {
        width: 20px;
        height: 20px;
    }

    .checkbox-input:not(:checked) + .checkbox-label,
    .checkbox-input:checked + .checkbox-label {
        position: relative;
        margin: 0 20px;
        cursor: pointer;
    }

    /* checkbox aspect */
    .checkbox-input:not(:checked) + .checkbox-label:before,
    .checkbox-input:checked + .checkbox-label:before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        width: 20px;
        height: 20px;
        border: 2px solid var(--lead-color);
        background: transparent;
        border-radius: 20px;
    }

    .checkbox-input:checked + .checkbox-label:before {
        background: var(--lead-color);
        box-shadow: 0 0 6px var(--lead-color);
    }

    /* checked mark aspect */
    .checkbox-input:not(:checked) + .checkbox-label:after,
    .checkbox-input:checked + .checkbox-label:after {
        content: '\2713\0020';
        position: absolute;
        border-radius: 20px;
        top: 5px;
        left: 6px;
        font-size: 1em;
        line-height: 0.8;
        background-color: var(--lead-color);
        color: white;
        transition: all .2s;
    }

    /* checked mark aspect changes */
    .checkbox-input:not(:checked) + .checkbox-label:after {
        opacity: 0;
        transform: scale(0);
    }

    .checkbox-input:checked + .checkbox-label:after {
        opacity: 1;
        transform: scale(1);
    }


</style>