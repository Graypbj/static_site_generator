from textnode import TextType, TextNode

def main():
    new_class = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(new_class)

main()
