Implemented sentimental analysis using k-nearest neighbor
Text was preprocessed using NLTK by removing stop words and non-alphabets, and tokenization

Distance formula used for determining the similarity:
Distance = 1/N where N is the number of same words in two sentences

Dataset:
[Stanford movie review dataset for sentimental analysis](http://nifty.stanford.edu/2016/manley-urness-movie-review-sentiment/)

Accuracy: 60%

Steps:
1) python main.py 
2) Input number of neighbors
3) Select option to find accuracy of test file(you can change it) in data folder or just predict sentiments of input string
