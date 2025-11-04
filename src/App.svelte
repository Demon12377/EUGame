<script>
  import { onMount } from 'svelte';
  import Map from './lib/Map.svelte';

  let tilesData = [];
  let gameState = {};
  let selectedColor = '#000000';

  onMount(async () => {
    const res = await fetch('/data.txt');
    const text = await res.text();
    tilesData = text.split('\n').map((line, index) => {
      const [id, name] = line.split(',');
      return { id, name };
    });

    const savedState = localStorage.getItem('gameState');
    if (savedState) {
      gameState = JSON.parse(savedState);
    } else {
      tilesData.forEach(tile => {
        gameState[tile.id] = '#ffffff';
      });
    }
  });

  function handleTileClick(event) {
    const tileId = event.detail;
    gameState[tileId] = selectedColor;
    gameState = gameState; // Trigger reactivity
    localStorage.setItem('gameState', JSON.stringify(gameState));
  }

  function resetMap() {
    tilesData.forEach(tile => {
      gameState[tile.id] = '#ffffff';
    });
    gameState = gameState; // Trigger reactivity
    localStorage.removeItem('gameState');
  }
</script>

<main>
  <h1>Интерактивная карта</h1>
  <div class="container">
    <div class="map-container">
      <Map {tilesData} {gameState} on:tileClick={handleTileClick} />
    </div>
    <div class="controls">
      <input type="color" bind:value={selectedColor} />
      <button on:click={resetMap}>Сбросить</button>
    </div>
  </div>
</main>

<style>
  .container {
    display: flex;
    gap: 20px;
  }
  .map-container {
    width: 80%;
  }
  .controls {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
</style>
