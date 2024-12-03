
def getBookText(path):
    with open(path) as f:
        return f.read()

def getWordCount(text):
    words = text.split()
    return len(words)

def lowerText(text):
    words = text.lower()
    return words

def charCount(text):
    charCounter = {}
    for word in text:
        for char in word:
            if char not in charCounter:
                charCounter[char] = 1
            elif char in charCounter:
                charCounter[char] += 1
    return charCounter

def sortDict(dict):
    return dict["num"]

def dictList(dict):
    dictList = []
    for item in dict:
        dictList.append({"char": item, "num": dict[item]})
        dictList.sort(reverse=True, key=sortDict)
    return dictList

def main():
    bookPath = "books/frankenstein.txt"
    text = getBookText(bookPath)
    wordCount = getWordCount(text)
    print(f"{wordCount} words found in the document")
    lowercaseText = lowerText(text)
    characterCounts = charCount(lowercaseText)
    print(f"--- Begin report of {bookPath} ---")
    print(f"{wordCount} words found in the document")
    characterCounts = dictList(characterCounts)
    for dict in characterCounts:
        if dict["char"].isalpha():
            print(f"The '{dict["char"]}' character was found {dict["num"]} times")
    print("--- End report ---")

main()