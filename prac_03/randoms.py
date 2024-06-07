import random

print(random.randint(5, 20))

print(random.randrange(3, 10, 2))

print(random.uniform(2.5, 5.5))


# What did you see on line 1?
# Answer: The output will be a random integer between 5 and 20, inclusive.
# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest number: 5, Largest number: 20

# What did you see on line 2?
# Answer: The output will be 3，5， 7， 9.
# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest number: 3, Largest number: 9
# Could line 2 have produced a 4?
# Answer: Line 2 could not have produced a 4.

# What did you see on line 3?
# Answer: The output will be a random float between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest number: 2.5， Largest number: 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))