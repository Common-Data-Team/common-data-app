<script>
  export let group
  export let title
  export let checked = false

  function changeGroup() {
    if (checked) {
      group.splice(group.indexOf(title), 1)
      group = group
    } else {
      group = [title]
    }
    checked = !checked
  }
</script>

<label>
  <input class="custom-radio" name="color" type="radio" id="color-green" on:change={changeGroup}>
  <div class="title"><slot/></div>
</label>

<style>
    .custom-radio {
      position: absolute;
      z-index: -1;
      opacity: 0;
    }

    .title {
      display: inline-flex;
      align-items: center;
      user-select: none;
    }

    .custom-radio + .title::before {
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

    .custom-radio:not(:disabled):not(:checked) + .title:hover::before {
      border-color: #b3d7ff;
    }

    .custom-radio:not(:disabled):active + .title::before {
      background-color: #b3d7ff;
      border-color: #b3d7ff;
    }

    .custom-radio:focus + .title::before {
      box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
    }

    .custom-radio:focus:not(:checked) + .title::before {
      border-color: #80bdff;
    }

    .custom-radio:checked + .title::before {
      border-color: #1355FF;
      background-color: #1355FF;
      background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23fff'/%3e%3c/svg%3e");
    }

    .custom-radio:disabled + .title::before {
      background-color: #e9ecef;
    }
  </style>
  