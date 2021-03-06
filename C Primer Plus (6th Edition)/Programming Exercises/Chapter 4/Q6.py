'''
C Primer Plus
Chapter 4 Exercise 6:
Write a program that requests the user’s first name and then the user’s last name. Have 
it print the entered names on one line and the number of letters in each name on the 
following line. Align each letter count with the end of the corresponding name, as in the 
following:
Melissa Honeybee 
      7        8

Next, have it print the same information, but with the counts aligned with the beginning
of each name.
Melissa Honeybee 
7       8
'''

first_name, last_name = input("Enter your first and last name (e.g.: Melissa Honeybee): ").split()

print("%s %s" % (first_name, last_name))

print("%*lu %*lu" % 
        (
        int(len(first_name)), len(first_name), 
        int(len(last_name)), len(last_name))
        )

print()

print("%s %s" % (first_name, last_name))
print("%-*lu %-*lu" % 
        (
        int(len(first_name)), len(first_name), 
        int(len(last_name)), len(last_name))
        )
