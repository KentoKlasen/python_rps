import random


def main():
	choices = ['rock', 'paper', 'scissor']
	user_choice = False
	while user_choice == False:
		cpu_choice = random.choice(choices)
		user_choice = input('enter a choice (rock, paper, scissor): ')
		print(f'cpu chose {cpu_choice}')
		if user_choice not in choices:
			print('not a valid choice')
			user_choice = False
		else:
			if user_choice == cpu_choice:
				print('tie try again')
				user_choice = False
			elif user_choice == 'rock':
				if cpu_choice == 'scissor':
					print("you win i guess")
				else:
					print('you lose ha')
			elif user_choice == 'paper':
				if cpu_choice == 'rock':
					print("you win i guess")
				else:
					print('you lose ha')
			elif user_choice == 'scissor':
				if cpu_choice == 'paper':
					print("you win i guess")
				else:
					print('you lose ha')




	
















if __name__ == '__main__':
	main()