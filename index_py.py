letter = {
  "진짜" : "인터넷에",
  "파이썬" : "이",
  "대세" : "인거 맞아?",
  "이 정도만" : "하면",
  "나도" : "파이써니스타?"
}

def textLetter(obj) : 

    for i in obj.items() :
        for key, value in obj.items() :
            stringAdd = key + " " + value
            print(stringAdd)
    
        # stringAddTwo = stringAddTwo + stringAdd
        # print(stringAddTwo)
    
    






textLetter(letter)