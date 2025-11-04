<script>
  import { onMount } from 'svelte';
  import Map from './lib/Map.svelte';

  let regions = [];
  let selectedColor = '#f00';
  let tileData = {};

  onMount(async () => {
    const response = await fetch('/regions.txt');
    const text = await response.text();
    regions = text.split('\n').filter(Boolean);
    loadTileData();
    window.addEventListener('storage', loadTileData);
  });

  function loadTileData() {
    const storedData = localStorage.getItem('tileData');
    if (storedData) {
      tileData = JSON.parse(storedData);
    } else {
      tileData = {};
    }
  }

  function handleTileClick(event) {
    const id = event.detail.id;
    tileData[id] = selectedColor;
    localStorage.setItem('tileData', JSON.stringify(tileData));
    // Svelte's reactivity will update the component
    tileData = tileData;
  }

  function resetMap() {
    localStorage.removeItem('tileData');
    tileData = {};
  }
</script>

<main>
  <h1>Интерактивная карта</h1>
  <div class="container">
    <div class="map-container">
      <Map {tileData} on:tileclick={handleTileClick} />
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
    flex-grow: 1;
  }
  .controls {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
</style>
