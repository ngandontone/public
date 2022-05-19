function getCount(str) {
    let vowelsCount = 0;
    const vowels = ['a', 'e', 'i', 'o', 'u']
    for(let i = 0;i<str.length;i++){
      if (vowels.join(',').includes(str[i])){
        vowelsCount++
      }
    }
    
    
    return vowelsCount;