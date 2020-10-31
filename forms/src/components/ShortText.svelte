<script>
  export let name = 'Short Text';
</script>

<label>
  <input type="text" placeholder={name}>
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
    height: 50px;
    margin-bottom: 10px;
    width: 100%;
  }

</style>