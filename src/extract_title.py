def extract_title(markdown: str):
    if "#" not in markdown:
        raise Exception("NO h1 tags in this markdown")
    splited = markdown.split('#')
    if splited[0] == '':
        return splited[1].strip()
    return splited[2].strip()


