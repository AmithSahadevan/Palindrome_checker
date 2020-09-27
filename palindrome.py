# Palindrome

input_str = input("Enter your word/number: ")
rev = input_str[::-1] # reversing the string

if input_str == rev:
	print("Yes, it is a palindrome! reversed word =", rev)
else:
	print("No, it is not a palindrome! reversed word =", rev)