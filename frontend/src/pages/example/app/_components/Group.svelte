<script>
    import {flip} from 'svelte/animate';
    import {getContext} from 'svelte';
    import Task from '../_components/Task.svelte'

    export let title = "Мой список задач";
    export let url;
    export let tasks = [];

    let theme = getContext('theme');
    let newTask = '';
    let newKey = tasks.length
    tasks = Object.assign({}, tasks);

    function destroyFunction(index) {
        delete tasks[index];
        tasks = tasks; // Svelte needs to detect changes in value
    }

    function addTask(event) {
        if ((event.key && event.key === 'Enter') || !event.key) {
            if (newTask !== '') {
                tasks[newKey] = {title: newTask};
                newKey++;
                newTask = '';
            }
        }
    }
</script>

<div class="{$theme} component">
    <div class="header">
        <label>
            <input class="title" value="{title}">
        </label>
        <svg width="33" height="35" viewBox="0 0 33 35" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M22.6876 24.8752C22.3767 25.1861 22.1091 25.5278 21.8778 25.8891L11.626 19.6663C11.8972 18.9876 12.0508 18.2496 12.0508 17.4754C12.0508 16.7012 11.8972 15.9631 11.6266 15.2844L21.8807 9.10908C22.9338 10.7631 24.78 11.8654 26.8826 11.8654C30.1539 11.8654 32.8153 9.204 32.8153 5.93271C32.8153 2.66141 30.1539 0 26.8826 0C23.6113 0 20.9499 2.66141 20.9499 5.93271C20.9499 6.67785 21.094 7.38859 21.3456 8.04594L11.0779 14.2296C10.0171 12.6135 8.191 11.5427 6.11752 11.5427C2.84623 11.5427 0.184814 14.2041 0.184814 17.4754C0.184814 20.7467 2.84623 23.4081 6.11752 23.4081C8.191 23.4081 10.0165 22.3372 11.0773 20.7212L21.3432 26.9523C21.0881 27.6203 20.9493 28.334 20.9493 29.0703C20.9493 30.6549 21.5663 32.1452 22.687 33.2653C23.8433 34.4216 25.3626 35 26.882 35C28.4014 35 29.9207 34.4216 31.077 33.2653C32.1977 32.1446 32.8147 30.6549 32.8147 29.0703C32.8147 27.4856 32.1977 25.9953 31.077 24.8752C28.7638 22.5615 25.0007 22.5615 22.6876 24.8752ZM26.8826 1.18654C29.4995 1.18654 31.6288 3.31579 31.6288 5.93271C31.6288 8.54962 29.4995 10.6789 26.8826 10.6789C24.2657 10.6789 22.1364 8.54962 22.1364 5.93271C22.1364 3.31579 24.2651 1.18654 26.8826 1.18654ZM6.11811 22.2215C3.5012 22.2215 1.37195 20.0923 1.37195 17.4754C1.37195 14.8585 3.5012 12.7292 6.11811 12.7292C8.73503 12.7292 10.8643 14.8585 10.8643 17.4754C10.8643 20.0923 8.73503 22.2215 6.11811 22.2215ZM30.2381 32.4264C28.3877 34.2768 25.3769 34.2768 23.5265 32.4264C22.63 31.53 22.1364 30.3375 22.1364 29.0703C22.1364 27.803 22.63 26.6106 23.5265 25.7141C24.452 24.7886 25.667 24.3265 26.8826 24.3265C28.0982 24.3265 29.3132 24.7886 30.2387 25.7141C31.1351 26.6106 31.6288 27.803 31.6288 29.0703C31.6288 30.3375 31.1352 31.53 30.2381 32.4264Z"
                  fill="#28486F"/>
        </svg>
    </div>
    <div class="list">
        {#each Object.entries(tasks) as [id, task] (id)}
            <div animate:flip>
                <Task key={id} title={task.title} {destroyFunction}/>
            </div>
        {/each}
    </div>
    <div class="footer">
        <label>
            <input bind:value={newTask} on:keydown={addTask} class="input" placeholder="Новая задача...">
        </label>
        <button class="addTask" on:click={addTask}>
            <svg width="16" height="21" viewBox="0 0 16 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M8.70711 0.292892C8.31658 -0.0976321 7.68342 -0.0976321 7.29289 0.292892L0.928933 6.65685C0.538408 7.04738 0.538408 7.68054 0.928933 8.07107C1.31946 8.46159 1.95262 8.46159 2.34315 8.07107L8 2.41421L13.6569 8.07107C14.0474 8.46159 14.6805 8.46159 15.0711 8.07107C15.4616 7.68054 15.4616 7.04738 15.0711 6.65685L8.70711 0.292892ZM9 21L9 0.999999H7L7 21H9Z"
                      fill="#28486F"/>
            </svg>
        </button>
    </div>
</div>

<style>
    .dark {
        --background-component: #272B30;
        --shadow-component: -10px -10px 15px rgba(82, 82, 82, 0.34), 10px 11px 18px rgba(24, 24, 24, 0.54);
        --lead-color: #E43B15;
        --plain-color: #B8B8B8;
        --button-background: linear-gradient(135deg, #292D31, #282C31);
        --button-box-shadow: 2px 2px 7px #1C1C1C, -2px -2px 5px #494949;
        --footer-background: linear-gradient(91.7deg, #292D31 0%, #282C31 100%);
        --footer-box-shadow: 7px 7px 17px #202020, -5px -5px 10px #343B42;
    }

    .light {
        --shadow-component: 10px 10px 17px #9B9B9B, -10px -10px 26px #FFFFFF;
        --background-component: #E8F1FA;
        --lead-color: #FF5977;
        --plain-color: #28486F;
        --button-background: linear-gradient(135deg, rgba(255, 255, 255, 0.53) 0%, rgba(203, 209, 217, 0.8) 100%), #E8F1FA;
        --button-box-shadow: 2px 2px 4px rgba(172, 172, 172, 0.53), -2px -2px 5px rgba(255, 255, 255, 0.65);
        --footer-background: linear-gradient(91.7deg, #EFF4F9 0%, rgba(225, 240, 255, 0.26) 100%);
        --footer-box-shadow: 7px 7px 8px rgba(0, 0, 0, 0.08), -7px -7px 6px #F8F8F8;
    }

    input {
        margin: 0;
        background: none;
        border: none;
        color: var(--lead-color);
        font-family: var(--lead-font-family);
    }

    input:focus {
        outline: none;
    }

    .addTask {
        border: none;
        cursor: pointer;
        width: 40px;
        height: 40px;
        border-radius: 20px;
        margin-top: 5px;
        background: var(--button-background);
        box-shadow: var(--button-box-shadow);
    }

    .addTask:active {
        border: none;
        background: var(--button-background);
    }

    path {
        fill: var(--plain-color)
    }

    .component {
        width: 465px;
        height: 730px;
        display: flex;
        flex-direction: column;
        align-items: center;
        border-radius: 29px;
        background: var(--background-component);
        box-shadow: var(--shadow-component);
    }

    .header {
        height: 15%;
        display: flex;
        align-items: center;
    }

    .title {
        font-weight: 700;
        font-size: 24px;
    }

    .footer {
        padding: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: var(--footer-background);
        box-shadow: var(--footer-box-shadow);
        border-radius: 35px;
        width: 350px;
        height: 27px;
        margin-bottom: 25px;
    }

    .input {
        width: 295px;
    }

    .input::placeholder {
        opacity: 0.9;
    }

    .list {
        margin: 0 auto;
        width: 100%;
        height: 80%;
        overflow-y: scroll;

        scrollbar-color: var(--lead-color);
        scrollbar-width: thin;
    }

    .list::-webkit-scrollbar {
        width: 7px;
    }

    .list::-webkit-scrollbar-track {
        box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
    }

    .list::-webkit-scrollbar-thumb {
        background-color: darkgrey;
        outline: 1px solid slategrey;
    }
</style>