import errno
import os
import shutil

from blocks import markdown_to_html_node


def copyDirectory(src, dest):
    try:
        filepaths = os.listdir(src)
        if not os.path.exists(dest):
            os.makedirs(dest)
        else:
            shutil.rmtree(dest)
            os.makedirs(dest)
        for file in filepaths:
            src_file = os.path.join(src, file)
            dest_file = os.path.join(dest, file)
            if os.path.isdir(src_file):
                copyDirectory(src_file, dest_file)
                print('Directory copied from %s to %s' % (src_file, dest_file))
            else:
                shutil.copy(src_file, dest_file)
                print('File copied from %s to %s' % (src_file, dest_file))
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)

def extract_title(markdown):
    lines = markdown.split("\n")
    if len(lines) == 0:
        return ""
    if lines[0].startswith("# "):
        return lines[0][2:]
    return ""

def generate_html(markdown, template):
    title = extract_title(markdown)
    body = markdown_to_html_node(markdown)
    template = open(template, "r").read()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", body.to_html())
    return template

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        if file.endswith(".md"):
            print(f"Generating {dest_dir_path}/{file.replace('.md', '.html')}")
            with open(f"{dir_path_content}/{file}", "r") as f:
                markdown = f.read()
                html = generate_html(markdown, template_path)
                with open(f"{dest_dir_path}/{file.replace('.md', '.html')}", "w") as f:
                    f.write(html)
        elif os.path.isdir(f"{dir_path_content}/{file}"):
            os.makedirs(f"{dest_dir_path}/{file}")
            generate_pages_recursive(f"{dir_path_content}/{file}", template_path, f"{dest_dir_path}/{file}")