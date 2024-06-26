#!/usr/bin/node
const args = process.argv;
const arg = args[2];
const number = parseInt(arg);
if (!isNaN(number)) {
    for (i = number; i > 0; i--) {
	row = '';
	for (x = number; x > 0; x--) {
	    row += 'X';
	}
	console.log(row);
    }
} else {
    console.log(`Missing size`);
}
