//1
function opposite(number) {
  return number > 0 ? -Math.abs(number) : Math.abs(number);
}
//2
function monkeyCount(n) {
  // your code here
  const array = [];
  for (let i = 1; i <= n; i++) {
    array.push(i);
  }
  return array;
}
//3
function positiveSum(arr) {
  return arr.filter((x) => x > 0).reduce((x, s) => x + s, 0);
}
