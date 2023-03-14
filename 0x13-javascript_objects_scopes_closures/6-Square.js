#!/usr/bin/node
const Squarep = require('5-square.js');
class Square extends Squarep {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let square = '';
      for (let j = 0; j < this.width; j++) {
        square += c;
      }
      console.log(square);
    }
  }
}
module.exports;
