def display_chars(file_name, num_of_chars):
    with open(file_name) as file:
        partial_data = file.read(num_of_chars)
        print(partial_data)
       # file.close()



def display_lines(file_name):
    with open(file_name) as file:
        print(file.readline().rstrip("\n"), end = " ; ")
        print(file.readline().rstrip("\n"), end = " ; ")
        print(file.readline().rstrip("\n"))

display_lines("library.txt")



def display_text(file_name):
    with open(file_name) as file:
       text = file.read()
       print(text)


def run_task2():
    display_chars("library.txt", 16)
    display_lines("Library.txt")
    display_text("library.txt")

run_task2()



