from django.shortcuts import render

from AyDictionary import AyDictionary

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def translate(request):
    search = request.GET.get('search')
    dictionary = AyDictionary()
    meaning = dictionary.meaning(search)
    synonym = dictionary.synonym(search)
    antonym = dictionary.antonym(search)
    return render(request, 'pages/translate.html', {'meaning': meaning, 'synonyms': synonym, 'antonyms': antonym})
