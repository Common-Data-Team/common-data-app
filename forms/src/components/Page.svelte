<script>
    import FileUpload from './FileUpload.svelte';
    import LongText from './LongText.svelte';
    import MultipleChoice from './MultipleChoice.svelte';
    import Picture from './Picture.svelte';
    import ShortText from './ShortText.svelte';
    import Statement from './Statement.svelte';
    import {fade} from 'svelte/transition';
import OneChoice from './OneChoice.svelte';

    import {CurrentPage} from '../stores';
    export let questions = [];

    let components = {
        FileUpload: FileUpload,
        LongText: LongText,
        MultipleChoice: MultipleChoice,
        Picture: Picture,
        ShortText: ShortText,
        Statement: Statement
    };

</script>

<div class="component" transition:fade>
    {#each questions as question}
        <svelte:component this={components[question.type]}/>
    {/each}
    <button on:click={() => CurrentPage.update(val => val + 1)}>+</button>
	<button on:click={() => CurrentPage.update(val => val - 1)}>-</button>
</div>

<OneChoice></OneChoice>

<style>

</style>