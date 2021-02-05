import sqlite3
from django.shortcuts import render
from raterapi.models import GameReview
from raterreports.views import Connection


def top_3_reviewers(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            cmd = """
            SELECT 
                count(gr.player_id)  as reviews,
                u.first_name || ' ' || u.last_name as fullname
            FROM raterapi_gamereview gr
            JOIN raterapi_player p ON p.id = gr.player_id
            JOIN auth_user u ON u.id = p.user_id
            GROUP BY fullname
            ORDER BY reviews DESC
            LIMIT 3
	        """

            db_cursor.execute(cmd)

            dataset = db_cursor.fetchall()

            top_reviewers = []

            for row in dataset:
                review = GameReview()
                review.name = row['fullname']
                review.review = row['reviews']

                top_reviewers.append(review)

            template= 'reviews/top_3_reviewers_list.html'
            context = {
                'top_3_reviewers': top_reviewers
            }
            
            return render(request, template, context)
