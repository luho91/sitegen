from transformer import markdown_to_html_node
from extract import extract_title
from pathlib import Path


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        from_content = f.read()

    with open(template_path, "r") as t:
        template_content = t.read()

    html = markdown_to_html_node(from_content).to_html()
    title = extract_title(from_content)
    new_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html).replace("href=\"/", f"href=\"{basepath}").replace("src=\"/", "src=\"{basepath}")

    dst = Path(dest_path)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(new_content, encoding="utf-8")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    root = Path(__file__).resolve().parents[1]
    template_path = (root / template_path).resolve()

    src = Path(dir_path_content)
    if not src.is_absolute():
        src = root / src
    src = src.resolve()

    dst = Path(dest_dir_path)
    if not dst.is_absolute():
        dst = root / dst
    dst = dst.resolve()

    if not dst.exists():
        dst.mkdir(parents=True, exist_ok=True)

    content = list(src.iterdir())

    for el in content:
        if el.is_file() and el.suffix == ".md":
            rel = el.relative_to(src)
            new_name = (dst / rel).with_suffix(".html")
            generate_page(el, template_path, new_name, basepath)
        if el.is_dir():
            new_dst = dst / el.name
            generate_pages_recursive(el, template_path, new_dst, basepath)
