#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
const file = args[0];
const string = args[1];
fs.writeFile(file, string, function (err) { if (err) { console.log(err); } });
