def read_write_file(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)
    print(len(file_contents.split()))

def main():
    path_to_file = "books/frankenstein.txt"
    read_write_file(path_to_file)

if __name__ == '__main__':
    main()
