import sqlite3
from django.shortcuts import render
from raterapi.models import Game, GameReview
from raterreports.views import Connection

def most_reviews(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            cmd = """
            SELECT 
                count(gr.game_id) as reviews,
                g.title
            FROM raterapi_gamereview gr
            JOIN raterapi_game g ON g.id = gr.game_id
            GROUP BY g.title
            ORDER BY reviews DESC
            """
            db_cursor.execute(cmd)

            dataset = db_cursor.fetchall()
            
            game_reviews = []

            for row in dataset:
                game = GameReview()
                game.title = row['title']
                game.review = row['reviews']

                game_reviews.append(game)
            
            template = 'reviews/most_reviews_list.html'
            context = {
                'most_reviews': game_reviews
            }

            return render(request, template, context)
