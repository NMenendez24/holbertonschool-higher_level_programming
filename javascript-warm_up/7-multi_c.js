#!/usr/bin/node
const arg = process.argv.slice(2)
if (isNaN(arg[0])) {
    console.log("Missing number of occurrences")
} else {
    for (let j = 0; j < arg[0]; j++) {
        console.log("C is fun")
    }
}