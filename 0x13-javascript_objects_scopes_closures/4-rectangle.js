#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
	if (w > 0 && h > 0) {
	    this.width = w;
	    this.height = h;
	}
    }


    print() {
	if (this.width && this.height) {
	    for (let i = 0; i < this.height; i++) {
		console.log('X'.repeat(this.width));
	    }
	}
    }

    rotate() {
	if (this.width && this.height) {
	    let k = this.width;
	    this.width = this.height;
	    this.height = k;
	}
    }

    double() {
	if (this.width && this.height) {
	    this.width = this.width * 2;
	    this.height = this.height * 2;
	}
    }
}

module.exports = Rectangle;
