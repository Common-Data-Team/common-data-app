<script>
  import {ready, url, params, goto} from '@roxi/routify';
  import { getContext } from 'svelte';
  import {writable} from "svelte/store";
  import { getCookie, getData, dataStore, authorizedRequest } from '../../../_api.js';
  import Tags from '../../../_components/Tags.svelte'

  function EditProfile() {
    const {fio, tags, about} = $dataStore;
    const response = authorizedRequest('users/edit', 'PUT', {fio, tags: tags.map(e => e.name), about});
    edit = false;
  }

  let auth = getCookie('user_id') === $params.user_id;
  let edit = false;
  let apiUrl = getContext('apiUrl');
  const promise = getData('users/'+ $params.user_id);

  //функция загрузки и предпросмотра изображения
  let  avatar_file, file_input;
	
	const onFileSelected =(e)=>{
  let image = e.target.files[0];
  let reader = new FileReader();
  reader.readAsDataURL(image);
  reader.onload = e => {
    avatar_file = e.target.result
  };
}
</script>
<!--TODO добавить стили для редактирующих инпутов-->
<main>
  <div class="profile">
    {#await $promise}
      <h1>Загрузка...</h1>
    {:then {fio, avatar, about, tags, as_leader}}
      <div class="main-block">
        <h2 class="pr">Профиль</h2>
        {#if auth}
          {#if edit}
        <a class="edit" on:click={EditProfile}>Сохранить</a>
          {:else}
        <a class="edit" on:click={() => edit = true}>Редактировать</a>
          {/if}
        {/if}
      </div>
      <div class="user_info">
        <div class="user">
          {#if edit}
            <div id="app">
              {#if avatar_file}
              <img class="avatar" src={avatar_file} alt="" />
              {:else}
              <img class="avatar" src={'/' + avatar + '.jpg'} alt="" />
              {/if}
              <img class="upload" src="/images/user_images/upload.svg" alt="" on:click={()=>{file_input.click();}} />
              <div class="chan" on:click={()=>{file_input.click();}}></div>
              <input style="display:none" type="file" accept=".jpg, .jpeg, .png" on:change={(e)=>onFileSelected(e)} bind:this={file_input} >
            </div>
          {:else}
            <img src={'/'+avatar+'.jpg'} class="photo" alt="user_photo"/>
          {/if}
          {#if edit}
          <input bind:value={$dataStore.fio} class="title">
          {:else}
          <h2 class="title" id="name">{fio}</h2>
          {/if}
        </div>
        <div class="self">
          <h2 class="title"> О себе:</h2>
          {#if edit}
            <textarea class="self_textarea" bind:value={$dataStore.about}></textarea>
          {:else}
          <p>{about}</p>
          {/if}
        </div>
        <div class="catigories">
          <h2 class="title">Предпочтения</h2>
          <Tags {edit} {tags}/>
        </div>
        <div clsaa="exexperience">
          <h2 class="title">Участие в проектах:</h2>
          <div class="experience-tags">
            <li>
            {#if as_leader.projects.length === 0}
            <ul>Пока проектов нет.</ul>
              {:else}
              {#each as_leader.projects as project}
                <ul><a on:click={() => $goto('../../project/'+project.project_link)} class="ex-tag">{project.title}</a></ul>
              {/each}
              {/if}
            </li>
          </div>
        </div>
      </div>

    {/await}
  </div>
</main>
<style>

  #app {
    position:relative;
    width: 128px;
    height: 128px;
    border-radius: 50%;
    margin-bottom: 1%;
  }

  .avatar {
    position:absolute;
    object-fit: cover;
    filter: brightness(70%);
    width: 100%;
    padding: 0;
    margin: 0;
    height: 100%;
    border-radius: 50%;
  }

.upload {
  position:absolute;
  height:30px;
   top: 50%;
   left: 50%;
   transform: translate(-50%, -50%);
}

input, textarea {
  background: transparent;
  border: 2px solid #000000;
  border-radius: 5px;
  width: 70%;
}

input {
  font-family: "Helvetica Neue";
  font-size: 24px;
}
textarea {
  overflow: auto;
  font-family: "Helvetica Norm";
  font-size: 16px;
}

  .ex-tag {
    text-decoration: none;
  }

  .ex-tag:hover {
    cursor: pointer;
          }

  #name {
    padding-top: 3%;
  }

  .title {
    font-size: 24px;
  }

  .profile {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    width: 60%;
  }

  .pr {
    padding-bottom: 5%;
    font-size: 40px;
  }

  main {
    margin-left: 5%;
  }


  .edit {
    font-style: normal;
    font-weight: normal;
    font-size: 16px;
    margin-top: 15%;
    text-decoration-line: underline;
  }
  .edit:hover {
    cursor: pointer;
  }
  .user_info {
    display: flex;
    flex-direction: column;
    width: 40%;
  }

  .user {
    margin-bottom: 10%;
  }

  .self {
    margin-bottom: 5%;
  }
  .self p {
    width: 70%;
    white-space: pre-wrap;
  }
  .catigories {
    margin-bottom: 10%;
  }

  .experience-tags {
    margin-top: 2%;
  }

  .ex-tag {
    text-decoration: none;
  }

  .photo {
    object-fit: cover;
    width: 128px;
    height: 128px;
    border-radius: 50%;
    margin-bottom: 1%;
  }
  .self_textarea {
    height: 80px;
  }
  li {
    list-style-type: none;
    margin-bottom: 30%;
  }

  ul {
    padding: 0;
    margin-block-start: 0em;
    margin-block-end: 0em;
    padding: 0;
    margin: 0;
    padding-inline-start: 0px;
  }

  @media (max-width: 768px) {

    main {
      width: 95%;
    }

    .profile {
      flex-direction: column;
    }

    .user_info {
      margin-right: 0%;
      margin-left: 0%;
      max-width: 90%;
      margin-top: 5%;
    }

    .right-menu {
      display: none;
    }
  }

</style>