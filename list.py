# squares = []
# for i in range(1, 101):
#     squares.append(i**2)
# # print(squares)


# squares2 = [i**2 for i in range(1, 101)]
# # print(squares2)

# remainders5 = [x**2 % 5 for x in range(1, 101)]
# # print(remainders5)

# remainders11 = [x**2 % 11 for x in range(1, 101)]
# # print(remainders11)


# movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone With the wind", "Citizen Kane", "It's a wonderful life", "The wizard of Oz", "Gattaca", "Rear Window", "GhostBusters", "To kill A mockingbird", "Good will Hunting", "Raidars", "Ground Boy ", "Close Encounters of the third kind"]

# gmovies = []
# for title in movies:
#     if title.startswith("G"):
#         gmovies.append(title)

# # print(gmovies)

# gmovieslist = [title for title in movies if title.startswith("G")]
# # print(gmovieslist)
# def count_substring(string, sub_string):
#     return

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

s = input()
result = ""

for letter in s:
    if letter== letter.lower():
        result += letter.upper()
    else:
        result += letter.lower()

print(result)