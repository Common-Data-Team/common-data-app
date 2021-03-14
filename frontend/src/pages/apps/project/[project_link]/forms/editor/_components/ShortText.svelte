<script>
  export let content = {};
</script>

<div class="component">
  <label>
    <input class="question" placeholder="Новый вопрос" bind:value={content.question}>
  </label>
  <label>
    <input type="text" placeholder="Начните вводить">
  </label>
</div>

<style>
  .component {
    max-width: 1000px;
    min-width: 300px;
  }
  input {
    background: transparent;
    border: 2px solid transparent;
    border-bottom-color: #666666;
    width: 100%;
    font-size: calc(var(--plain-font-size) - 5px);
    transition: 0.5s ease;
    color: #282828;
  }

  input:focus {
    outline: none;
  }

  label {
    display: flex;
    position: relative;
    /*height: 50px;*/
    /*margin-bottom: 10px;*/
    width: 100%;
  }
  .question{
    font-weight: bold;
    border: 0;
    color: #000000;
  }
  .question::placeholder {
    color: #757580;
  }
  input {
    margin: 10px 0;
  }
  input::placeholder {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
    color: #757580;
    padding: 5px 0;
  }
</style>