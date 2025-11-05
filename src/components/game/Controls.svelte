<script>
  import { currentPlayer, players, turn } from '../../lib/store.js';

  function endTurn() {
    currentPlayer.update(cp => {
      const nextPlayerIndex = ($players.findIndex(p => p.id === cp) + 1) % $players.length;
      return $players[nextPlayerIndex].id;
    });

    if ($currentPlayer === $players[0].id) {
      turn.update(t => t + 1);
    }
  }
</script>

<div class="controls">
  <h2>Controls</h2>
  <button on:click={endTurn}>End Turn</button>
</div>

<style>
  .controls {
    display: flex;
    flex-direction: column;
  }
</style>
