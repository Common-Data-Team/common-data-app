<script>
    import Checkbox from "svelte-checkbox";

    let checked = false;
    
    export let question = 'Choose multiple';
    export let options = ['1', '2', '3', '4'];
</script>

<h2>{question}</h2>
{#each options as option}
    <div>
        <Checkbox name={option} id={option} size="1.5rem" primaryColor="#1355FF"/>
        <label class="text-login01">{option}</label>
    </div>
{/each}

<style>
    div {
        display: flex;
        margin-bottom: 1%;
    }

    .text-login01 {
        cursor: pointer;
        margin-right: 3%;
        margin-left: 3%;
    }

</style>