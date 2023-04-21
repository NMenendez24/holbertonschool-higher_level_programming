#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
let url = args[0];
  request.get(url, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    console.log((body));
  }
);
