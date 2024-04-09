#!/usr/bin/node
let myVar = process.argv;
let x = myVar.length;
if (x > 3) {
    console.log('Arguments found');
} else if (x === 3) {
    console.log('Argument found');
} else {
    console.log('No argument');
}

