#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.w; i++) {
      let square = '';
      for (let j = 0; j < this.h; j++) {
        square += 'X';
      }
      console.log(square);
    }
  }
}

module.exports = Rectangle;
