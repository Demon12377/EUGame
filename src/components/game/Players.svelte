<script>
  import { players, currentPlayer } from '../../lib/store.js';
</script>

<div class="players">
  <h2>Players</h2>
  <ul>
    {#each $players as player}
      <li class:active={player.id === $currentPlayer}>
        {player.name}
      </li>
    {/each}
  </ul>
</div>

<style>
  .active {
    font-weight: bold;
    color: #fff;
    background-color: #333;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    padding: 0.5rem;
    border: 1px solid #ccc;
    margin-bottom: 0.5rem;
  }
</style>
