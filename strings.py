def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return 'un{}'.format(word)


def make_word_groups(vocab_words, separator=' :: '):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    prefix = vocab_words[0]
    vocab_words = map(lambda w: prefix+w if w is not prefix else prefix, vocab_words)
    return separator.join(vocab_words)



def remove_suffix_ness(word, suffix='ness'):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    word = word.removesuffix(suffix)
    if word.endswith('i'):
        word = word.replace('i', 'y')
    return word


def adjective_to_verb(sentence, index, point_index=-1):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    if sentence.endswith('.'):
        sentence = sentence[:point_index]
    return sentence.split()[index]+'en'