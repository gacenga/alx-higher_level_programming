#!/usr/bin/node
const args = process.argv;
const arg = args[2];
const number = parseInt(arg);
if (!isNaN(number)) {
    for (i = 0; i < arg; i++) {
	console.log(`C is fun`);
    }
} else {
    console.log(`Missing number of occurrences`);
}
