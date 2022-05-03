// 1
class SmallestIntegerFinder {
  findSmallestInt(args) {
    let smallestValue = args[0];
    for (let i = 0; i <= args.length; i++) {
      if (args[i] < smallestValue) {
        smallestValue = args[i];
      }
    }
    return smallestValue;
  }
}
// 2
function greet(name) {
  //your code here
  return `Hello, ${name} how are you doing today?`;
}
// 3
var summation = function (num) {
  // Code here
  let result = 0;
  for (let i = 0; i <= num; i++) {
    result += i;
  }
  return result;
};
