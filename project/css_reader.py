"""
CSS READER
"""
from html_builder import HTML

DEFAULT_STYLE = """
<style>
body {background-image: linear-gradient(180deg, @BACKCOLOR, white);}

.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
h1   {color: @HEADCOLOR;
      font-family: @FONTSTYLE;
      text-align:center;
      }

h2   {color: @HEADCOLOR;
      font-family: @FONTSTYLE;
      text-align: justify;
      }

p    {color: @FONTCOLOR;
      font-family: @FONTSTYLE;
      padding: 30px;
      text-align: justify;
      background-color: white;
      box-shadow: 4px 0 2px -2px rgba(0,0,0,0.4);
      font-size: 14px;
      }
      
</style>
"""

def open_style_file(file_name):
    """
    Open style file takes in the file name submitted by the user and opens to read the file.
    :param file_name: user input
    :return: file.read
    """
    with open(file_name, 'r', encoding="utf-8") as file:
        return file.read()


def replace_symbol(template, html):
    """
    replace symbol takes in the template which is the CSS template and will reaplce the instances of @BACK or @HEAD
    Color and place it into the dataclass in order to store it all together as the CSS file and put it into the
    HTML file later on.
    :param template: the CSS templace
    :param html: html
    :return: css file
    """
    css = template.replace("@BACKCOLOR", html.background_color).replace("@HEADCOLOR", html.header_color).replace("@FONTSTYLE", html.font).replace("@FONTCOLOR", html.paragraph_color)
    return css


def get_template(html):
    """
    Get templace takes and opens the CSS file and saves it into the CSS file
    :param html: html builder
    :return: css
    """
    print("Opening CSS File...")
    file_name = str(input("Input the Name of the CSS File (ex style_template.txt) or nothing for default "))
    if file_name:
        template = open_style_file(file_name)
    else:
        template = DEFAULT_STYLE
    print("Converting File Contents to Data Class...")
    css = replace_symbol(template, html)
    return css
