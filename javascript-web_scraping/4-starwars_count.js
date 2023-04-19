#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
let counter = 0;
const character = 'https://swapi-api.hbtn.io/api/people/18/';
for (let i = 1; i <= 7; i++) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + i + '/';
  counter += request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    if (JSON.parse(body).characters.includes(character)) {
      return 1;
    }
  });
}
console.log(counter);
