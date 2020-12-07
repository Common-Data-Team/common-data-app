<script context="module">

</script>

<script>
  export let value = "";
  export let destroyer = () => {};
  export let onFocus = () => {};
  export let onBlur = () => {};
</script>

<label class="option-label">
  <input class="option" placeholder="Новая опция..." bind:value on:focus={onFocus} on:blur={onBlur}>
  {#if value !== ""}
    <button class="cross" on:click={destroyer}>
      <svg width="15" height="15">
        <line x1="0" y1="0" x2="15" y2="15"></line>
        <line x1="0" y1="15" x2="15" y2="0"></line>
      </svg>
    </button>
  {/if}
</label>

<style>
  label {
    display: flex;
  }

  .option-label {
    margin-top: 3px;
  }

  line {
    color: black;
    stroke: currentColor;
    stroke-width: 1px;
  }

  .cross {
    padding: 5px 10px;
  }

  input {
    border: none;
  }
</style>