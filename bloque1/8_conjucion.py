# encoding: utf-8

import re

def replaceFirstPerson(word):
    return word[:-2]+"o"

def replaceSecondPerson(word):
    if re.match("\w*(ar)", word):
        return word[:-2]+"as"
    else:
        return word[:-2]+"es"
    
def replaceThirtyPerson(word):
    if re.match("\w*(ar)", word):
        return word[:-2]+"a"
    else:
        return word[:-2]+"e"

def replaceFortyPerson(word):
    if re.match("\w*(ar)", word):
        return word[:-2]+"amos"
    elif re.match("\w*(er)", word):
        return word[:-2]+"emos"
    else:
        return word[:-2]+"imos"

def replaceFivetyPerson(word):
    if re.match("\w*(ar)", word):
        return word[:-2]+"áis"
    elif re.match("\w*(er)", word):
        return word[:-2]+"éis"
    else:
        return word[:-2]+"ís"

def replaceSixtyPerson(word):
    if re.match("\w*(ar)", word):
        return word[:-2]+"an"
    elif re.match("\w*(er)", word):
        return word[:-2]+"en"
    else:
        return word[:-2]+"en"

def presente_indicativo(word):
    if re.match("\w*(ar|er|ir)", word):
        result = list()
        result.append(replaceFirstPerson(word))
        result.append(replaceSecondPerson(word))
        result.append(replaceThirtyPerson(word))
        result.append(replaceFortyPerson(word))
        result.append(replaceFivetyPerson(word))
        result.append(replaceSixtyPerson(word))
        return result
    

from unittest import TestCase, main

class Test(TestCase):
    def test_conjugacion(self):
        self.assertEqual(presente_indicativo('amar'),
                         ['amo', 'amas', 'ama', 'amamos', 'amáis', 'aman'])
        self.assertEqual(presente_indicativo('leer'),
                         ['leo', 'lees', 'lee', 'leemos', 'leéis', 'leen'])
        self.assertEqual(presente_indicativo('batir'),
                         ['bato', 'bates', 'bate', 'batimos', 'batís', 'baten'])
        self.assertEqual(presente_indicativo('ir'),
                         ['o', 'es', 'e', 'imos', 'ís', 'en'])

main()

    