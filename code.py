users = {}

applications = []

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
			
			if not password == "$back":
				if username in users:
					if users[username]["Password"] == password:
						log_in(username)
						sign_in_complete = True
					else:
						print("The username or password is incorrect.")
				else:
					print("The username or password is incorrect.")	
			else:
				sign_in_complete = True
				sign_in_options()
		else:
			sign_in_complete = True
			sign_in_options()
			
def create_account():
	print("")
	
	valid_username = False
	while not valid_username:
		username = input("Select A Username: ")
		
		if not username == "$back":
			if not username in users:
				index1 = 0
				while index1 < len(username) - 1:
					if username[index1] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_":
						valid_username = True
					else:
						valid_username = False
						index1 = len(username) - 1
					index1 += 1
			else:
				print("This username already exists.")
		else:
			valid_username = True
			sign_in_options()
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
			verified_password = True
			sign_in_options()
			return 0

	users[username] = {}
	users[username]["Password"] = password
	print("Your account was successfully created.")
	sign_in_options()
	
def log_in(username):
	print("")
	print("Welcome " + username + "! Use \"$help\" if you need a list of commands.")
	
	exit_cmd = False
	while not exit_cmd:
		print("")
		command = input("Enter Command: ")
		if command == "$help":
			print("")
			index1 = 0
			while index1 < len(commands) - 1:
				print(commands[index1])
				index1 += 1
		elif command == "$sign_out":
			print("You were successfully signed out.")
			exit_cmd = True
			sign_in_options()
			
		elif command == "$show_apps":
			if len(applications) > 0:
				index2 = 0
				print("")
				while index2 < len(applications):
					print(index2 + 1 + ": " + applications[index2])
			else:
				print("You don't have any applications.")
		elif command[0:13] == "$download_app ":
			download(command[14:])
		else:
			print("Invalid command.")
			
sign_in_options()
