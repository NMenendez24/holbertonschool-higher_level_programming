#!/usr/bin/node
const arg = process.argv.slice(2);
if (isNaN(arg[0])) {
  console.log('Missing size');
} else {
  let row = '';
  for (let j = 0; j < arg[0]; j++) {
    row += 'X';
  }
  for (let i = 0; i < arg[0]; i++) {
    console.log(row);
  }
}
