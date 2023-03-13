#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    let square = '';
    for (let j = 0; j < x; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
