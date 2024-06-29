#!/usr/bin/node
const Square_p = require('./5-square');

class Square extends Square_p {
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
