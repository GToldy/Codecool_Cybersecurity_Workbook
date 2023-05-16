import os

def main():
    path = './Sources/'
    files = folder_reader(path)

    for filename in files:
        data = file_reader(f'{path}{filename}').splitlines()
        create_markdown_file(data)

    create_sidebar(files)


def create_markdown_file(data):
    lines = []
    filename = data[1].replace(" ", "_")
    main_path = f'docs/{data[0]}'
    answers_path = f'{main_path}/{filename}'

    if not os.path.exists(answers_path):
        os.makedirs(answers_path)

    main_file = f'{filename}.md'

    opened_file = open(f'{main_path}/{main_file}', 'w', encoding='utf-8')

    for index, line in enumerate(data, 0):
        if index == 0:
            pass
        elif index == 1:
            lines.append(f'# {line}')
        else:
            lines.append(f'#### {line}\n[filename]({filename}/{convert_string(line)}.md \':include :type=code\')')
            answer_file = open(f'{answers_path}/{convert_string(line)}.md', 'w', encoding='utf-8')
            answer_file.write(convert_string(line))
            answer_file.close()
    opened_file.write('\n\n'.join(lines))
    opened_file.close()


def create_sidebar(files):
    lines = {
        'title': '* Cybersecurity Mildestones Workbook\n',
        'headers': {}
    }
    sidebar = open('_sidebar.md', 'w', encoding='utf-8')

    for filename in files:
        data = file_reader(f'./Sources/{filename}').splitlines()
        if data[0] not in lines['headers'].keys():
            lines['headers'].update({data[0]: []})
        
        if data[1] not in lines['headers'][data[0]]:
            lines['headers'][data[0]].append(data[1])
        
    lines['headers'] = dict(sorted(lines['headers'].items(), key=lambda item: item[0]))
    sorted(lines['headers'][data[0]])

    _sidebar = [lines['title']]

    for key, value in lines['headers'].items():
        header = key.split('_')
        print(' '.join(header))
        print(value)
        _sidebar.append(f'\t* Security {" ".join(header)}')
        for line in value:
            _sidebar.append(f'\t\t* [{line}](docs/{key}/{convert_string(line)}.md)')

        
    sidebar.write('\n'.join(_sidebar))
    sidebar.close
    # * Security Basics I
    #     * [PC and OS basics](docs/Basics_I/pc_and_os_basics.md)
    #     * [Linux basics](docs/Basics_I/linux_basics.md)
    #     * [Network basics](docs/Basics_I/network_basics.md)

    # * Security Basics II
    #     * []()
    #     * []()

    # * Security Basics III
    #     * []()
    #     * []()
    pass


def folder_reader(path):
    files = os.listdir(path)
    return files


def file_reader(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        file.close()
    return data


def convert_string(str):
    for key, value in characters.items():
        str = str.replace(key, value)
    return str


characters = {
    ':': '',
    '?': '',
    '/': '%',
    ' ': '_',
    ',': '',
    '-': '',
    '"': ''
}


if __name__ == "__main__":
    main()