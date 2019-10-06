functions = []
for x in "anz":
    def f():
        return x
    functions.append(f)

for f in functions:
    print(f())
