# If Statement
is_hot = True
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm cloth")
else:
    print("It's a lovely day")
print("Enjoy your day")

# Logical operator AND and OR and NOT
has_high_income = True
has_good_credit = True
# and
if has_high_income and has_good_credit:
    print("Eligible for loan")
# or
if has_high_income or has_good_credit:
    print("Eligible for loan")

# not
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan second time")

# comparision operator > , < , >= , <= , ==
temperature = 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")






