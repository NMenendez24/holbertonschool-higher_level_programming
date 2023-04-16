#!/usr/bin/node

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let character = 'X';
    if (c) {
      character = c;
    }
    let row = '';
    for (let j = 0; j < this.width; j++) {
      row += character;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(row);
    }
  }
};
