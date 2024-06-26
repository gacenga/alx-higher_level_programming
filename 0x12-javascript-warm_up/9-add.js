#!/usr/bin/node
const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);
function add(a, b) {
    if (!isNaN(a) && !isNaN(b)) {
	let x = a + b
	console.log(`${x}`);
    } else {
	console.log(`NaN`);
    }
}
add(a, b);
