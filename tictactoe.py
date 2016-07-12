refboard={1:'1',2:'2',3:'3',
	   4:'4',5:'5',6:'6',
	   7:'7',8:'8',9:'9'}	   

theboard={1:' ',2:' ',3:' ',
	   4:' ',5:' ',6:' ',
	   7:' ',8:' ',9:' '}

def check(board,t,l):
	if l==1:
		if board[1]==t and board[2]==t and board[3]==t:
			return True
		if board[1]==t and board[4]==t and board[7]==t:
			return True	
		if board[1]==t and board[5]==t and board[9]==t:
			return True	
	elif l==2:
		if board[1]==t and board[2]==t and board[3]==t:
			return True
		if board[2]==t and board[5]==t and board[8]==t:
			return True	
	elif l==3:
		if board[1]==t and board[2]==t and board[3]==t:
			return True	
		if board[3]==t and board[5]==t and board[7]==t:
			return True	
		if board[3]==t and board[6]==t and board[9]==t:
			return True
	elif l==4:
		if board[1]==t and board[4]==t and board[7]==t:
			return True	
		if board[4]==t and board[5]==t and board[6]==t:
			return True
	elif l==5:
		if board[1]==t and board[5]==t and board[9]==t:
			return True
		if board[3]==t and board[5]==t and board[7]==t:
			return True	
		if board[4]==t and board[5]==t and board[6]==t:
			return True						
		if board[2]==t and board[5]==t and board[8]==t:
			return True
	elif l==6:
		if board[3]==t and board[6]==t and board[9]==t:
			return True		
		if board[4]==t and board[5]==t and board[6]==t:
			return True
	elif l==7:
		if board[1]==t and board[4]==t and board[7]==t:
			return True
		if board[3]==t and board[5]==t and board[7]==t:
			return True
		if board[7]==t and board[8]==t and board[9]==t:
			return True	
	elif l==8:
		if board[7]==t and board[8]==t and board[9]==t:
			return True	
		if board[2]==t and board[5]==t and board[8]==t:
			return True										
	elif l==9:
		if board[3]==t and board[6]==t and board[9]==t:
			return True	
		if board[7]==t and board[8]==t and board[9]==t:
			return True
		if board[1]==t and board[5]==t and board[9]==t:
			return True				

def printboard(board):
	print(board[1]+'|'+board[2]+'|'+board[3])
	print('-+-+-')
	print(board[4]+'|'+board[5]+'|'+board[6])
	print('-+-+-')
	print(board[7]+'|'+board[8]+'|'+board[9])


print('\n\n\n')
printboard(refboard)
print('\n Reference Board')
print('\n\n\n')
printboard(theboard)


print('Please choose who goes first "X" or "0"')
turn=input()
turn=turn.upper()
for i in range(9):
	while True:
		print ('Enter a location for '+turn+' according to reference board')
		location=input()
		location=int(location)
		if theboard[location]==' ':
			break;
		else:
			print('Oops loaction already filled..please select another')
	theboard[location]=turn
	printboard(theboard)
	b=check(theboard,turn,location)
	if(b==True):
		print('Player '+turn+' wins!!')
		break;

	if(turn=='X'):
		turn='0'
	else:
		turn='X'	

	if i==8:
		print('\n')
		print('Match Drawn!!')