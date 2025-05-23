from itertools import permutations
def solve_cryptarithmetic(words, result):
    unique_letters = set("".join(words) + result)
    if len(unique_letters) > 10:
        print("Too many unique letters (more than 10), cannot solve!")
        return
    unique_letters = list(unique_letters)
    for perm in permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))
        if any(mapping[word[0]] == 0 for word in words + [result]):
            continue
        word_values = [sum(mapping[char] * (10 ** i) for i, char in enumerate(word[::-1])) for word in words]
        result_value = sum(mapping[char] * (10 ** i) for i, char in enumerate(result[::-1]))
        if sum(word_values) == result_value:
            print("Solution Found!")
            for key, value in mapping.items():
                print(f"{key} = {value}")
            return
    print("No solution found.")
words = ["SEND", "MORE"]
result = "MONEY"
solve_cryptarithmetic(words, result)