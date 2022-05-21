#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:56:00 2022

@author: venkatarevanthnaidudanala
"""


def cleantext(text):
    text = text.lower()
    text = text.strip()
    for letters in text:
        if letters in """[]!.,"-!—@;':#$%^&*()+/?""":
            text = text.replace(letters, " ")
    return text

#Removing duplicate words
def countwords(words, is_spam, counted):
    for each_word in words:
        if each_word in counted:
            if is_spam == 1:
                counted[each_word][1]=counted[each_word][1] + 1
            else:
                counted[each_word][0]=counted[each_word][0] + 1
        else:
            if is_spam == 1:
                counted[each_word] = [0,1]
            else:
                counted[each_word] = [1,0]
    return counted



def make_percent_list(k, theCount, spams, hams):
    for each_key in theCount:
        theCount[each_key][0] = (theCount[each_key][0] + k)/(2*k+hams)
        theCount[each_key][1] = (theCount[each_key][1] + k)/(2*k+spams)
    return theCount

#Main_train
spam = 0
ham = 0
counted = dict()
#redaing the train file
fname = input("Enter the name of the train_spam-ham file:" )
fin = open(fname, "r")
textline = fin.readline()
#reading the stopwords file
stopwords=input("Enter the name of the stopwords file: " )
stopwords_handle=open(stopwords,'r')
stop_words=[]
stop_words_line=stopwords_handle.readline()

while stop_words_line !="":
    stop_words.append(stop_words_line[:1])
    stop_words_line=stopwords_handle.readline()

while textline != "":
    is_spam = int(textline[:1])
    if is_spam == 1:
        spam = spam + 1
    else:
        ham = ham + 1
    textline = cleantext(textline[1:])
    words = textline.split()
    words = set(words)
    words=words.difference(stop_words)
    counted = countwords(words, is_spam, counted)
    textline = fin.readline()
#print(counted)
vocab = (make_percent_list(1, counted, spam, ham))
#print(vocab)
fin.close()
#print(spam_train)
#print(ham_train)

from math import log
import math
#main_test
spam_test = 0
ham_test = 0
counted = dict()
spam_probability=spam/(spam+ham)
ham_probability=ham/(spam+ham)
#print(probability_ham)
#print(probability_spam)
fname_test = input("Enter the name of the test_spam_ham file:" )
fin_test = open(fname_test, "r")
textline_test = fin_test.readline()
test_spam_class=[]
predict_spam_class=[]
while textline_test != "":
    test_spam_class.append(int(textline_test[:1]))
    if (int(textline_test[:1]))==0:
        ham_test=ham_test+1
    else:
        spam_test=spam_test+1
    textline_test = cleantext(textline_test[1:])
    words_test = textline_test.split()
    words_test = set(words_test)
    #predicted_class=predict(vocab,words_test,probability_spam,probability_ham)
    header_spam=0
    header_ham=0
    for word in vocab:
        if word in words_test:
            header_spam=header_spam+log(vocab[word][1])
            header_ham=header_ham+log(vocab[word][0])
        else:
            header_spam=header_spam+log(1-vocab[word][1])
            header_ham=header_ham+log(1-vocab[word][0])
    total_spam_prob=math.exp(header_spam)
    total_ham_prob=math.exp(header_ham)
    bayes=1/(1+(math.exp((log(total_ham_prob)+log(ham_probability))-(log(total_spam_prob)+log(spam_probability)))))
    
    if bayes >= 0.5:
        predict_spam_class.append(1)
    else:
        predict_spam_class.append(0)
    #predict_spam_class.append(predicted_class)
    textline_test = fin_test.readline()
#print(predict_spam_class)
#print(total_spam_prob)
#print(total_ham_prob)
print("no of Spams emails in Test File\t"+str(spam_test))
print("no of Hams emails in Test File\t"+str(ham_test))

FP=0
FN=0
TN=0
TP=0
for i in range(len(test_spam_class)):
    if test_spam_class[i]==0 and predict_spam_class[i]==0:
        TN=TN+1
    elif test_spam_class[i]==1 and predict_spam_class[i]==1:
        TP=TP+1
    elif test_spam_class[i]==0 and predict_spam_class[i]==1:
        FP=FP+1
    elif test_spam_class[i]==1 and predict_spam_class[i]==0:
        FN=FN+1
print("FP:\t"+str(FP))
print("FN:\t"+str(FN))
print("TP:\t"+str(TP))
print("TN:\t"+str(TN))
accuracy=(TP+TN)/(TP+TN+FN+FP)
print("Accuracy:"+str(accuracy))
precision=(TP)/(TP+FP)
print("Precision:"+str(precision))
recall=(TP)/(TP+FN)
print("recall:"+str(recall))
F1score=2*(precision*recall)/(precision+recall)
print("F1Score:"+str(F1score))