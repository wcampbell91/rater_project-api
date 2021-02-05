import sqlite3
from django.shortcuts import render
from raterapi.models import Game
from raterreports.views import Connection

def games_with_no_images(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            cmd = """
            SELECT count(g.title) as 'No Images'
            FROM raterapi_game g
            WHERE g.game_image = ''
            """

            db_cursor.execute(cmd)
            
            dataset = db_cursor.fetchall()

            games_with_no_images = []

            for row in dataset:
                games_with_no_images.append(row['No Images'])

            template = 'images/games_with_no_images_list.html'
            context = {
                'games_with_no_images': games_with_no_images
            }

            return render(request, template, context)
