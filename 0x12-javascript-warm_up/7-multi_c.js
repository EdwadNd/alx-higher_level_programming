#!/usr/bin/node
const process = require('process');
const args = process.argv;

const x = Math.floor(Number(args[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
