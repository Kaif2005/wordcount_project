from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    
    if worddictionary == {}:
        return render(request, 'home.html')

    most_rep_word = max(worddictionary, key=worddictionary.get)
    sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    total_len = 0
    for word in wordlist:
        len_of_each_str = len(word)
        total_len += len_of_each_str
    print(total_len)

    just_one = False
    if worddictionary[most_rep_word] == 1:
        just_one = True

    return render(request, 'count.html', {'fulltext':fulltext, 'wordcount':len(wordlist), 'worddictionary':worddictionary.items(), 'most_rep_word':most_rep_word, 'total_characters':total_len, 'just_one':just_one, 'sortedWords':sortedWords})

def about_page(request):
    return render(request, 'about.html')
