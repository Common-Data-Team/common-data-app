<svelte:options accessors={true}/>
<script>
    export let span = "";
    export let type = "text";
    export let value = "";
    export let name = "";
    export let placeholder = "";
    export let spanColor = "#636DFF";
    export let mainColor = "#3f3d56"
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

<label style="--placeholderColor: {spanColor};
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
        color: var(--placeholderColor);
        font-weight: 700;
        cursor: text;
    }

    .focus {
        margin-top: -7px;
        font-size: 0.8em;
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
        transition: 0.5s ease;
    }

    input:invalid {
        border-bottom-color: #F45B69;
    }

    .invalid {
        border-bottom-color: #F45B69;
    }

</style>