# /robotafm/motor/interface.py
# Main web interface, contains basic
# information display

# imports:
import xml.dom.minidom
from flask import Flask, render_template

# constants:
LANG = "./lang/rus.xml"

# XML: load text strings from language file
dom = xml.dom.minidom.parse(LANG)
main_title = dom.getElementsByTagName("main_title")[0].childNodes[0].nodeValue
language = dom.getElementsByTagName("language")[0].childNodes[0].nodeValue
greeting = dom.getElementsByTagName("greeting")[0].childNodes[0].nodeValue
invitation = dom.getElementsByTagName("invitation")[0].childNodes[0].nodeValue
main_page_text = dom.getElementsByTagName("main_page_text")[0].childNodes[0].nodeValue

# Flask init:
app = Flask(__name__)

# Main site page:
@app.route('/')
def index():
    return render_template(
        'index.html', 
        main_title=main_title, 
        greeting=greeting,
        invitation=invitation,
        main_page_text = main_page_text
        )

