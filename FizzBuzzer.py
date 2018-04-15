  # github.com/sixsixseven

print("\n\n\tFIZZ BUZZ BUZZER\n\n\a\a\a")


	#	Ask user for starting range
start_range = int(input("Please enter a starting range: "))

	#	Ask user for ending range
ending_range = int(input("\nPlease enter an ending range: ")) + 1

	#	Ask user for divisor for Fizz
fizz_div = int(input("\nPlease enter a 'Fizz' divisor: "))

	#	Ask user for divisor for Buzz
buzz_div = int(input("\nPlease enter a 'Buzz' divisor: "))

	#	Print it all.
print("\n\n\n")



for x in range(start_range,ending_range):
	if x % fizz_div == 0:
		print("Fizz")
	if x % buzz_div == 0:
		print("Buzz")
	else:
		print(x)
