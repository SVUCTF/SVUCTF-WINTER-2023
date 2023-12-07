import random

with open("base_recipe") as f:
    recipes = f.readlines()

output_recipes = [random.choice(recipes) for _ in range(60)]
output_recipes.append("Zlib_Deflate('Dynamic Huffman Coding')")

print("".join(output_recipes))
