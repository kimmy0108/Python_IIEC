# Program to handle multiple errors with one
# except statement
# Python 3

def fun(a):
	if a < 4:

		# throws ZeroDivisionError for a = 3
		b = a/(a-3)

	# throws NameError if a >= 4
	print("Value of b => ", b)
	
try:
	fun(7)
	fun(9)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
	print("Zero Division Error Occurred and Handled Gracefully")
except NameError:
	print("Name Error Occurred and Handled Correctly")
