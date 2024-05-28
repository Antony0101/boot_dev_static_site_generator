import os
from helper import copyDirectory, generate_html, generate_pages_recursive


def main():
    src = "static"
    dest = "public"
    content = "contents"
    template = "src/template.html"
    print(f"Copying directory from {src} to {dest}")
    copyDirectory(src, dest)
    print(f"Generating page from {content} to {dest} using {template}")
    # for file in os.listdir(content):
    #     if file.endswith(".md"):
    #         print(f"Generating {file.replace('.md', '.html')}")
    #         with open(f"{content}/{file}", "r") as f:
    #             markdown = f.read()
    #             html = generate_html(markdown, template)
    #             with open(f"{dest}/{file.replace('.md', '.html')}", "w") as f:
    #                 f.write(html)
    generate_pages_recursive(content, template, dest)
   

if __name__ == "__main__":
    main()