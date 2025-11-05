<script>
  import { resources, currentPlayer } from '../../lib/store.js';

  $: currentResources = $resources[$currentPlayer];
</script>

<div class="resources">
  <h2>Resources</h2>
  <p>Industrial: {currentResources.industrial}</p>
  <p>Military: {currentResources.military}</p>
  <p>Economic: {currentResources.economic}</p>
</div>
