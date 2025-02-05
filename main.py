def read_write_file(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)
    print(len(file_contents.split()))

def char_count(path_to_file):
    with open(path_to_file) as f:
        file_contents_lower = f.read().lower()
#    freq = {c: file_contents_lower.count(c) for c in file_contents_lower}
    freq = {}
    for c in file_contents_lower:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    return freq

def main():
    path_to_file = "books/frankenstein.txt"
    print(char_count(path_to_file))

if __name__ == '__main__':
    main()
