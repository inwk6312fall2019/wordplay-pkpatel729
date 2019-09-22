def uses_only(word, string_words):

	for letter in word:

		if letter not in string_words:

			return False

	return True


