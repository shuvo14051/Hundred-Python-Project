li = [[10, 20, 30], 
      [40, 50, 60], 
      [70, 80, 90]]

output = []
index = 0

for i in range(len(li[0])):
    output.append([])
    for j in range(len(li)):
        output[index].append(li[j][index])
    index+=1
x,y,z = output[0],output[1],output[2]
print(x,y,z)


