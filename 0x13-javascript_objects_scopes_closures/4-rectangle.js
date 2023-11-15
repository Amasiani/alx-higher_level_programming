#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
     this.height = h;
  }
  
  print () {
    for (let = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.height; j++) {
        s += 'X';
      }
     console.log(s);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
