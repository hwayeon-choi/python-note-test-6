letter = {
  "진짜" : "인터넷에",
  "파이썬" : "이",
  "대세" : "인거 맞아?",
  "이 정도만" : "하면",
  "나도" : "파이써니스타?"
}

function textLetter(obj) {
  let result_map = Object.keys(obj).map(function (key) {
    return [key, obj[key]];
  });
  // console.log(result_map);

  let stringAdd = [];
  let stringAddTwo = [];
  for(let i = 0; i < result_map.length; i++) {    
    for(let j = 0; j < result_map[i].length; j++) {
      stringAdd.push(result_map[i][j]);
    }   
  }
  stringAddTwo.push(stringAdd);
  let flattened = stringAddTwo.reduce(function(acc, items) {
    return acc.concat(items);
  }, []);
  // console.log(flattened);
  let stringResult = flattened.join(' ');
  console.log(stringResult);
}

textLetter(letter);
