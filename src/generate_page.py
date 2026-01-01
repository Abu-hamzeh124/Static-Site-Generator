import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")

	with open(from_path, "r", encoding="utf-8") as f:
		markdown = f.read()

	with open(template_path, "r", encoding="utf-8") as f:
		template = f.read()

	html_content = markdown_to_html_node(markdown).to_html()
	title = extract_title(markdown)

	output = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
	output = template.replace('href="/', f'href="{dest_path}').replace('src="/', f'src="{dest_path}')
	dest_dir = os.path.dirname(dest_path)
	if dest_dir:
		os.makedirs(dest_dir, exist_ok=True)

	with open(dest_path, "w", encoding="utf-8") as f:
		f.write(output)

	return None

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	for entry in os.listdir(dir_path_content):
		entry_path = os.path.join(dir_path_content, entry)
		if os.path.isfile(entry_path) and entry_path.endswith(".md"):
			relative_path = os.path.relpath(entry_path, start=dir_path_content).replace(".md", ".html")
			dest_path = os.path.join(dest_dir_path, relative_path)
			generate_page(entry_path, template_path, dest_path)
		elif os.path.isdir(entry_path):
			generate_pages_recursive(entry_path, template_path, os.path.join(dest_dir_path, entry))
			
		    