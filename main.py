import csv


def read_csv_lines(file_path):
    lines_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            title = line['Title'].strip()
            lyrics = line['Lyrics'].strip()
            lines_dict[title] = lyrics
    return lines_dict


def search_sequence_in_dict(dictionary, sequence):
    res = []
    for index, value in dictionary.items():
        value_str = ''.join(value)
        sequence_str = ''.join(sequence)
        if sequence_str in value_str:
            res.append(index)
    return res


def extract_first_letters(lines_dict):
    result_dict = {}
    for line_number, line in lines_dict.items():
        words = line.split()
        first_letters = []
        for word in words:
            for char in word:
                if char.isalnum():
                    first_letters.append(char.lower())
                    break
        result_dict[line_number] = ''.join(first_letters)
    return result_dict


if __name__ == '__main__':
    filename = 'songs.csv' 
    result = read_csv_lines(filename)
    res = extract_first_letters(result)
    while (True):
        print("Please enter the sequence:")
        inp = input()
        print(search_sequence_in_dict(res, inp))
