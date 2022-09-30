from lib2to3.pytree import convert
from num2words import num2words
from random import shuffle 
import pandas as pd
numbers = list(range(0,10000000))
shuffle(numbers)
def preProcess():
    words = []
    nums = []
    for i in numbers:
        nums.append(i)
        words.append(num2words(i))
    df = pd.DataFrame()
    df['nums'] = nums
    df['words'] = words
    return df
# data = preProcess()
# data.to_csv('wordNumber.csv')
data = pd.read_csv('wordNumber.csv')
print(data.head())
print(len(data))