# Dictionary is nothing but a key-value pair
# d1 = {}
# print(type(d1))
d2 = {"harry":"Burger",
      "rohan":"fish",
      "skillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti","D":"Chicken"}}

# d2["Ankit"] = "Junk Food"
# d2[420] = "kebabs"
# del d2[420]
# print(d2["Shubham"])
# print(d2.copy())
# d3 = d2.copy()
# del d3["harry"]
# print(d2)
# print(d2.get("harry"))
d2.update({"Leena":"Toffee"})
print(d2)
print(d2.keys())
print(d2.items())