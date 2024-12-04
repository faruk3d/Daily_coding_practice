# open a file
# with open("ex_my_file.txt", mode = "r") as file:
#     content = file.read()
#     print(content)

# write in a file, mode: w, r, a
with open("ex_my_file.txt", mode = "a") as file:
    file.write("\nNew text.")