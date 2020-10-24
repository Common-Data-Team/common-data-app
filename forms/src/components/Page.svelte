<script>
    import FileUpload from './FileUpload.svelte';
    import LongText from './LongText.svelte';
    import MultipleChoice from './MultipleChoice.svelte';
    import Picture from './Picture.svelte';
    import ShortText from './ShortText.svelte';
    import Statement from './Statement.svelte';
    import {fade} from 'svelte/transition';
import OneChoice from './OneChoice.svelte';

    export let questions = [{type: "ShortText"}];

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
</div>

<OneChoice></OneChoice>

<style>

</style>