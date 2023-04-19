#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + args[0];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
