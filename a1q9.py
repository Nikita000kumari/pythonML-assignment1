# Write a python program that checks if a substring is present in a given string.
main_string = "Hello, world!"
substring = "world"

index = main_string.find(substring)

if index != -1:
    print(f"'{substring}' is found in '{main_string}' at index {index}")
else:
    print(f"'{substring}' is not found in '{main_string}'")











