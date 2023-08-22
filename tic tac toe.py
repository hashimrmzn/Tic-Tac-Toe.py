



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



print("Player 1 use X")
print("Player 2 use #")
#apni conditions add krni ha !

while not winner and iterations <16:
  printbox()

  iterations +=1

  if firstplayer == True:
    print('Player 1 :', end = '')
  else:
    print('Player 2 :',end = '')

  try:
    playerinput = int(input())
  except:
    print('Please enter the value in the box ')
    continue
  

  #hum check kr rhy hain agr phle sy udr koi mark hua ha ya nhi
  if choices[playerinput]=='X' or choices[playerinput]=='#':
    print('yh move thk nhi thi ')
    continue

  if firstplayer:
    choices[playerinput ] = 'X'
  else:
    choices[playerinput ] = '#'

  firstplayer = not firstplayer

  #indexing kidr place krna ha or kon sa khali ha box

  for index in range(0,4):
    if (choices[index*4]==choices[((index*4)+1)] and choices[index*4]==choices[((index*4)+2)]and choices[index*4]==choices[((index*4)+3)]):
      winner = True
      printbox()

    if (choices[index]==choices[index+4]and choices[index+4]==choices[index+8] and choices[index+8]==choices[index+12]):
      winner = True
      printbox()


  if((choices[0]==choices[5]and choices[5]==choices[10] and choices[10]==choices[15]) or
     (choices[3]==choices[6]and choices[6]==choices[9])and choices[9]==choices[12]):
     winner = True
     printbox()

if winner:
  print('Player '+str(int(firstplayer+1))+ ' wins, Congratualetions !')
else:
  print("game draw ho gae ")

