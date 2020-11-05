

<select value={selected}>
  {#each Object.entries(components) as [_, [object, name]]}
    <option>{name}</option>
  {/each}
</select>
<svelte:component this={components[question.type]} {...question.content || {}}/>