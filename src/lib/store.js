import { writable } from 'svelte/store';

const initialPlayers = [
  { id: 1, name: 'Player 1', color: '#ff0000' },
  { id: 2, name: 'Player 2', color: '#0000ff' },
];

const initialResources = {
  1: { industrial: 10, military: 10, economic: 10 },
  2: { industrial: 10, military: 10, economic: 10 },
};

const initialTerritories = {
  path12: { owner: 1, armies: 2 },
  path22: { owner: 1, armies: 2 },
  path32: { owner: 1, armies: 2 },
  path13: { owner: 2, armies: 2 },
  path23: { owner: 2, armies: 2 },
  path33: { owner: 2, armies: 2 },
};

export const players = writable(initialPlayers);
export const resources = writable(initialResources);
export const territories = writable(initialTerritories);
export const selected_territory = writable(null);
export const currentPlayer = writable(1);
export const turn = writable(1);
