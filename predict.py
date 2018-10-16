''' files containing the functions of prediction '''

# libraries import
import pandas as pd

# files import
from nltk_functions import get_tokenized_list

class prediction:    

    def __init__(self, train_set, test_set):
        self.train_set = train_set
        self.test_set = test_set
        # model = Word2Vec.load_word2vec_format('/data/vectors.bin', binary=True)

    # train modal
    # def train_modal(self):
    #     model = Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4)
    #     model.save("word2vec.model")

    # end point for the class to get accuracy
    def get_accuracy(self, no_of_nearest_neighbor):
        total_count = len(self.test_set)
        total_hits = 0
        for index in range(0, total_count):
            # print(test_set.at[index, 'Label'], test_set.at[index, 'Data'])
            prediction_result = self.get_prediction(self.test_set.at[index, 'Data'], no_of_nearest_neighbor)
            if prediction_result == int(self.test_set.at[index, 'Label']):
                total_hits += 1
        return total_hits * 100 / total_count

    # end point for the class to predict sentiment
    def get_sentiments(self, input_data, no_of_nearest_neighbor):
        return self.get_prediction(get_tokenized_list(input_data), no_of_nearest_neighbor)

    # add different distant formula here
    # calculate distance using formula
    def calculate_trivial_distance(self, list1, list2):
        # string1_word_list = string1.split()
        # string2_word_list = string2.split()  
        common_elements_length = len(set(list1)-(set(list1) - set(list2)))     
        return 0 if common_elements_length < 1 else 1/common_elements_length

    # main prediction function
    def get_prediction(self, word_list, no_of_nearest_neighbor):
        distance_dict = {}
        for index in range(0, len(self.train_set)):
            # distance formula can be changed here
            distance = self.calculate_trivial_distance(word_list, self.train_set.at[index, 'Data'])
            if distance > 0:
                distance_dict[index] = distance
        nearest_neighbor = sorted(distance_dict, key=distance_dict.get, reverse=True)
        index = 0
        while(True):
            index += 1
            if index < len(nearest_neighbor) - 1:
                if nearest_neighbor[index] == nearest_neighbor[index+1]:
                    continue
            if not(index < int(no_of_nearest_neighbor)):
                break
        # print(index)
        score = 0
        selected_neighbors = nearest_neighbor[0:index]
        for item in selected_neighbors:
            score += int(self.train_set.at[item, 'Label'])
            #print(item, int(self.train_set.at[item, 'Label']), str(self.train_set.at[item, 'Data']))
        return 1 if score >= len(selected_neighbors)/2 else 0
