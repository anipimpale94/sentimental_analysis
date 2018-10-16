''' Used for loading the data from file to python data structure format '''

# libraries import
import pandas as pd
import os

# files import
from nltk_functions import get_tokenized_list

def load_dataset():
    test_set = read_data_file('test.txt')
    train_set = read_data_file('train.txt')
    return train_set, test_set

def read_data_file(filename):
    file_path = os.path.join('.\\data', filename)
    data_list = []
    with open(file_path, 'r') as f:
        for line in f:            
            # word_list = line.split(' ')
            # data_item = ' '.join(word_list[1:])
            # stop_words = set(stopwords.words('english')) 
            # word_tokens = word_tokenize(data_item)
            # content = [w for w in words if w.lower() not in english_stopwords] 
            # label =  word_list[0]
            line_items = line.split()
            label = line_items[0]
            content = get_tokenized_list(' '.join(line_items[1:]))
            data_list.append([content, label])
        f.close()
    data_frame = pd.DataFrame(data_list, columns=['Data', 'Label'])
    return data_frame


