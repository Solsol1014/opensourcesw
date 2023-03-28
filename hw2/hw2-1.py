f = open("README.txt", "r")

data = f.read()
f.close()

datalist = data.split()

#print(datalist)

count = {}

for i in datalist:
    if i in count:
        count[i] = count.get(i)+1
    else:
        count[i] = 1

for i in count:
    print("{} {}".format(i, count.get(i)))