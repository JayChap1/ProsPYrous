import math  # Need this for square root calculations - can't do advanced math without the toolbox

# Step 1: First name goes here - keeping it lowercase like my confidence after that first quiz
firstname = "jason"

# Step 2: Last name in all caps - SCREAMING IT BECAUSE WE'RE BEHIND AND NEED TO LOCK IN
lastname = "CHAPMAN"

# Step 3: Time to flip the script - uppercase the first, lowercase the last (Python's version of uno reverse)
print("Hello,", firstname.upper(), lastname.lower())

# Step 4: Two newlines because apparently one isn't enough space to breathe
print("\n\n")

# Step 5: Mashing first and last name together like my schedule this weekend
fullname = firstname + " " + lastname

# Step 6: Slicing out just the last name in one line - surgical precision baby
print(fullname[6:])  # jason is 5 chars + 1 space = index 6 is where CHAPMAN starts

# Step 7: Replacing my last name with "official student status" - making it official
fullname = fullname.replace(lastname, lastname + ", Walsh College Student")
print(fullname)

# Step 8: Dropping some Francis of Assisi wisdom - motivation for this long weekend ahead
print("\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\"")

# Step 9: Two random decimal numbers because math is about to math
num1 = 12.5
num2 = 4.2

# Step 10: All four basic operations - addition, subtraction, multiplication, division (the og squad)
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Step 11: Printing these results FOUR different ways (professor wants variety, professor gets variety)

# Method 1: Concatenation - the OG way, converting everything to strings manually
print(str(num1) + " plus " + str(num2) + " equals " + str(addition))

# Method 2: Percent formatting - old school but still works
print("%s minus %s equals %s" % (num1, num2, subtraction))

# Method 3: .format() method - getting fancier now
print("{} multiplied by {} equals {}".format(num1, num2, multiplication))

# Method 4: F-strings - the best one, saved it for last like dessert
print(f"{num1} divided by {num2} equals {division}")

# Step 12: Square root time - math.sqrt() doing the heavy lifting
sq_root = round(math.sqrt(multiplication), 2)
print(f"The square root of {multiplication} equals {sq_root}")

# Step 13: Storing today's date info - October grind never stops
month = "October"
day = 25

# Step 14: Final output with double tabs because formatting matters (even when we're behind on chapters)
print(f"\n\t\tToday is day {day} of the month of {month}.")

