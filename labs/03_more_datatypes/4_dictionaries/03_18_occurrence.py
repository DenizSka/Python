'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
input_ = input("please provide a string:")
dict_ = { x: input_.count(x) for x in input_}
print(dict_)
