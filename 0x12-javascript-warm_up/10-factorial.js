#!/usr/bin/node
function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * factorial(n - 1));
}
let x = factorial(process.argv[2]);
console.log(`${x}`);
