<script>
  // Import markdown conversion library
  import {cache, dataStore} from '../../../../_api.js';
  import {params} from '@roxi/routify';
  import marked from 'marked'

  // Declare a variable to store the markdown data. Set a default value
  export let edit;
  export let markdown;
</script>

<!-- Convert the markdown to HTML and display it -->
<div class="preview">{@html marked($dataStore.description ? $dataStore.description : '')}</div>

<!-- Declare a textarea where the user can enter markdown, and bind it to the variable `markdown` -->
{#if edit}
  <textarea bind:value={$dataStore.description} placeholder="Enter markdown here"></textarea>
{/if}


<style>
  textarea, .preview {
    box-sizing: border-box;
    display: block;
    width: 100%;
  }

  textarea {
    font-family: monospace, Roboto;
    margin: 0 2% 50px 2%;
    min-height: 200px;
    width: 800px;
    border: 2px solid #000000;
    border-radius: 5px;
    outline: none;
  }

  .preview {
    padding: 2rem;
  }

  :global(body) {
    padding: 0;
  }
  @media (max-width: 1000px) {
    textarea {
      width: 90%;
    }
    .preview {
      padding: 10px 3%;
    }
  }
</style>