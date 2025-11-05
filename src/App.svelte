<script>
  import { onMount } from 'svelte';
  import Map from './lib/Map.svelte';

  let locations = [];
  let locationName = '';
  let selectedColor = '#ff0000';
  let selectedCountry = null;

  onMount(() => {
    const storedLocations = localStorage.getItem('locations');
    if (storedLocations) {
      locations = JSON.parse(storedLocations);
    }
  });

  function handleCountryClick(event) {
    selectedCountry = event.detail;
  }

  function assignLocation() {
    if (!selectedCountry || !locationName) {
      alert('Please select a country and enter a location name.');
      return;
    }

    const newLocation = {
      id: selectedCountry.id,
      name: locationName,
      color: selectedColor,
    };

    locations = [...locations.filter(loc => loc.id !== selectedCountry.id), newLocation];
    localStorage.setItem('locations', JSON.stringify(locations));
    locationName = '';
    selectedCountry = null;
  }
</script>

<main>
  <h1>Интерактивная карта</h1>
  <div class="container">
    <div class="map-container">
      <Map {locations} on:countryclick={handleCountryClick} />
    </div>
    <div class="controls">
      <h2>Режим ОПа</h2>
      <div>
        <label for="location-name">Название:</label>
        <input id="location-name" type="text" bind:value={locationName} />
      </div>
      <div>
        <label for="location-color">Цвет:</label>
        <input id="location-color" type="color" bind:value={selectedColor} />
      </div>
      <button on:click={assignLocation}>Назначить</button>
      {#if selectedCountry}
        <p>Выбрана страна: {selectedCountry.name}</p>
      {/if}
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
    width: 200px;
  }
  label {
    display: block;
    margin-bottom: 5px;
  }
</style>
