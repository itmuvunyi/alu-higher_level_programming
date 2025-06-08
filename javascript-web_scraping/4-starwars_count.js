#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;

  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes(`/people/${wedgeId}/`)) {
        count++;
        break; // No need to keep checking other characters in the same film
      }
    }
  }

  console.log(count);
});
