"""
Make HTML File with HTML Data Class
The program takes in all of the elements form the different dataclasses and puts them into the actual HTML file
with adding onto one large string which will be put into an actual html file and opened at the end of the
program as well.
"""
import webbrowser
import os
import css_reader as CSS

def make_html_file(html):
    title = html.title_text
    paragraphs = html.paragraphs
    images = html.images

    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>
        """
    html_template += title + "</title>\n" + CSS.get_template(html)
    html_template += "</head>\n <body>\n"
    html_template += "<h1>" + title + "</h1>\n"
    for paragraph in paragraphs:
        html_template += "<h2>" + paragraph.header + "</h2>\n"
        html_template += "<p>" + paragraph.text + "</p>\n"
    for image in images:
        html_template += '<img src="' + image.path + '"'
        if image.width:
            html_template += ' width="' + image.width + '">\n'
    html_template += "</body>\n" + "</html>\n"
    return html_template


def main(html):
    f = open('mywebsite.html', 'w')
    f.write(make_html_file(html))
    f.close()
    filename = "file://" + os.getcwd() + '/' + 'mywebsite.html'
    webbrowser.open_new_tab(filename)
