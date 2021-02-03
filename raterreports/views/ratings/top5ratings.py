import sqlite3
from django.shortcuts import render
from raterapi.models import Game, GameRating
from raterreports.views import Connection

def top_5_ratings_list(request): 
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            cmd = """
            SELECT
                title,
                id,
                rating
            FROM GAMES_BY_RATING
            ORDER BY rating DESC
            LIMIT 5
            """
            db_cursor.execute(cmd)

            dataset = db_cursor.fetchall()

            games_by_rating = {}

            for row in dataset:
                rating = GameRating()
                rating.game = Game()
                rating.game.title = row['title']
                rating.rating = row['rating']

                gid = row['id']

                if gid in games_by_rating:
                    games_by_rating[gid]['ratings'].append(rating)
                else:
                    games_by_rating[gid] = {}
                    games_by_rating[gid]['id'] = gid
                    games_by_rating[gid]['ratings'] = [rating]

            list_of_games_by_rating = games_by_rating.values()

            template = 'ratings/desc_list_with_ratings.html'
            context = {
                'top_5_ratings_list' : list_of_games_by_rating
            }

            return render(request, template, context)
