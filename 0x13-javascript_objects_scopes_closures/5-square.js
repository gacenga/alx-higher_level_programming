#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
    constructor(size) {
	if (size > 0) {
	    super();
	    this.width = size;
	    this.height = size;
	}
    }
}

module.exports = Square;
