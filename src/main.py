from textnode import TextNode, text_type_bold

def main():
    node1 = TextNode("My Text", text_type_bold, "http://sth.com")
    print(node1)

if __name__ == "__main__":
    main()