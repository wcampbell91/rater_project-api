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




# db_cursor.execute("""
#                 SELECT
#                     g.id,
#                     g.title,
#                     AVG(r.value) AS average_rating
#                 FROM
#                     raterprojectapi_game g
#                 JOIN
#                     raterprojectapi_rating r ON r.game_id = g.id
#                 GROUP BY g.title
#                 ORDER BY average_rating DESC
#                 LIMIT 5
#             """)
#             dataset = db_cursor.fetchall()
#             top_games_by_rating = []
#             for row in dataset:
#                 # Create a Game instance and set its properties. String in brackets matches the SQL results
#                 game = Game()
#                 game.title = row["title"]
#                 game.rating = row["average_rating"]
#                 top_games_by_rating.append(game)
#         # Specify the Django template and provide data context
#         template = 'ratings/list_with_top_ratings.html'
#         context = {
#             'topgamerating_list': top_games_by_rating
#         }
