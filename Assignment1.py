"""
Task 1: Keyword Highlighter

Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
"""

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it.",
]

for item in reviews:
    if "bad" in item:
        item = item.replace("bad", "BAD")
        print(item)
    elif "good" in item:
        item = item.replace("good", "GOOD")
        print(item)
    elif "excellent" in item:
        item = item.replace("excellent", "EXCELLENT")
        print(item)
    elif "poor" in item:
        item = item.replace("poor", "POOR")
        print(item)
    elif "average" in item:
        item = item.replace("average", "AVERAGE")
        print(item)
        break


"""
Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.

"""


reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it.",
]

positive_words = [
    "good",
    "excellent",
    "great",
    "awesome",
    "fantastic",
    "superb",
    "amazing",
]
negative_words = [
    "bad",
    "poor",
    "terrible",
    "horrible",
    "awful",
    "disappointing",
    "subpar",
]

positive_count = 0
negative_count = 0

for item in reviews:

    for word in positive_words:
        if word in item:
            positive_count += item.count(word)
    for word in negative_words:
        if word in item:
            negative_count += item.count(word)


print(positive_count)
print(negative_count)

# expected output is 2 for positive and 1 for negative because it is looking for "poor" not "Poor" as it is in the review.
# this part confused me at first but then I noticed the uppercae P, not sure if that makes sense.


"""
Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
"""
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it.",
]


for item in reviews:
    summary = item[:30].rsplit(" ", 1)[0]
    print(summary + "...")
