#!/usr/bin/node
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
const arg = process.argv.slice(2);
add(arg[0], arg[1]);
