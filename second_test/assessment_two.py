import string

class AssessmentTwo:

    # ===== BASIC =====

    def count_negative_numbers(self, numbers):
        """Return the number of negative values in the list."""
        count = 0
        for i in numbers:
            if i < 0:
                count += 1
        return count

    def average(self, numbers):
        """Return the average of numbers or None if list is empty."""
        if numbers == []:
            return None
        else:
            return int(sum(numbers)/len(numbers))

    def first_and_last(self, items):
        """Return a tuple of (first, last) item or None if list is empty."""
        if items == []:
            return None
        else:
            return (items[0], items[-1])

    def count_consonants(self, text):
        """Return the number of consonants in the string (letters only)."""
        count = 0
        
        for i in text:
            if i.lower() in "bcdfghjklmnpqrstvwxyz":
                count += 1

        return count

    def is_even_length(self, text):
        """Return True if the string length is even."""
        if len(text) % 2 == 0:
            return True
        else:
            return False


    # ===== INTERMEDIATE =====

    def remove_duplicates_preserve_order(self, numbers):
        """Remove duplicates while preserving order."""
        numbers = set(numbers)
        return list(numbers)

    def word_lengths(self, sentence):
        """Return a dictionary mapping each word to its length."""
        s = sentence.split()
        
        word_length = {}

        for word in s:
            word_length[word] = len(word)
        return word_length

    def second_largest(self, numbers):
        """Return the second largest number or None if it doesn't exist."""
        if numbers == []:
            return None
        elif len(numbers) <= 1:
            None
        else:
            numbers = set(numbers)
            numbers = list(numbers)
            numbers.sort()
            return numbers[-2]

    def chunk_list(self, numbers, size):
        """Split list into chunks of given size."""
        chunk = [list(numbers[i:i+size]) for i in range(0, len(numbers), size)]
        return chunk

    def is_anagram(self, s1, s2):
        """Return True if the two strings are anagrams (ignore case & spaces)."""
        s1 = s1.replace(" ", "")
        s2 = s2.replace(" ", "")

        s1 = sorted(s1)
        s2 = sorted(s2)

        if s1 == s2:
            return True
        else:
            return False


    # ===== ADVANCED =====

    def running_sum(self, numbers):
        """Return a list of running sums."""
        pass

    def longest_unique_substring(self, text):
        """Return the length of the longest substring without repeating characters."""
        pass

    def rotate_matrix_90(self, matrix):
        """Rotate a square matrix 90 degrees clockwise."""
        pass

    def validate_palindrome_number(self, n):
        """Return True if integer n is a palindrome."""
        n = str(n)
        if n[0:] == n[::-1]:
            return True

    def generate_pascal_row(self, n):
        """Return the nth row of Pascal's Triangle (0-indexed)."""
        pass

obj = AssessmentTwo()

print(obj.chunk_list([1, 2, 3, 4, 5], 2))