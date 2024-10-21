import timeit

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1
    skip = {}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1
    skip[pattern[m - 1]] = m
    i = m - 1
    while i < n:
        j = m - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1
        if j == -1:
            return k + 1
        i += skip.get(text[i], m)
    return -1

def kmp(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = [0] * m
    j = 0
    compute_lps(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def compute_lps(pattern, m, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1

def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    for i in range(m-1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            if j == m - 1:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1

def test_algorithm(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=100)

# Читаємо тексти з файлів
with open('стаття 1.txt', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open('стаття 2.txt', 'r', encoding='utf-8') as f:
    text2 = f.read()

# Підрядки для пошуку
existing_substr = "відрізняється"
non_existing_substr = "xyzabcdefghijk"

algorithms = [
    ("Boyer-Moore", boyer_moore),
    ("KMP", kmp),
    ("Rabin-Karp", rabin_karp)
]

texts = [
    ("Text 1", text1),
    ("Text 2", text2)
]

results = {}

for text_name, text in texts:
    print(f"\nResults for {text_name}:")
    for substr_type, substr in [("Existing", existing_substr), ("Non-existing", non_existing_substr)]:
        print(f"\n  Searching for {substr_type} substring: '{substr}'")
        for alg_name, alg_func in algorithms:
            time = test_algorithm(alg_func, text, substr)
            print(f"    {alg_name}: {time:.6f} seconds")
            results.setdefault(alg_name, []).append(time)

print("\nOverall results:")
for alg_name, times in results.items():
    avg_time = sum(times) / len(times)
    print(f"{alg_name}: {avg_time:.6f} seconds (average)")

fastest_alg = min(results, key=lambda x: sum(results[x]))
print(f"\nFastest algorithm overall: {fastest_alg}")