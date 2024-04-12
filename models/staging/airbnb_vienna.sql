WITH weekdays AS (
  SELECT
    "realSum"                     AS realSum,
    "room_type"                   AS room_type,
    "room_shared"                 AS is_shared_room,
    "room_private"                AS is_private_room,
    "host_is_superhost"           AS is_superhost,
    "multi"                       AS is_multi_rooms,
    "biz"                         AS is_business,
    "bedrooms"                    AS bedrooms,
    "person_capacity"             AS person_capacity,
    "cleanliness_rating"          AS cleanliness_rating,
    "guest_satisfaction_overall"  AS guest_satisfaction_rating,
    "dist"                        AS central_distance,
    "metro_dist"                  AS metro_distance,
    "lng"                         AS longitude,
    "lat"                         AS latitude,
    'vienna'                   AS city,
     FALSE                        AS is_weekend,
  FROM AIRBNB.AIRBNB."airbnb_vienna"
),
weekends AS (
  SELECT
    "realSum"                     AS realSum,
    "room_type"                   AS room_type,
    "room_shared"                 AS is_shared_room,
    "room_private"                 AS is_private_room,
    "host_is_superhost"           AS is_superhost,
    "multi"                       AS is_multi_rooms,
    "biz"                         AS is_business,
    "bedrooms"                    AS bedrooms,
    "person_capacity"             AS person_capacity,
    "cleanliness_rating"          AS cleanliness_rating,
    "guest_satisfaction_overall"  AS guest_satisfaction_rating,
    "dist"                        AS central_distance,
    "metro_dist"                  AS metro_distance,
    "lng"                         AS longitude,
    "lat"                         AS latitude,
    'Amsterdam'                   AS city,
     TRUE                         AS is_weekend,
  FROM  AIRBNB.AIRBNB."airbnb_vienna"
)

SELECT * FROM weekdays
UNION ALL
SELECT * FROM weekends
