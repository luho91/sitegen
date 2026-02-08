from transformer import markdown_to_html_node
from extract import extract_title
from pathlib import Path


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        from_content = f.read()

    with open(template_path, "r") as t:
        template_content = t.read()

    html = markdown_to_html_node(from_content).to_html()
    title = extract_title(from_content)
    new_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dst = Path(dest_path)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(new_content, encoding="utf-8")
