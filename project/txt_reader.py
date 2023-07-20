"""
Txt Reader
The TXT Reader file works to take in the user named txt file which contains information for the file such as content
images but the style information which is put into the CSS file later called in the make_html function is still done
by user input. Its quite similar to the wizardmode.py file in many ways
"""
from html_builder import HTML, Image, Paragraph
import turtle as tt
#ask about how to open/set the file name to the same file as inserted in html_builder?

colors = ["black", "silver", "gray", "white", "maroon", "red", "purple", "fuchsia", "green", "lime", "olive", "yellow", "navy", "blue", "teal", "aqua", "aliceblue", "antiquewhite", "aquamarine", "azure", "beige", "bisque", "blachedalmond", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "choclate", "coral", "cornflowerblue", "cornsilk", "crimson", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "gainsboro", "ghostwhite", "gold", "goldenrod", "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "limegreen", "linen", "magenta", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "meiumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mintyrose", "moccasin", "najajowhite", "navy", "oldlace", "olive", "olivedrab", "orangered", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "plum", "powderblue", "rosybrown", "royalblue", "saddlebrown", "sandybrown", "seagreen", "seashell", "sienna", "skyblue", "slateblue", "slategrey", "slategray", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "violet","wheat", "whitesmoke", "yellow", "yellowgreen"]


def open_txt(txt_file):
    line_lists = []
    with open(txt_file, 'r', encoding="utf-8") as file:
        for line in file:
            #print(line.strip())
            line_lists.append(line.strip())
    return line_lists


def background_color(html):
    """
    User inputed background color for the CSS file and puts it into the HTML class for background color selection
    :param html:
    :return:
    """
    while True:
        background_colors = input("Choose the name of a color, or in format '#XXXXXX' for the title color: ")
        if background_colors[0] != "#" and background_colors not in colors: # color:
            print("Illegal Format for Choosing Background Color... Please try again.")
        else:
            break
    html.background_color = background_colors


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
        for f in font_list:
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


def write_to_html(line_lists, html):
    """
    write to html takes in the line lists which is the lines in the txt file and html and for each line in the
    line lists if it is equal to either !new_paragraph, !title, or !image it will perform or save the results to a
    different area of the HTML dataclass or split it up in the case of teh !image section in order to make sure that
    the name of the image and the width of the image are saved in the proper palces inside of the image dataclass
    in the html builder function
    :param line_lists:each line in the file
    :param html:html buulder
    :return:htnl
    """
    html.title_text = line_lists[0]
    title = ""
    paragraph_text = ""
    for line in line_lists:
        if "!new_paragraph" in line:
            if title == "":
                continue
            else:
                html.paragraphs.append(Paragraph(title, paragraph_text))
                continue
        elif "!title" in line:
            line_split = line.split()
            title = line_split[1]
            continue
        elif "!image" in line:
            line_split = line.split(" ")
            if len(line_split) == 2:
                html.images.append(Image(line_split[1], ""))
            else:
                html.images.append(Image(line_split[1], line_split[2]))
            continue
        else:
            paragraph_text += line + "\n"
    return html


def main(file):
    html = HTML("", "", "", "", "", "", [], [])
    print("TXT Mode will begin...")
    print("Background Color")
    background_color(html)
    print("Choose Font")
    choose_font(html)
    print("Paragraph Text Color")
    choose_text_color(html)
    print("Heading Color")
    choose_heading_color(html)
    line_lists = open_txt(file)
    write_to_html(line_lists, html)
    return html
