ex = ["ceci", "est", "un", "exemple", "très", "original"]

with open("output_script.txt", "w") as file_out:
    for elem in ex:
        file_out.write(elem)

print("Succès !")
