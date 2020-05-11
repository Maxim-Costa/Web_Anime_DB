#!/usr/bin/python
# coding:utf-8
import cgi
import json
import requests
import unidecode



def Template(title, image):
    TemplateData = f"""
        <a class="card" href="anime.py?animeName={title}">
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
    html = f"""
    <!DOCTYPE html>
    <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title> Anime </title>
            <link rel="stylesheet" href="./css/style.css" />
        </head>
        <body>
            <div class="list" id="style-1">
                {body}
            </div>
        </body>
    </html>
    """
    print(html)


body = ""
jsonFile = ["./json/data.json", "./json/data1.json"]

for i in jsonFile:
    with open(i, 'r', encoding="utf-8") as fp:
        dico = json.load(fp)
        dico = dico["Anime"]
        for k, v in dico.items():
            body += Template(k, v["image_url"])

htmlprint(body)
