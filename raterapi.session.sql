CREATE VIEW GAMES_BY_RATING AS
SELECT 
    g.title,
    g.id,
    r.rating
FROM raterapi_gamerating r
JOIN raterapi_game g ON r.game_id = g.id

CREATE VIEW GAMES_PER_CATEGORY AS
SELECT 
    g.category_id,
    c.name,
    c.id
FROM raterapi_game g
JOIN raterapi_category c ON c.id = g.category_id

DROP VIEW GAMES_PER_CATEGORY
