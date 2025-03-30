s = " i like this program very much "

# Strip leading/trailing spaces, split into words, reverse, and join
# reversed_s = ' '.join(s.split()[::-1])
reversed_s = ' '.join(reversed(s.split()))

print(reversed_s)
