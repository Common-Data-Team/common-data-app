<script>
  export let content = {};
  let {question, placeholder} = content;
  question = question || 'Enter a text';
  placeholder = placeholder || 'Short Text';
</script>

<label>
  <input class="question" placeholder="Новый вопрос">
</label>
<label>
  <input type="text" placeholder={placeholder}>
</label>


<style>
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
    border: none;
  }

</style>