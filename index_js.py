#pip install js2py
import js2py

letter = {
  "진짜" : "인터넷에",
  "파이썬" : "이",
  "대세" : "인거 맞아?",
  "이 정도만" : "하면",
  "나도" : "파이써니스타?"
}

i_am_javascript = """

function textLetter(obj) {
  let result_map = Object.keys(obj).map(function (key) {
    return [key, obj[key]];
  });

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
  let stringResult = flattened.join(' ');
  console.log(stringResult);
}
"""

internet_warrior = js2py.eval_js(i_am_javascript)

print(internet_warrior(letter))