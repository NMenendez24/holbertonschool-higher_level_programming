#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
const url = args[0];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(args[1], body, function (err) { if (err) { console.log(err); } });
}
);
