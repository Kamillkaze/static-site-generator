from textnode import TextNode

def main():
    node1 = TextNode("My Text", "bold", "http://sth.com")
    print(node1.__repr__())

if __name__ == "__main__":
    main()