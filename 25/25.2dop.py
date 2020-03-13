from collections import defaultdict
words = defaultdict(list)
for i in sorted([input().lower() for i in range(int(input()))]):
    words[''.join(sorted(i))].append(i)
for i in words:
    if len(words[i]) > 1 and len(set(words[i])) > 1:
        print(' '.join(sorted(list(set(words[i])))))
