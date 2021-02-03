CREATE VIEW GAMES_BY_RATING AS
SELECT 
    g.title,
    g.id,
    r.rating
FROM raterapi_gamerating r
JOIN raterapi_game g ON r.game_id = g.id
