SECURE =(('s' , '$'), ('and', '&'), ('a', '*'),('i', '!'),('1','l'),('2','z'),
	('3','u'),('4','p'),('5','r'),('6','d'),('7','t'),('8','b'),('9','q'),('0','o'))

def securepassword(password):
	for a,b in SECURE:
		password = password.replace(a, b)
	return password


if __name__ == '__main__':
	password = input("Enter your password : ")
	password = securepassword(password)
	print(f"your password is : {password}")