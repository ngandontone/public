function disemvowel(str) {
  const vowels = ["a", "e", "i", "o", "u"];
  const newstring = str
    .split("")
    .filter((letter) => {
      if (!vowels.includes(letter.toLowerCase())) {
        return letter;
      }
    })
    .join("");
  return newstring;
}
