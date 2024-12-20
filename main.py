
def anagram_checker(str1, str2):
    if str1.strip() == "" or str2.strip() == "":
        return "Enter two valid text."

    return "Anagrams!" if sorted(str1.lower()) == sorted(str2.lower()) else "Not anagrams"


text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

check = anagram_checker(text1, text2)
print(check)