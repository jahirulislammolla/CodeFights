def htmlEndTagByStartTag(startTag):

    result = ['<', '/']
    position = 1
    while startTag[position] != ' ' and startTag[position] != '>':
        result.append(startTag[position])
        position += 1
    result.append('>')
    return ''.join(result)
