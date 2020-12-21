<script>
  import { BaseTransition } from '@roxi/routify/decorators'
  import { fade } from 'svelte/transition'
  import {selfUrl} from './_api.js';

  const configs = [
    {
        condition: meta => meta.routes[0].filepath === '/apps/project/[project_link]/index.svelte',
        transition: fade
    },
    {
      condition: () => true,
      transition: () => {}
    }
  ]
</script>

<svelte:head>
  <link rel="shortcut icon" href="/favicon.svg" type="image/svg+xml">
</svelte:head>
<main>
  <a href="{selfUrl}" class="logo-class">
    <img src="/logo.svg" alt="Common data">
  </a>
  <BaseTransition {configs}>
  <slot/>
  </BaseTransition>
</main>

<style>

  main {
    position: absolute;
    width: 100%;
    height: 95%;
    margin-top: 24px;
  }

  img {
    max-width: 600px;
    margin-bottom: 3%;
    margin-left: 5%;
  }

  @media (max-width: 768px) {
    img {
      max-width: 300px;
    }
  }
</style>