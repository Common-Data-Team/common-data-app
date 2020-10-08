<svelte:options accessors={true}/>
<script>
    export let span = "";
    export let type = "text";
    export let value = "";
    export let name = "";
    export let placeholder = "";
    export let spanColor = "#4d4d4d";
    export let mainColor = "black";
    export let input = null;

    let className = "";
    export {className as class};

    let focus = false;

    const handleInput = e => {
        value = type.match(/^(number|range)$/)
            ? +e.target.value
            : e.target.value;
    };
</script>

<label style="--spanColor: {spanColor};
              --mainColor: {mainColor};">
    <input bind:this={input} { placeholder } {type} class="{className}" {name} {value} on:input={handleInput}
           on:focus={() => focus = true}
           on:blur={() => focus = value !== ""}>
    <span class:focus>{span}</span>
</label>

<style>
    input ~ span {
        position: absolute;
        transition: all .5s ease;
        margin-top: 10px;
        margin-left: 5px;
        color: var(--spanColor);
        font-weight: 100;
        font-size: calc(var(--plain-font-size) - 3px);
        cursor: text;
    }

    .focus {
        margin-top: -7px;
        font-size: calc(var(--plain-font-size) - 7px);
    }

    textarea:focus, input:focus {
        outline: none;
    }

    label {
        display: flex;
        position: relative;
        height: 50px;
        margin-bottom: 10px;
        width: 100%;
    }

    input {
        background: transparent;
        border: 2px solid transparent;
        border-bottom-color: var(--mainColor);
        color: var(--mainColor);
        width: 100%;
        font-size: calc(var(--plain-font-size) - 5px);
        transition: 0.5s ease;
    }

    input:invalid {
        border-bottom-color: #F45B69;
    }

    .invalid {
        border-bottom-color: #F45B69;
    }

</style>