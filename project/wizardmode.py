"""
User Input for the Wizard Mode
"""


from html_builder import HTML, Paragraph, Image
from turtle import *
import turtle as tt

colors = ["black", "silver", "gray", "white", "maroon", "red", "purple", "fuchsia", "green", "lime", "olive", "yellow", "navy", "blue", "teal", "aqua", "aliceblue", "antiquewhite", "aquamarine", "azure", "beige", "bisque", "blachedalmond", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "choclate", "coral", "cornflowerblue", "cornsilk", "crimson", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "gainsboro", "ghostwhite", "gold", "goldenrod", "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "limegreen", "linen", "magenta", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "meiumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mintyrose", "moccasin", "najajowhite", "navy", "oldlace", "olive", "olivedrab", "orangered", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "plum", "powderblue", "rosybrown", "royalblue", "saddlebrown", "sandybrown", "seagreen", "seashell", "sienna", "skyblue", "slateblue", "slategrey", "slategray", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "violet","wheat", "whitesmoke", "yellow", "yellowgreen"]


def choose_title(html):
    """
    Makes input for the title and saves it in the HMTL builder under title text
    :param html: html builder file
    :return: none
    """
    title = input("Insert Website Title Name: ")
    html.title_text = title


def background_color(html):
    """
    While the background color input is true, it will prompt the user for the background color and if the
    color is not starting with a # and is not in the overall list of colors which are able to be used in CSS
    it will break out otherwise and finally set the background color inputed by the user into the data class
    :param html: html builder file
    :return: none
       """
    while True:
        background_color = input("Choose the name of a color, or in format '#XXXXXX' for the title color: ")
        if background_color[0] != "#" and background_color not in colors: # color:
            print("Illegal Format for Choosing Background Color... Please try again.")
        else:
            break
    html.background_color = background_color


def choose_font(html):
    """
    Choose font from the font lists and displays it in the turtle if the ser types in yes otherwise it will
    add the font style to the HTML dataclass
    :param html: html builder file
    :return: none
       """
    font_list = ["Arial", "Comic Sans MS", "Lucida Grande", "Tahoma",
                 "Verdana", "Helvetica", "Times New Roman"]
    font = str(input("Do you want to see what the fonts look like?  [yes]"))
    if font == "yes":
        tt.left(90)
        for f in font_list:
            tt.forward(10)
            tt.write(f + ", size 14", font=(f, 14, "bold"))
        tt.done()
        print("Close the window when you have made your choice...")
        # once its closed display the following
    print("Choose a font by its number...")
    for i in range(len(font_list)):
        print(str(i) + ": " + font_list[i])
    font = int(input("Select Font"))
    html.font = font_list[font]


def choose_text_color(html):
    """
    Choose text color works similarly to the choosing of other colors, in which while the user input is returned
    it will say if the text_color at index 0 or at the start of the string is equal to a # to indictate a hash code abd
    the text_color is in the list of valid CSS text colors it will put it into the text_color part of HTML class
    :param html: HTML builder file
    :return: none
    """
    while True:
        text_color = input("Choose the name of a color, or in format '#XXXXXX' for the text color: ")
        if text_color[0] != '#' and text_color not in colors:
            print("Illegal Format for Selecting Text Color... Try Again")
        else:
            break
    html.paragraph_color = text_color


def choose_heading_color(html):
    """
        Choose heading color works similarly to the choosing of other colors, in which while the user input is returned
        it will say if the heading_color at index 0 or at the start of the string is equal to a # to indictate a hash code and
        the text_color is in the list of valid CSS text colors it will put it into the heading_color part of HTML class
        :param html: HTML builder file
        :return: none
        """
    while True:
        header_color = input("Choose the name of a color, or in format '#XXXXXX' for the header color: ")
        if header_color[0] != '#' and header_color not in colors:
            print("Illegal Format for Selecting Text Color... Try Again")
        else:
            break
    html.header_color = header_color


def paragraphs(html):
    """
    Paragraphs is similar to the title funciton where it prompts the user for the header and the content of the
    paragraph which are apart of a different dataclass called paragraph and will append the content to the dataclass
    paragraph.
    :param html: html builder file
    :return: none
    """
    header = input("Choose Header Name: ")
    content = input("Insert Content of your Paragraph (single line): ")
    html.paragraphs.append(Paragraph(header, content))


def image_selector(html):
    """
    Image selector says that while the user input of yes is true it will prompt the user to endter the image name
    and append the image name to the images dataclass as the image name and an empty string in case there is an insertion
    of the width of the image in the txt reader
    :param html: html builder file
    :return: none
    """
    while True:
        image_selection = str(input("Do you want to add images? [yes]"))
        if image_selection == "yes":
            image_name = str(input("Insert Image File Name: "))
        else:
            break
    html.images.append(Image(image_name, ""))


def insert_paragraphs(html):
    """
    Insert paragraphs says that while the user inputs is true and it results in a yes than it will append it to the
    paragraphs portion of the html file
    :param html: html builder file
    :return: none
    """
    #prompts user for all content protaining to the paragraphs
    while True:
        paragraph_result = str(input("Do you want to add paragraphs? "))
        if paragraph_result == "yes":
            print("Header Name and Paragraph Content")
            paragraphs(html)
        else:
            break

def main():
    """
    The main function prints and calls the different functions and messages to the user as well and returns html for the
    user to call to the html_builder the function does the same with the image selector and colors as well.
    :return: html
    """
    html = HTML("", "", "", "", "", "", [], [])
    print("Wizard Mode has Begun...")
    choose_title(html)
    print("Background Color")
    background_color(html)
    print("You will now choose a font")
    choose_heading_color(html)
    choose_text_color(html)
    choose_font(html)
    insert_paragraphs(html)
    print("Images: ")
    image_selector(html)
    return html

