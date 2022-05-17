function arrayPlusArray(arr1, arr2) {
  let arr1Sum = arr1.reduce((e, i) => e + i, 0);
  let arr2Sum = arr2.reduce((e, i) => e + i, 0);
  return arr1Sum + arr2Sum; //something went wrong
}
