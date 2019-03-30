import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']

    # split() - seprates a string to different items
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # increase
            worddictionary[word] += 1

        else:
            # add to dictionary
            worddictionary[word] = 1

    sortedWord = sorted(worddictionary.items(),
                        key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedWord': sortedWord})
