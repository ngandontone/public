//1
function repeatStr(n, s) {
  let string = "";
  for (let i = 1; i <= n; i++) {
    string += s;
  }
  return string;
}
//2
function find_average(array) {
  // your code here
  return array.length > 0 ? array.reduce((x, y) => x + y) / array.length : 0;
}
//3
function check(a, x) {
  return a.includes(x) ? true : false;
}
