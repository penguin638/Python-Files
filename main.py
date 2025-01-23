
with open("students.txt", "w") as file:

    file.write("Lida,101\n")
    file.write("Tara,5\n")
    file.write("Allessandro,12\n")
    file.write("Rafael,46\n")
    file.write("Oli,34\n")
    file.write("Aaron,21\n")
    file.write("Jolie,76\n")
    file.write("Maisie,90\n")
    file.write("Ollie,65\n")
    file.write("Harry,46\n")
    file.write("Ken,83\n")
    file.write("Bayne,99\n")
    file.write("Leila,96\n")
    file.write("Amelia,67\n")
    file.write("Selma,75\n")
    file.write("Sofi,88\n")
    file.write("Tao,32\n")
    file.write("Marlee,90\n")
    file.write("Layla,100\n")
    file.write("Ben,9\n")
    file.write("Letlotlo,10\n")
    file.write("Bram,7\n")
    file.write("Joseph,11\n")
    file.write("Bella,78\n")
    file.write("Axel,2\n")


with open("students.txt", "r") as file:
    for line in file:
        print(line.split(",",1)[0].strip())
        print(line[1])
        

new_line = input("Enter a new name:")

with open("students.txt", "a") as file:
    file.write(new_line + "\n")

with open("students.txt", "r") as file:
    for line in file:
        print(line.split(",",1)[0].strip())

print("Students with a name over 6 characters:")

with open("students.txt", "r") as file:
    for line in file:
        if len(line)>6:
            print(line.split(",",1)[0].strip())

# I tried the extension but ran out of time and couldn't finish, it isnt fixed yet


print("Students test scores:")

with open("students.txt","r") as file:
    for line in file:
        print(line.split(",",1)[1].strip())

# It gives me an IndexError because of the [1], but the string has two parts so I'm not asking for something that doesnt exist?

#This was the start of my code for the extension, but i didnt have time to finish or fix the indexerror above
# name = input("Whose score would you like to see?")

# with open("students.txt","r") as file:
    for line in file:    
        if name in line:
           print(line.strip())

delete = input("Who do you want to delete?")

with open("students.txt","w") as file:
    for line in file:
         if line != delete:
             file.write(line)

