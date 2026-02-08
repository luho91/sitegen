import sys

from copy import copy_all_from_source_to_target
from generate import generate_pages_recursive


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    copy_all_from_source_to_target("static", "public")
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
