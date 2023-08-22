



#list
choices = [] # kyun ky hum ny option select krni ha
#loop bar bar check krne k liye kon sa box khali ha or kis ki bari ha
for i in range(0,16):
  choices.append(str(i))
firstplayer = True
winner = False
iterations = 0

#ab hum box ko deisgn kr lyte hain

def printbox():
  print("===============")
  print('|'+ choices[0]+ ' ' +'|' +choices[1] + ' ' +'|' +choices[2]+ '|' +' ' + '|' +choices[3]+ ' ' +'|')
  print('|'+ choices[4]+ ' ' +'|' +choices[5] + ' ' +'|' +choices[6]+ '|' +' ' + '|' +choices[7]+ ' ' +'|')
  print('|'+ choices[8]+ ' '+'|' +choices[9] + '|' +choices[10]+ '|' + ' |' +choices[11]+ '|')
  print('|'+ choices[12]+ '|'+choices[13] + '|' +choices[14]+ '|' + '|' +choices[15]+ '|')
  print('===============')

printbox()

