"""
get the user's name.
Print the menu options "(H)ello\n(G)oodbye\n(Q)uit".

get the choice and convert it to uppercase.
While choice is not equal to 'Q', do the following:
If choice is 'H', then print "Hello" followed by the name.

Otherwise, if choice is 'G', then print "Goodbye" followed by the name.
If neither of the above, print "Invalid choice".

Print the menu options again "(H)ello\n(G)oodbye\n(Q)uit".

Input the choice again and convert it to uppercase.

Print "Finished."
"""
name = input("Please enter your name:")
print(("(H)ello\n(G)oodbye\n(Q)uit"))

choice = input(">>>").upper()

while choice !='Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>>").upper()

print("Finished.")