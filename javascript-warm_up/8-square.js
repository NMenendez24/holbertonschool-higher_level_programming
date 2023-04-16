#!/usr/bin/node
const arg = process.argv.slice(2)
if (isNaN(arg[0])) {
    console.log("Missing size")
} else {
    let row = ""
    for (let j = 0; j < 5; j++) {
      row += 'X';
    }
    for (let i = 0; i < 5; i++) {
        console.log(row);
      }
}