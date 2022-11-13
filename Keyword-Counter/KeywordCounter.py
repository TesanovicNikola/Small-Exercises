from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

with open('AllData.txt', encoding="utf8") as f:      #Opening the .txt file, have to use utf8 encoding because there are different languages in the file
    data_set =f.read()                                      #reading the file
    for char in '., \n':                                    #filtering out , and .
        data_set = data_set.replace(char,' ')

    data_set=data_set.lower()                               #lowering all upper case letters
    split_it = data_set.split()                             #turning the data into a list
    k = Counter(filter(lambda x: len(x) >= 5, split_it))    #removing words that have less then 5 words
    Counter = dict(k.most_common(20))                       #counting the most common

    labels, values = zip(*Counter.items())                   #Packing the values to be usable in graphs
    indSort = np.argsort(values)[::-1]                       #Sorting the values in a descending order

    labels = np.array(labels)[indSort]                       #rearanging the data
    values = np.array(values)[indSort]

    indexes = np.arange(len(labels))                         #indexing the values


    plt.style.use('seaborn-whitegrid')                       #adding a grid to make the histogram pretty
    plt.bar(indexes, values)                                                            #ploting the histogram
    plt.title('Histogram of the most occurring words in the articles', fontsize=18)     #title of the histogram
    plt.xticks(indexes, labels)                                                         #making it so the words are displayed on the histogram
    plt.xticks(fontsize=7.5)                                                            #regulating the font size of the word so they dont overlap
    plt.ylabel('Number of occurrences', fontsize=16)                                    #labeling y
    plt.xlabel('Words', fontsize=16)                                                    #labeling x
    plt.show()                                                                          #opening the graph
