#!/usr/bin/node

const Square = require('./5-square');

module.exports = class Square extends Square {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let character = 'X';
    if (c) {
      character = c;
    }
    let row = '';
    for (let j = 0; j < this.size; j++) {
      row += character;
    }
    for (let i = 0; i < this.size; i++) {
      console.log(row);
    }
  }
};
