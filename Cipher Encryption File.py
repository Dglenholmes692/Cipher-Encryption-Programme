#Importing the randint function from the random libary
from random import randint

#Declaring the alphabet constant
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

#This function allows for a new sheet to be generated with the .txt file ext
#It will allow each new file to be named with OTP (ie. OTP0.txt OTP1.txt etc)
def generate_otp(sheets, length):
    for sheet in range (sheets):
        with open ("otp" + str(sheet) + ".txt", "w") as f:
            for i in range (length):
                f.write(str(randint(0,26))+"\n")

#This bit of code creates a new function called load_sheet.
#It then reads ("r") the file and the splitlines syntax breaks each line into a single item and removes the new line syntax as well
def load_sheet(filename):
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents

#This allows the user to input a message it will convert the message to all lowercase so that it's easier to encrypt
def get_plaintext():
    plaintext = input('Please type your message')
    return plaintext.lower()


#These two variables allow the program to read the otp.txt file and it will also allow a user to save (hence the write permission) text to the files also 

def load_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents

def save_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)
#The first part of the code declares another variable = Encrypt
#It then tells the program to check each position in the character and keep a note of it (enumerate)
#Finally it runs a test to see if the character is present within the alphabet, if it's not then it will add it to the ciphertext string
#if it is then the position of the character is found(Alphabet.index..)
#it will then be added to the value from the same position on the sheet from the OTP (int(sheet[position]))
#Finally the modulo operator is used to work out the maths behind the encryption and then the number is converted into a letter hence %26                
def encrypt (plaintext,sheet):
    ciphertext = ""
    for position, character in enumerate(plaintext):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) + int(sheet[position]))% 26
            ciphertext += ALPHABET[encrypted]
    return ciphertext

#This is literally the same code for the function above except instead of an addition its a subtraction as it's decrypting the message whereas the function above encrypted it
def decrypt(ciphertext, sheet):
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += ALPHABET[decrypted]
    return plaintext

#This is the start of the menu function. It will allow the user to choose between 4 options as seen below
#Followig this, it will have 4 statements which will execute dependant on the users choice
def menu():
	choices = ['1', '2', '3', '4']
	choice = '0'
	while True:
		while choice not in choices:
			print('What would you like to do?')
			print('1. Generate one-time pads')
			print('2. Encrypt a message')
			print('3. Decrypt a message')
			print('4. Quit the program')
			choice = input('Please type 1, 2, 3 or 4 and press Enter ')
#The first if statement asks the user how many one-time pads and then the length of the message
#This will then assign the values to the relevent variables and call the function (generate_otp)
			if choice == '1':
				sheets = int(input('How many one-time pads would you like to generate? '))
				length = int(input('What will be your maximum message length? '))
				generate_otp(sheets, length)
#The following elif statement will ask the user to type in the filename of the otp which will have been generated(otp1.txt etc)
#it will then assign the value to the sheet variable and then call the load_sheet function
#It will also call the get_plaintext function and following this it will assign a value to the ciphertext variable by using the encrypt function
#Using the filename variable based on the users input, it will assign both variables using the filename and the ciphertext values within the save_file function 
			elif choice == '2':
				filename = input('Type in the filename of the OTP you want to use ')
				sheet = load_sheet(filename)
				plaintext = get_plaintext()
				ciphertext = encrypt(plaintext, sheet)
				filename = input('What will be the name of the encrypted file? ')
				save_file(filename, ciphertext)
#This statement is similar to the one above except it calls the load_file function and does the reverse of the statement above 
			elif choice == '3':
				filename = input('Type in the filename of the OTP you want to use ')
				sheet = load_sheet(filename)
				filename = input('Type in the name of the file to be decrypted ')
				ciphertext = load_file(filename)
				plaintext = decrypt(ciphertext, sheet)
				print('The message reads:')
				print('')
				print(plaintext)
#This is a simple statement if the user chooses the 4th option then the program will end and the choice will be reset to 0
			elif choice == '4':
				exit()
			choice = '0'

menu()
