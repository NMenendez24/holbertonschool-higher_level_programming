#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
let api = args[0]
if (args[0] === "https://swapi-api.hbtn.io/api/films") {
  api = "https://swapi-api.alx-tools.com/api/people/18/"
};
request.get(api, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log((JSON.parse(body).films.length))
});
