import sqlite3
from django import db
from django.shortcuts import render
from raterapi.models import Game
from raterreports.views import Connection

def more_than_5(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            cmd = """
            SELECT
                g.title,
                g.num_players
            FROM raterapi_game g
            WHERE g.num_players > 5 """

            db_cursor.execute(cmd)

            dataset = db_cursor.fetchall()
            
            games_with_more_than_5 = []

            for row in dataset:
                game = Game()
                game.title = row['title']
                game.num_players = row['num_players']

                games_with_more_than_5.append(game)
            
            template = 'players/more_than_5_players_list.html'
            context = {
                'more_than_5': games_with_more_than_5
            }

            return render(request, template, context)
