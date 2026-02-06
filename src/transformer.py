from textnode import text_to_textnodes


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


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for b in blocks:
        text_nodes = text_to_textnodes(b)

