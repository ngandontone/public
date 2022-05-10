//1
function abbrevName(name) {
  const fullname = name.split(" ");
  console.log(fullname);
  let first = fullname[0][0].toUpperCase();
  let last = fullname[1][0].toUpperCase();
  return `${first}.${last}`;
  // code away
}

//2
