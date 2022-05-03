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
