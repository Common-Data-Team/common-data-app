<script>
    export let name = "One Choice";
    export let scoops = 1;
    export let options = ['1', '2', '3', '4'];
</script>

<h2>{name}</h2>
{#each options as option}
    <label class="wrapper-login01">
        <input class="checkbox-login01" type=radio bind:group={scoops} value={option}>
        <span class="style-login01"></span>
        <span class="text-login01">{option}</span>
    </label>
{/each}

<style>
    .checkbox-login01 {
        display: none;
    }
    .style-login01 {
        display: inline-block;
        height: 16px;
        width: 16px;
        border-radius: 50%;
        border: 1px solid #282828;
        background-color: #ffff;
        position: relative;
        margin-right: 10px;
        cursor: pointer;
    }

    .style-login01::before {
            content: '●';
            position: absolute;
            color: #ffffff;
            font-size: 16px;
            height: 16px;
            width: 16px;
            border: 1px solid #282828;
            border-radius: 50%;
            background-color: #282828;
            display: flex;
            align-items: center;
            justify-content: center;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            opacity: 0;
            transition: .3s;
    }
    .text-login01 {
    cursor: pointer;
    }
    .checkbox-login01:checked + .style-login01::before {
    opacity: 1;
    }
</style>