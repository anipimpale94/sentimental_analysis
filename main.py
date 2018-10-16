''' Start point of the code which consist the main function '''

# libraries import
import sys

# files import
from load_data import load_dataset
from predict import prediction


def main():
    # get nearest neighbor count
    if len(sys.argv) < 2:
        print("Please enter number of nearest neighbor:")
        no_of_nearest_neighbor = input()
    else:
        no_of_nearest_neighbor = sys.argv[1]

    # load dataset
    print("Please put the dataset in data folder(named test.txt and train.txt)")
    train_set, test_set = load_dataset()

    print("Length of test set is %d and length of train set is %d" % (len(train_set), len(test_set)))

    # predictions
    p = prediction(train_set, test_set)
    print("Select option- 1: Get Accuracy from test set, 2: Get Sentimental Analysis")
    option = int(input())
    if(option == 1):
        print(p.get_accuracy(no_of_nearest_neighbor))
    else:
        if(option == 2):
            print('Input string to get sentiments:')
            input_data = input()
            print(p.get_sentiments(input_data, no_of_nearest_neighbor))
        else:
            print("Invalid option")
    
if __name__ == "__main__":
    main()