f = open("26_demo.txt")
data = f.readlines()
for i in range(len(data)):
    data[i] = int(data[i])

mark = (sum(data) // len(data))**2
print(mark)