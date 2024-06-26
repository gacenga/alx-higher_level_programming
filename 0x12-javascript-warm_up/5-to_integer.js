#!/usr/bin/node
const args = process.argv;
const arg = args[2];
const number = parseInt(arg, 10);
if (!isNaN(number)) {
    console.log(`My number: ${number}`);
} else {
    console.log(`Not a number`);
}
