import cgi
import cgitb
import json
import requests
import unidecode
import time

cgitb.enable()
animeName = cgi.FieldStorage()

if animeName.getvalue("anime"):
    anime = animeName.getvalue("anime")
else:
    raise Exception("no anime")
image = ""
title = ""


def Template(title, image):
    TemplateData = f"""
        <a class="card">
            <div class="card_image">
                <div class="filter">
                    <span class="filter_info">{title}</span>
                    <br>
                    <br>
                    <span class="filter_info">View more</span>
                </div>
                <img
                    src="{image}"
                    alt="{title}"
                />
            </div>
            <div class="card_text">
                <span>{title}</span>
            </div>
        </a>
    """
    return TemplateData

def htmlprint(body):
    print("Content-type: text/html; charset=utf-8\n")
    html = f"""
    <!DOCTYPE html>
    <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title> Anime </title>
        </head>
        <body>
            <div class="list" id="style-1">
                {body}
            """
    time.spleep(5)
    html +="""
            </div>
        </body>
    </html>
    """
    print(html)


htmlprint(anime)
