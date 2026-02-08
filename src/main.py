from copy import copy_all_from_source_to_target
from generate import generate_page


def main():
    copy_all_from_source_to_target("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
