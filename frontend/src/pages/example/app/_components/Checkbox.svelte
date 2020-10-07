<script>
    export let checked = false;
    export let text = "";
    export let id = 0;
</script>

<div class="component">
    <input id="checkbox-{id}" type="checkbox" class="check">
    <label class="box" for="checkbox-{id}"></label>
    <label class="label" for="checkbox-{id}">{text}</label>
</div>

<style>

    .check:not(:checked),
    .check:checked {
        display: none;
    }

    .box {
        width: 25px;
        height: 25px;
        /*margin: 0 20px;*/
    }

    .check:not(:checked) + .box,
    .check:checked + .box {
        position: relative;
        /*margin: 0 20px;*/
        cursor: pointer;
    }

    /* checkbox aspect */
    .check:not(:checked) + .box:before,
    .check:checked + .box:before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        width: 20px;
        height: 20px;
        border: 2px solid black;
        background: transparent;
        transition: all .2s ease;

    }

    .check:checked + .box:before {
        background: black;
        box-shadow: black;
    }

    /* checked mark aspect */
    .check:not(:checked) + .box:after,
    .check:checked + .box:after {
        content: '•';
        position: absolute;
        border-radius: 80px;
        top: 3px;
        left: 7px;
        font-size: 1em;
        line-height: 0.8;
        background-color: black;
        color: white;
        transition: all .3s ease;
    }

    /* checked mark aspect changes */
    .check:not(:checked) + .box:after {
        opacity: 0;
        transform: scale(0);
    }

    .check:checked + .box:after {
        opacity: 1;
        transform: scale(1);
    }
    .label {
        cursor: pointer;
        margin-left: 35px;
    }

</style>