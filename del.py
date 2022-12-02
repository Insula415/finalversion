title = "test title"
prod = 213194

with open("products.txt", "a") as f:
        f.write(title + " "+ str(prod) + "\n")
    