#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
request.get(args[0], function (error, response, body) {
  // const counter = 0;
  // const j = 0;
  const completed = {};
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    if (data[i].userId in completed) {
      if (data[i].completed === true) {
        completed[data[i].userId] += 1;
      }
    } else {
      if (data[i].completed === true) {
        completed[data[i].userId] = 1;
      }
    }
    /*
    if (j !== data[i].userId) {
      j++;
      counter = 0;
    }
    if (j === data[i].userId) {
      if (data[i].completed === true) {
        counter++;
      }
    }
    if (counter !== 0) {
      completed[data[i].userId] = counter;
    }
  }
*/
  }
  console.log(completed);
});
