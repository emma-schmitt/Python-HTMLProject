"""
Emma Schmitt
HTML Builder Python File
Professor Polak
"""
"""
HTML Builder contains three different dataclasses, including Paragraph, Image, and HTML. Each dataclass refers to 
storing either the user input or the information from the selected txt file in order to compile the HTML file all
at once. In the main file, it calls the given code for bringing up either the wizard or the txt mode calling 
the necessary files for each one
"""
from dataclasses import dataclass
from typing import *


@dataclass
class Paragraph:
    header: str
    text: str



@dataclass
class Image:
    path: str
    width: str


@dataclass
class HTML:
    background_color: str
    font: str
    paragraph_color: str
    title_color: str
    title_text: str
    header_color: str
    paragraphs: list[Paragraph]
    images: list[Image]
    #image_number: list[int] #every index is going to be an integer refering to the number of images and what order they are gonna be in
    #will i have to do same thing for the paragraphs??

import sys
#import files

import css_reader
import txt_reader
import make_html
import wizardmode

def main():

    if len(sys.argv) == 1:
        print('Wizard Mode') #start the wizard mode
        html = wizardmode.main()
        #always saved to index.html
    else:
        file = sys.argv[1] #for reading directly from the files?
        print('Not Wizard Mode')
        html = txt_reader.main(file)
            #call mode that makes the website from the files
            #html_builder
    #css_reader.main(html)
    make_html.main(html)


if __name__ == "__main__":
    main()