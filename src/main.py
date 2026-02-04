from textnode import TextNode, TextType



def main():
    n = TextNode("This is some anchor text", TextType.LINK, "www.hdf.de")
    print(n)



if __name__ == "__main__":
    main()
