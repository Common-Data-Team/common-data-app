<script>
  import {BaseTransition} from '@roxi/routify/decorators'
  import {fade} from 'svelte/transition'

  const configs = [
    {
      condition: (meta) => true,
      transition: fade,
      // inParams: { duration: 1000},
      // outParams: { duration: 1000 }
    }
  ]
</script>

<BaseTransition {configs}>
  <slot/>
</BaseTransition>
