<script>
  import Header from './Header.svelte';
  import Controls from './Controls.svelte';
  import Resources from './Resources.svelte';
  import Players from './Players.svelte';
  import Map from './Map.svelte';
  import { territories, currentPlayer, players } from '../../lib/store.js';

  function handleTileClick(event) {
    const id = event.detail.id;
    const currentPlayerId = $currentPlayer;
    const player = $players.find(p => p.id === currentPlayerId);

    territories.update(currentTerritories => {
      return {
        ...currentTerritories,
        [id]: {
          playerId: currentPlayerId,
          color: player.color
        }
      };
    });
  }

  $: tileData = Object.entries($territories).reduce((acc, [id, data]) => {
    acc[id] = data.color;
    return acc;
  }, {});
</script>

<div class="game-ui">
  <Header />
  <div class="main-content">
    <div class="left-panel">
      <Resources />
      <Players />
    </div>
    <div class="map-container">
      <Map {tileData} on:tileclick={handleTileClick} />
    </div>
    <div class="right-panel">
      <Controls />
    </div>
  </div>
</div>

<style>
  .game-ui {
    display: flex;
    flex-direction: column;
    height: 100vh;
  }

  .main-content {
    display: flex;
    flex-grow: 1;
  }

  .left-panel,
  .right-panel {
    width: 200px;
    padding: 1rem;
  }

  .map-container {
    flex-grow: 1;
  }
</style>
