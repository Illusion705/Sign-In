users = {}

commands = [
	"$help: Shows a list of commands.",
	"$sign_out: Signs you out of your account.",
	"$show_apps: Shows you your applications.",
	"$download_app {app name}: Allows you to download applications to your account.",
	"$open_app {app name}: Allows you to open an app."
]

def sign_in_options():
	print("")
	
	option_selected = False
  
	while not option_selected:
		sign_in_option = input("Choose An Option {Sign In} or {Create Account}: ")

		if sign_in_option == "Sign In":
			sign_in()
			option_selected = True
		elif sign_in_option == "Create Account":
			create_account()
			option_selected = True
		else:
			print("Option Invalid")
			print("")
			
def sign_in():
	print("")
	
	sign_in_complete = False
	
	while not sign_in_complete:
		username = input("Enter Username: ")

		if not username == "$back":
			password = input("Enter Password: ")

			if username in users:
				if users[username]["Password"] == password:
					log_in(username)
					sign_in_complete = True
				else:
					print("The username or password is incorrect.")
			else:
				print("The username or password is incorrect.")	
		else:
			sign_in_options()
			sign_in_complete = True
			
def create_account():
	print("")
	
	valid_username = False
	while not valid_username:
		username = input("Select A Username: ")
		
		if not username == "$back":
			if not username in users:
				index1 = 0
				while index1 < len(username) - 1:
					if username[index1] in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "_"]:
						valid_username = True
					else:
						valid_username = False
						index = len(username) - 1
					index1 += 1
			else:
				print("This username already exists.")
		else:
			sign_in_options()
			valid_username = True
			return 0
	
	verified_password = False
	while not verified_password:
		password = input("Select A Password: ")
		
		if not username == "$back":
			if input("Verify Password: ") == password:
				verified_password = True
			else:
				print("The passwords didn't match up.")
		else:
			sign_in_options()
			verified_password = True
			return 0
	users[username] = {}
	users[username]["Password"] = password
	print("Your account was successfully created.")
	sign_in_options()
	
def log_in(username):
	print("Welcome " + username + "! Use \"$help\" if you need a list of commands.")
	command = input("Enter Command: ")
	if command == "$help":
		index1 = 0
		while index1 < len(commands) - 1:
			print(commands[index1])
			index1 += 1
			
sign_in_options()
			
