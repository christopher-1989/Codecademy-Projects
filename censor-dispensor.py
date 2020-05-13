# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "learning algorithms", "her", "herself"]
negative_words = ["concerned", "behind", "dangerous", "danger", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]
list_of_terms_to_censor = proprietary_terms + negative_words


class Word:
    def __init__(self, word, position):
        self.word_lower = word.lower()
        self.word = word
        self.capital_test = word[0].isupper()
        self.position = position

    def get_next_word(self, position):
        return self.position + 1

def create_Words(list):
    count = 0
    class_word_list = []
    for word in list:
        class_word = Word(word, count)
        class_word_list.append(class_word)
        count+=1
    return class_word_list

def censor_function(email_listed, censor_terms, censored_list=[]):
    if email_listed == []:
        return censored_list    
    sentence = email_listed.pop(0)
    for term in censor_terms:
        sentence_lower = sentence.lower()
        if term in sentence.lower():
            term_length = len(term)
            term_position = sentence_lower.find(term)
            print("Term to be censored: " + term + " found at : " + str(term_position))
            sentence_lower = sentence.replace(term, "##" + term + "##")
    censored_list.append(sentence)
    return censor_function(email_listed, censor_terms, censored_list)

def email_to_sentences(email):
    return [line for line in email.split("\n")]

def sentence_to_wordlist(sentence):
    sentence_listified = []
    for word in sentence_listified:
        sentence_listified.append(word.split(" "))
    return sentence_listified

email_word_list = [word for word in email_one.split(" ")]
class_word_list = create_Words(email_word_list)
for word in class_word_list:
    print(word.word)




