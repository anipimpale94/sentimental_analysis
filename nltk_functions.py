import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

english_stopwords = set(stopwords.words('english')) 
def get_tokenized_list(line):
    tokenizer = RegexpTokenizer(r"[\w']+")
    word_tokens = tokenizer.tokenize(line)
    content = [w for w in word_tokens if w.lower() not in english_stopwords]
    return content 
    