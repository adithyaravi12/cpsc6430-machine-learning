import numpy as np
import pathlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

f = pathlib.Path("C:/Users/ravia/.spyder-py3/")
option = 'y'

file_name = input("Enter the name of your input file: ")
if f.exists():
    f = open(file_name, "r")
    s = f.readline()
    d = s.split("\t")
    rows = int(d[0])

    data= np.zeros([rows, 5])

    for p in range(rows):
        s = f.readline()
        temp = s.split("\t")
        temp[-1] = temp[-1].strip()
            
        for q in range(5):
            if(q<4): 
                data[p,q]= float(temp[q])
            else:
                if(temp[q] == "setosa"):
                    data[p,q] = 0
                elif(temp[q] == "versicolor"):
                    data[p,q] = 1
                elif(temp[q] == "virginica"):
                    data[p,q] = 2
    f.close()
else:
    print("File doesn't exists. Try again")
    file_name = input("Enter a file name:")

    
                              

def graph_plot():
    print("You can do a plot of any two features of the Iris Data set\nThe feature codes are:\n\t0 -> Sepal Length\n\t1 -> Sepal Width\n\t2 -> Petal Length\n\t3 -> Petal Width")
         
    x = int(input("Enter feature code for the horizontal axis: "))
    y = int(input("Enter feature code for the vertical axis: "))
    for i in range(rows):
    
        if data[i,4] == 0:
            plt.scatter(data[i,x], data[i,y], c = "green", marker = "v", label ="setosa")
        elif data[i,4] == 1:
            plt.scatter(data[i,x], data[i,y], c = "blue", marker = "o", label ="versicolor")
        else:
            plt.scatter(data[i,x], data[i,y], color = "red", marker = "+", label ="virginica")
        
    if(x == 0):
        x = "Sepal Length"
    elif(x == 1):
        x = "Sepal Width"
    elif(x == 2):
        x = "Petal Length"
    else:
        x = "Petal Width"
    if(y == 0):
        y = "Sepal Length"
    elif(y == 1):
        y = "Sepal Width"
    elif(y == 2):
        y = "Petal Length"
    else:
        y = "Petal Width"
    
    plt.title("Iris Flower Plot")
    plt.xlabel(x)
    plt.ylabel(y)

    legend_props = [Line2D([0], [0], marker='v', color='white', markerfacecolor='green', label='setosa', markersize=10),
               Line2D([0], [0], marker='o', color='white', markerfacecolor='blue', label='versicolor', markersize=10),
               Line2D([0], [0], marker="+", color ='white', markerfacecolor='red', label='virginica', markersize=10)]
    plt.legend(handles = legend_props)
    plt.show()
    
    
graph_plot()
while option == 'y':        
        option = input("Would you like to do another plot? (y/n): ")
        if option == 'y':
            graph_plot()
        elif option == 'n':
            break;