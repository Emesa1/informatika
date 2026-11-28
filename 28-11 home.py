f = open("26_demo.txt")
data = f.readlines()
for i in range(len(data)):
    data[i] = int(data[i])
# data.sort()
mark = (sum(data) // len(data))**2
dual = []
for i in range(len(data) -1):
    if data[i] * data[i+1] > mark:
        dual.append((data[i], data[i+1]))
        # break
print(dual)