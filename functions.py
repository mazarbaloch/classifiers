#parameter with default value prefix='pro'

def add_prefix(my_string, prefix='pro_'):
    """Adds a 'pro_' prefix before the string provided, a default value."""
    return prefix + my_string
final_string=input("Enter a string so we can put pro_ in front of it!:  ")
print(add_prefix(final_string))


def add_number(first,second):
	return first+second
first=int(input('enter some number'))
second=int(input('enter second number'))
print(add_number(first,second))