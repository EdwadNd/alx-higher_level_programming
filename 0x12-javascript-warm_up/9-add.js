#!/usr/bin/node

const a = Math.floor(Number(process.argv[2]));
const b = Math.floor(Number(process.argv[3]));

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(a + b);
}
