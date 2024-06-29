#!/usr/bin/node
const dict = require('./101-data').dict;

function groupByOccurrences(inputDict) {
    result = {};

    Object.keys(inputDict).forEach(userId => {
	let occurrence = inputDict[userId];
	if (!result[occurrence]) {
	    result[occurrence] = [];
	}
	result[occurrence].push(userId);
    });
    return result;
}

const new_result = groupByOccurrences(dict);
console.log(new_result);
