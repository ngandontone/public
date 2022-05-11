function noSpace(x) {
  const splitWords = x.split(" ");
  const wordsNoSpaces = splitWords.filter((x) => x !== " " && x !== ",");
  return wordsNoSpaces.join("");
}
