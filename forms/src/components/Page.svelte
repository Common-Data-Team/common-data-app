<script>
    import FileUpload from './FileUpload.svelte';
    import LongText from './LongText.svelte';
    import MultipleChoice from './MultipleChoice.svelte';
    import Picture from './Picture.svelte';
    import ShortText from './ShortText.svelte';
    import Statement from './Statement.svelte';
    import {fade} from 'svelte/transition';
    export let answers = [{type: "ShortText"}];

    let components = {
        FileUpload: FileUpload,
        LongText: LongText,
        MultipleChoice: MultipleChoice,
        Picture: Picture,
        ShortText: ShortText,
        Statement: Statement
    };
    // alert(JSON.stringify(components));

</script>

<div class="component" transition:fade>
    {#each answers as answer}
        <svelte:component this={components[answer.type]}/>
    {/each}
</div>

<style>

</style>