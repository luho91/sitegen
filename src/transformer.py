def markdown_to_blocks(markdown):
    arr = markdown.split("\n\n")
    r = []
    for l in arr:
        l = l.strip()
        if l == "":
            continue
        else:
            r.append(l)

    return r
