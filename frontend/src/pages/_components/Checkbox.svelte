<script>

</script>

<input type="checkbox" class="custom-checkbox" id="happy" name="happy" value="yes">
<label for="happy">Я принимаю пользовательское соглашение</label>

<style>
    .custom-checkbox {
        position: absolute;
        z-index: -1;
        opacity: 0;
    }

    .custom-checkbox+label {
        display: inline-flex;
        align-items: center;
        user-select: none;
    }

    .custom-checkbox+label::before {
        content: '';
        display: inline-block;
        width: 1em;
        height: 1em;
        flex-shrink: 0;
        flex-grow: 0;
        border: 2px solid #9a9a9a;
        border-radius: 0.25em;
        margin-right: 0.5em;
        background-repeat: no-repeat;
        background-position: center center;
        background-size: 50% 50%;
    }

    .custom-checkbox:checked+label::before {
        border-color: #1355FF;
        background-color: #1355FF;
        background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23fff' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3e%3c/svg%3e");
    }
    
    .custom-checkbox:not(:disabled):not(:checked)+label:hover::before {
        border-color: #b3d7ff;
    }

    .custom-checkbox:not(:disabled):active+label::before {
        background-color: #b3d7ff;
        border-color: #b3d7ff;
    }

    .custom-checkbox:focus+label::before {
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
    }

    .custom-checkbox:focus:not(:checked)+label::before {
        border-color: #80bdff;
    }

    .custom-checkbox:disabled+label::before {
        background-color: #e9ecef;
    }
</style>