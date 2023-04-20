#!/usr/bin/node
const request = require('request');
request.get("https://swapi-api.alx-tools.com/api/people/18/", function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log((JSON.parse(body).films.length))
});
