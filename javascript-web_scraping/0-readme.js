#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require( 'fs' );
let file = args[0]
fs.readFile(file, 'utf-8', function(err, data) {console.log(data)})
