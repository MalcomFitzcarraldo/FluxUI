from bs4 import BeautifulSoup
import markdown

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
html_doc.head.append(html_doc.new_tag('title', string='FluxUI'))

# Add meta tag for page refresh
meta = html_doc.new_tag('meta', **{'http-equiv': 'refresh', 'content': '50000'})
html_doc.head.append(meta)

style = html_doc.new_tag('style')
style.string = '''
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    background-color: #000000;
    color: #ffffff;
}
.content {
    border: 2px solid #ccc;
    padding: 20px;
    border-color: #02FE37;
    background-color: #131313;
}
code {
    background-color: #131313;
    border: 1px solid #FED50B;
    border-radius: 4px;
    padding: 5px;
}
pre code {
    display: block;
    padding: 10px;
    overflow: auto;
    background: #131313;
    border-radius: 3px;
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

print(f"HTML file created at {output_file_path}")



