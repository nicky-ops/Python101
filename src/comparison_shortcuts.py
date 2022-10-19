# EVALUATES TO TRUE
something = {"Item1",67}

if something:
    print("this is True")
else:
    print("this is false")

# EVALUTES TO FALSE
something = {}

if something:
    print("this is True")
else:
    print("this is false")

# EVALUATES TO TRUE
something = ("Item1",67)
if something:
    print("this is True")
else:
    print("this is false")

# EVALUATES TO FALSE
something = ()
if something:
    print("this is True")
else:
    print("this is false")

# EVALUATES TO TRUE
something = ["Item1",67]
if something:
    print("this is True")
else:
    print("this is false")

#EVALUATES TO FALSE
something = []
if something:
    print("this is True")
else:
    print("this is false")