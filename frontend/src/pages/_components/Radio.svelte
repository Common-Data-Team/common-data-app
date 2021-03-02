<script>
    export let title = 'Я люблю данные'
    export let choice = "0"
</script>

<input class="custom-radio" name="color" type="radio" id="color-green" value={choice}>
<label for="color-green">{title}</label>

<style>
    .custom-radio {
      position: absolute;
      z-index: -1;
      opacity: 0;
    }

    .custom-radio+label {
      display: inline-flex;
      align-items: center;
      user-select: none;
    }

    .custom-radio+label::before {
      content: '';
      display: inline-block;
      width: 1em;
      height: 1em;
      flex-shrink: 0;
      flex-grow: 0;
      border: 2px solid #9a9a9a;
      border-radius: 50%;
      margin-right: 0.5em;
      background-repeat: no-repeat;
      background-position: center center;
      background-size: 50% 50%;
    }

    .custom-radio:not(:disabled):not(:checked)+label:hover::before {
      border-color: #b3d7ff;
    }

    .custom-radio:not(:disabled):active+label::before {
      background-color: #b3d7ff;
      border-color: #b3d7ff;
    }

    .custom-radio:focus+label::before {
      box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
    }

    .custom-radio:focus:not(:checked)+label::before {
      border-color: #80bdff;
    }

    .custom-radio:checked+label::before {
      border-color: #1355FF;
      background-color: #1355FF;
      background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23fff'/%3e%3c/svg%3e");
    }

    .custom-radio:disabled+label::before {
      background-color: #e9ecef;
    }
  </style>
  