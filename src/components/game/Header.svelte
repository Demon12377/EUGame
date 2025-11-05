<script>
  import { turn, currentPlayer, players } from '../../lib/store.js';

  $: currentPlayerName = $players.find(p => p.id === $currentPlayer).name;
</script>

<header>
  <h1>Capture Europe Thread</h1>
  <div class="game-state">
    <span>Turn: {$turn}</span>
    <span>Current Player: {currentPlayerName}</span>
  </div>
</header>

<style>
  header {
    padding: 1rem;
    background-color: #333;
    color: white;
    text-align: center;
  }

  .game-state {
    display: flex;
    justify-content: space-around;
    padding-top: 0.5rem;
  }
</style>
