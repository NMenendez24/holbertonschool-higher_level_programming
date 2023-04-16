#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let row = '';
    for (let j = 0; j < this.width; j++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
