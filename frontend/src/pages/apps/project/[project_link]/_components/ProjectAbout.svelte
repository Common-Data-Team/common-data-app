<script>
  import ProjectMenu from './ProjectMenu.svelte';

  export let description;
</script>
<main>
  <ProjectMenu/>
  <div class="description_block">
    <p>{description}</p>
  </div>
</main>
<style>
  .description_block {
    margin: 30px 0 0 3%;
  }
</style>