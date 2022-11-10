"""Verify that the prefix and suffix functions work correctly."""

from sentences import get_verb, get_determiner,get_noun,get_prepositional_phrase,get_preposition
import pytest

def test_get_verb():
    # Call the get_verb function.
    past_verb = ["drank", "ate", "grew","laughed","thought","ran","slept","talked","walked","wrote"]
    sing_pres_verb = ["drinks", "eats", "grows","laughs","thinks","runs","sleeps","talks","walks","writes"]
    plur_pres_verb = ["drink", "eat", "grow","laugh","think","run","sleep","talk","walk","write"]
    fut_verb = ["will drink", "will eat", "will grow","will laugh","will think","will run","will sleep","will talk","will walk","will write"]

    for i in range(4):
        word = get_verb(1,"past")
        assert word in past_verb
    for i in range(4):
        word = get_verb(1,"present")
        assert word in sing_pres_verb
    for i in range(4):
        word = get_verb(1,"future")
        assert word in fut_verb
    for i in range(4):
        word = get_verb(2,"past")
        assert word in past_verb
    for i in range(4):
        word = get_verb(2,"present")
        assert word in plur_pres_verb
    for i in range(4):
        word = get_verb(2,"future")
        assert word in fut_verb


def test_get_noun():
    # Call the get_noun function.
    singular_nouns = ["bird", "boy", "car","cat","child","dog","girl","man","rabbit","woman"]
    plural_nouns = ["birds", "boys", "cars","cats","children","dogs","girls","men","rabbits","women"]

    # Verify that the word stored in the variable
    # determ is in the list of single determiners.
    for i in range(4):
        word = get_noun(1)
        assert word in singular_nouns
    for i in range(4):
        word = get_noun(2)
        assert word in plural_nouns


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]
    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_preposistion():
    words = ["about","above","across","after","along","around","at","before","behind","below","beyond","by","despite","except","for","from","in","into","near","of","off","on","onto","out","over","past","to","under","with","without"]
    for i in range(4):
        word = get_preposition()
        assert word in words

def test_get_preposistional_phrase():
    preps = ["about","above","across","after","along","around","at","before","behind","below","beyond","by","despite","except","for","from","in","into","near","of","off","on","onto","out","over","past","to","under","with","without"]
    single_determiners = ["a", "one", "the"]
    plural_determiners = ["some", "many", "the"]
    singular_nouns = ["bird", "boy", "car","cat","child","dog","girl","man","rabbit","woman"]
    plural_nouns = ["birds", "boys", "cars","cats","children","dogs","girls","men","rabbits","women"]


    for i in range(4):
        prep = get_preposition()
        det = get_determiner(1)
        noun = get_noun(1)
        assert prep in preps
        assert det in single_determiners
        assert noun in singular_nouns
    for i in range(4):
        prep = get_preposition()
        det = get_determiner(2)
        noun = get_noun(2)
        assert prep in preps
        assert det in plural_determiners
        assert noun in plural_nouns


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])