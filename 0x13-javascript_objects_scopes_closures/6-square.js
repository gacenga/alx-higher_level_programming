#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
    constructor(size) {
	super();
	this.width = size;
	this.height = size;
    }

    charPrint(c) {
	if (c) {
	    for (let i = 0; i < this.width; i++) {
		console.log(`${c}`.repeat(this.width));
	    }
	} else {
	    for (let i = 0; i < this.width; i++) {
		console.log('X'.repeat(this.width));
	    }
	}
    }
}

module.exports = Square;
