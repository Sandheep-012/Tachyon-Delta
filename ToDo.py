from random import shuffle

def write():										#Entering the tasks
	print()
	while True:
		To = input("What's to be Done? ")
		if To == 'q':
			break
		with open('theone.txt','a') as f:
			f.write(To + '\n')

def read():											#Listing out the tasks in the file
	with open('theone.txt') as f:
		tasks = f.readlines()

	if len(tasks) != 0:
		print()	
		print('We have to: ')
		print()		
	
		for task in tasks:
			print (f" - {task.rstrip()}")

		print()

	elif len(tasks) == 0:
		print('Nothing to do... ')

def selector():										#Selecting a random task from the bunch
	with open('theone.txt') as i:
		rtask = i.readlines()
	
	shuffle(rtask)

	print()
	print('We have to: ')
	print(rtask[0])

def r_sequence():									#Creating a random sequence of tasks
	with open('theone.txt') as r:
		stask = r.readlines()

	shuffle(stask)

	print()	
	print('We have to: ')
	print()

	n = 1		
	for task in stask:
		print (f" {n}) {task.rstrip()}")
		n = n+1
	print()

def delete():										#Deleting a task but better
	with open('theone.txt') as d:
		dtask = d.readlines()

	if len(dtask) == 0:
		print("A vacuum can't get any emptier!")
	
	else:
		print('whats to be deleted?')
		ToDel = int(input('Here first element is 1, second element is 2 and so on. '))
		
		try:
			
			with open('theone.txt' , 'w') as h:
					h.writelines(dtask)

			print('Mission successful')

		except: 
			print('Wrong input. Error code: Boz(1-1)')
			print()

def adel():												#Deleting all the inputs
	with open('theone.txt', 'r') as c:
		x = c.readlines()
	if len(x) == 0:
		print('Looking into the abyss..')
	
	else:	 
		a = input('Are you Sure? (yes/no) ')
	
		if a == 'yes':
			with open('theone.txt','w') as f:
				f.write('')
			print()
		else:
			print('Ok')

	''' THE MAIN FLOW '''

print('Help? try h !')
read()

while True:
	mode = input("What's my purpose? ")	
  	
	if mode == 'h':
		print()
		print(f"{'*i - input'}\n{'*l - display'}\n{'*r - random'}\n{'*s - random sequence'}\n{'*d - delete'}\n{'*a - delete all'}\n{'*quit - quit'}\n")


	elif mode == 'i':			#input task
		write()
		read()

	elif mode == 'l':			#provide all task
		read()

	elif mode == 'r':			#random mode
		selector()

	elif mode == 's':			#random series of tasks
		r_sequence()

	elif mode == 'd':			#deleter
		delete()

	elif mode == 'a':			#delete all
		adel()

	elif mode == 'quit':
		input('Noooooooooo...                           (press Enter)')
		break

	else:
		print()
		print('Wrong Input. Error code: id10t')
		print()
