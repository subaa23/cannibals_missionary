boat_side = 'Right'
missionaries_on_right = 3
cannibals_on_right = 3
missionaries_on_left = 0
cannibals_on_left = 0
print('M=',missionaries_on_left, 'C=',cannibals_on_left, '|-----B|', 'M=',missionar
while True:
 missionaries = int(input('No of missionaries or enter 10 to quit : '))
 if missionaries == 10:
 print('You Quit. Game Over!')
 break
 cannibals = int(input('No of cannibals : '))
 if (missionaries + cannibals) != 1 and (missionaries + cannibals) != 2:
 print('Invalid Move')
 continue
 if boat_side == 'Right':
 if missionaries_on_right < missionaries or cannibals_on_right < cannibals :
 print('Invalid Move')
 missionaries_on_right = missionaries_on_right - missionaries
 cannibals_on_right = cannibals_on_right - cannibals
 missionaries_on_left += missionaries
 cannibals_on_left += cannibals
 
 print('M=' ,missionaries_on_left, 'C=',cannibals_on_left, '|B-----|', 'M=',
 
 boat_side = 'Left'
 else:
 if missionaries_on_left < missionaries or cannibals_on_left < cannibals:
 print('Invalid Move')
 
 
 missionaries_on_left = missionaries_on_left - missionaries
 cannibals_on_left = cannibals_on_left - cannibals
 missionaries_on_right += missionaries
 cannibals_on_right += cannibals
 
 print('M=',missionaries_on_left, 'C=',cannibals_on_left, '|-----B|', 'M=',m
 boat_side = 'Right'
 if (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0) o
 print('You Loose')
 break
 if(missionaries_on_left == 3 and cannibals_on_left == 3):
 print('You win')
 break
