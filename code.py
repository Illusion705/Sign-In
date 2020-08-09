users = {
			
		}

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

		if not username == "*back":
			password = input("Enter Password: ")

			if username in users:
				if users[username]["Password"] == password:
					log_in()
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
		
		if not username == "*back":
			if not username in users:
				pass
			else:
				print("This username already exists.")
		else:
			sign_in_options()
			valid_username = True
	
def log_in():
	pass
