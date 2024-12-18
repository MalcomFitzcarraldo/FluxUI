from bs4 import BeautifulSoup
# BeautifulSoup4
import markdown
import random
import time
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)
colors = [ Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Back.BLACK, Back.GREEN, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE
]
def get_random_color():
    return random.choice(colors)

# Read the content of the Markdown file
input_file_path = r'C:\FluxUI\temp\output.txt'
try:
    with open(input_file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
except FileNotFoundError:
    print(f"The file at {input_file_path} was not found.")
    input("Press Enter to exit...")
    exit()

# Convert Markdown to HTML
html_content = markdown.markdown(markdown_text, extensions=['fenced_code'])

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Create a new HTML document
html_doc = BeautifulSoup("<html><head></head><body></body></html>", 'html.parser')
html_doc.head.append(html_doc.new_tag('FluxUI', string='FluxUI'))

# Add meta tag for page refresh
meta = html_doc.new_tag('meta', **{'http-equiv': 'refresh', 'content': '2'})
html_doc.head.append(meta)

# Add favicon 
favicon = html_doc.new_tag('link', rel='icon', href='file:///C:/FluxUI/back/web/flux-fav-work.png', type='image/png')
html_doc.head.append(favicon)

style = html_doc.new_tag('style')
style.string = '''
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    background-color: #474545;
    color: #ffffff;
}
.content {
    border: 5px dotted #ccc;
    padding: 20px;
    border-color: #FE9900;
    background-color: #131313;
    color: #ffffff;
}
code {
    background-color: #131313;
    border: 1px solid #FED50B;
    border-radius: 1px;
    padding: 5px;
}
pre code {
    display: block;
    padding: 1px;
    overflow: auto;
    background: #131313;
    border-radius: 1px;
}
'''
html_doc.head.append(style)

# Add local Prism.js files for syntax highlighting
prism_css = html_doc.new_tag('link', rel='stylesheet', href='file:///C:/FluxUI/plugins/prism.min.css')
prism_js = html_doc.new_tag('script', src='file:///C:/FluxUI/plugins/prism.min.js')
html_doc.head.append(prism_css)
html_doc.body.append(prism_js)

body = html_doc.body
body.append(html_doc.new_tag('h1', string='Markdown Content'))

div = html_doc.new_tag('div', attrs={'class': 'content'})
div.append(soup)
body.append(div)

# Convert to string and write to an HTML file
output_file_path = r'C:\FluxUI\temp\output.html'
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(str(html_doc.prettify()))
os.system('cls')
print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "FluxUI" + Style.RESET_ALL)
print(Fore.GREEN + "")
print(Fore.GREEN + Style.BRIGHT + "Responding in browser...")
print(Fore.GREEN + "")
for i in range(2):
    random_color = get_random_color()
    print(random_color + f"Cached at {output_file_path}")
