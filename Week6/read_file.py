def search(file_name):
    print("Searching ...")
    with open(file_name, "r") as file:
        for each_line in file:
            line = each_line.rstrip('\n')
            print(f"Looked in {line}")
        print("Done!")
        file.close()

def run_task3():
    search("library.txt")

run_task3()