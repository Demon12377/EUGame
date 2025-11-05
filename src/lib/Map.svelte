<script>
  import { onMount } from 'svelte';
  import { geoMercator, geoPath } from 'd3-geo';
  import { feature } from 'topojson-client';
  import { createEventDispatcher } from 'svelte';

  export let locations = [];

  const dispatch = createEventDispatcher();

  let countries = [];
  const width = 800;
  const height = 600;

  const projection = geoMercator().scale(400).translate([width / 2, height / 1.2]);
  const path = geoPath().projection(projection);

  onMount(async () => {
    const response = await fetch('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json');
    const world = await response.json();
    countries = feature(world, world.objects.countries).features;
  });

  function handleCountryClick(country) {
    dispatch('countryclick', { id: country.id, name: country.properties.name });
  }

  $: countryData = countries.map(country => {
    const location = locations.find(loc => loc.id === country.id);
    const centroid = path.centroid(country);
    return {
      ...country,
      location,
      centroid,
    };
  });
</script>

<svg {width} {height}>
  <g>
    {#each countryData as country}
      <path
        d={path(country)}
        fill={country.location?.color || '#ccc'}
        stroke="#fff"
        stroke-width="0.5"
        on:click={() => handleCountryClick(country)}
      />
      {#if country.location}
        <text
          x={country.centroid[0]}
          y={country.centroid[1]}
          text-anchor="middle"
          fill="#000"
          font-size="10px"
          font-family="sans-serif"
        >
          {country.location.name}
        </text>
      {/if}
    {/each}
  </g>
</svg>
