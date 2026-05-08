# #nums = [3, 1, 4, 1, 5, 9, 2, 6, 3, 5]
# #Experiment 1
# print(nums[0])
# print(nums[-1])
# print(nums[2:5])
# print(nums[:3])
# print(nums[3:])
# print(nums[::-1])

# #Experiment 2
# #print(len(nums))
# #print(sum(nums))
# #print(max(nums))
# #print(min(nums))
# #print(nums)

# #Experiment 3
# #nums.append(100)
# #print(nums)
# #nums.sort()
# #print(nums)
# #removed = nums.pop()
# #print("removed:", removed)
# #print(nums)

# #Task 1
# words = ["apple", "banana", "cherry", "date", "elderberry"]
# print(words[2])
# print(words[-1])
# print(words[0:3])
# print(words[-2:])
# print(words[::-1])

# #Task 2
# scores = [78, 92, 45, 88, 60, 95, 73]
# print(max(scores))
# print(min(scores))
# print(sum(scores)/len(scores))
# scores.sort(reverse = True)
# print(scores)

# #Task 3
# prices = [19.99, 5.50, 100.00, 250.75, 12.30]
# discounted = []
# for item in prices:
#     new_price = item * 0.9
#     discounted.append(new_price)
# print(discounted)


# --- Dictionaries ---

# user = {
#     "name": "Linus",
#     "age": 55,
#     "country": "USA",
#     "languages": ["C", "Bash", "English"],
# }

# # Experiment 1
# print(user["name"])
# print(user["age"])
# print(user["languages"])
# print(user["languages"][0])

# # Experiment 2
# user["email"] = "linus@example.com"
# print(user)
# user["age"] = 56
# print(user)
# del user["country"]
# print(user)

# # Experiment 3
# # print(user.keys())
# # print(user.values())
# # print(user.items())

# # # Experiment 4
# # print(user.get("name"))
# # print(user.get("phone"))
# # print(user.get("phone", "no phone"))
# # print(user["phone"])

# user = {"name": "Linus", "age": 55, "country": "USA"}

# # Loop over keys (default behavior)
# for key in user:
#     print(key)

# # Loop over values
# for value in user.values():
#     print(value)

# # Loop over both at once (most common in real code)
# for key, value in user.items():
#     print(key, "->", value)




    
# age = 25
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

# temperature = 30
# if temperature > 35:
#     print("Very hot")
# elif temperature > 25:
#     print("Warm")
# elif temperature > 15:
#     print("Mild")
# else:
#     print("Cold")

# fruits = ["apple", "banana", "cherry"]
# if "banana" in fruits:
#     print("Found banana")
# if "watermelon" in fruits:
#     print("Found watermelon")
# else:
#     print("No watermelon here")

#Task 4
# words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
# counts = {}
# for word in words:
#     if word in counts:
#         counts[word] +=1
#     else:
#         counts[word] = 1
# print(counts)

# user = {
#     "name": "Alice",
#     "age": 30,
#     "city": "Paris",
#     "occupation": "engineer",
# }

# for key, value in user.items():
#     print(key, value)

products = [
    {"name": "apple", "price": 1.50, "quantity": 10},
    {"name": "bread", "price": 3.20, "quantity": 5},
    {"name": "milk", "price": 2.80, "quantity": 7},
    {"name": "eggs", "price": 4.50, "quantity": 12},
]

total = 0
for product in products:
    total = total + product["price"] * product["quantity"]
print(total) 