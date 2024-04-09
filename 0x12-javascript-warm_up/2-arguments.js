#!/usr/bin/node
let myVar = process.argv;
let x = myVar.length;
if (x > 2){
    if (x > 3){
	console.log('Arguments found');
    } else {
	console.log('Argument found');
    }
} else {
    console.log('No argument');
}
