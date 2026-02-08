from copy import copy_all_from_source_to_target
from generate import generate_pages_recursive


def main():
    copy_all_from_source_to_target("static", "public")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
