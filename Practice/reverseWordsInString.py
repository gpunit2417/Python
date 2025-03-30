# s = " i like this program very much "

# # Strip leading/trailing spaces, split into words, reverse, and join
# # reversed_s = ' '.join(s.split()[::-1])
# reversed_s = ' '.join(reversed(s.split()))

# print(reversed_s)


# s = "Geeks for Geeks"

# # Split the string into words
# words = s.split()

# # Initialize an empty string to store the result
# reversed_words = ""

# # Iterate through the words in reverse order
# for word in reversed(words):
#     reversed_words += word + " "

# # Strip the trailing space
# reversed_words = reversed_words.strip()

# print(reversed_words)


# Input string
# s = "Geeks for Geeks"

# # Split the string into words
# words = s.split()

# # Reverse the words using a stack
# stack = []
# for word in words:
#     stack.append(word)

# reversed_words = ""
# while stack:
#     reversed_words += stack.pop() + " "

# # Strip the trailing space
# reversed_words = reversed_words.strip()

# # Output the result
# print(reversed_words)


s = "Geeks for Geeks"

# Recursive function to reverse words
def reverse_words(words):
    if not words:
        return ""
    return words[-1] + " " + reverse_words(words[:-1])

# Split the string and call the recursive function
reversed_words = reverse_words(s.split()).strip()

print(reversed_words)
