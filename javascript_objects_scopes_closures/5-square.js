#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    let character = "X"
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
