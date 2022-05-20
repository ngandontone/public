function highAndLow(numbers) {
  const splitNumbers = numbers.split(" ");
  const numberArray = splitNumbers.map(Number);
  const min = Math.min(...numberArray);
  const max = Math.max(...numberArray);

  return `${max} ${min}`;
}
