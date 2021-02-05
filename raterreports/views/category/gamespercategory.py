import sqlite3
from django.shortcuts import render
from raterapi.models import Game, Category
from raterreports.views import Connection

def GamesPerCategory(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            cmd = """
            SELECT COUNT(category_id), name, id
            FROM GAMES_PER_CATEGORY
            GROUP BY name
            """

            db_cursor.execute(cmd)

            dataset = db_cursor.fetchall()

            games_per_category = []

            for row in dataset:
                category = Category()
                category.name = row['name']
                category.id = row['id']
                category.games = row['count(category_id)']

                games_per_category.append(category)
            
            template = 'categories/list_games_per_category.html'
            context = {
                'GamesPerCategory': games_per_category
            }
            
            return render(request, template, context)
