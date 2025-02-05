def read_write_file(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)
    print(len(file_contents.split()))

def char_count(path_to_file):
    with open(path_to_file) as f:
        file_contents_lower = f.read().lower()
    freq = {}
    for c in file_contents_lower:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    return freq

def sort_on(dic):
    return dic["count"]

def sort_dic(dic):
    list_dic = []
    for c in dic:
        list_dic.append({"char": c, "count": dic[c]})
    list_dic.sort(reverse=True, key=sort_on)
    return list_dic

def print_report(sorted_list_of_dics):
    for dic in sorted_list_of_dics:
        if dic["char"].isalpha():
            print(f"The '{dic["char"]}' character was found {dic["count"]} times")

def main():
    path_to_file = "books/frankenstein.txt"
    print_report(sort_dic(char_count(path_to_file)))

if __name__ == '__main__':
    main()
