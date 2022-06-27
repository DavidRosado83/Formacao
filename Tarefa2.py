from tkinter.tix import INTEGER
import matplotlib.pyplot as plt
import numpy as np

List = np.array([1, 5, 1, 4, 1, 3, 2, 5, 5, 1, 4, 5, 2, 4, 5,
                 4, 4, 1, 2, 5, 3, 5, 3, 0, 2, 1, 3, 4, 5, 4,
                 5, 2, 5, 3, 0, 4, 5, 1, 4, 0, 4, 4, 1, 2, 1,
                 5, 5, 5, 2, 3])
Soma = np.sum(List)
Max = np.size(List)
Media = Soma / Max
print("Media = ", Media)

List_NVal = np.array([0,0,0,0,0,0])
for i in List:
    List_NVal[i]+=1
print(List_NVal)

x = np.array(["0","1","2","3","4","5"])    
plt.bar(x,List_NVal)
plt.show()

