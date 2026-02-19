class PracticeExam:

    # ===== BASIC QUESTIONS =====

    def count_odd_numbers(self, numbers):
        """Return the count of odd numbers in the list."""
        count = 0
        for i in numbers:
            if i % 2 != 0:
                count += 1
        return count

    def sum_list(self, numbers):
        """Return the sum of all numbers in the list."""
        return sum(numbers)

    def reverse_words_order(self, sentence):
        """Reverse the order of words in a sentence."""
        sentence= sentence.split()
        r_sentence = " ".join(reversed(sentence))
        return r_sentence

    def contains_vowel(self, text):
        """Return True if the string contains at least one vowel."""
        vowels = "AEIOUaeiou"
        return any(True for i in text if i in vowels)

    def smallest_number(self, numbers):
        """Return the smallest number in the list or None if empty."""
        if numbers == []:
            return None
        else:
            return min(numbers)


    # ===== INTERMEDIATE QUESTIONS =====

    def remove_vowels(self, text):
        """Return the string with all vowels removed (case-insensitive)."""
        vowels = "AEIOUaeiou"
        non_vowels = [i for i in text if i not in vowels]
        return "".join(non_vowels)

    def count_character_frequency(self, text):
        """Return a dictionary with character frequencies."""
        frequency = {}
        for i in text:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        return frequency
        
    def is_prime(self, n):
        """Return True if n is a prime number, otherwise False."""
        if n <= 1:
            return False
        
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    def flatten_list(self, nested):
        """Flatten a 2D list into a 1D list."""
        flat = []
        if nested == []:
            return []
        else:
            for i in nested:
                for j in i:
                    flat.append(j)
        return flat

    def longest_common_prefix(self, words):
        """Return the longest common prefix among a list of words."""
        #print(prefix)
        if words == []:
            return ""
        
        prefix = words[0]
        for i in words[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                
        return str(prefix)


    # ===== ADVANCED QUESTIONS =====

    def fibonacci_sequence(self, n):
        """Return a list containing the first n Fibonacci numbers."""
        if n == 0:
            return []
        if n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib = self.fibonacci_sequence(n-1)
            nth = fib[-1] + fib[-2]
            fib.append(nth)
            
            return fib
        
    def max_subarray_sum(self, numbers):
        """Return the maximum sum of a contiguous subarray."""
        d = numbers[2] - numbers[1] 
        print(d)
        # tn = numbers[0] + (numbers.index(numbers)-1)(d)
        # print(tn)
        # return sum(numbers)

    def valid_parentheses(self, s):
        """Return True if parentheses are valid."""
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
                #print(stack)
            else: 
                if not stack:
                    return False
        
                last_opener = stack.pop()
                if last_opener != brackets[i]:
                    return False
                
        return len(stack) == 0

    def rotate_left(self, numbers, k):
        """Rotate the list to the left by k positions."""
        if k <= 0 or not numbers:
            return numbers
        
        k = k % len(numbers) 
        
        if k == 0:
            return numbers
        new_numbers = numbers[1:] + [numbers[0]]
    
        return self.rotate_left(new_numbers, k - 1)

    def spiral_matrix(self, n):
        """Return an n x n spiral matrix."""
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1

obj = PracticeExam()

print(obj.spiral_matrix(2))