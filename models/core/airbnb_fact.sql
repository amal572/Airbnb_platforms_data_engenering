{{ config(materialized='table') }}

WITH amsterdam AS (
  SELECT *
  FROM {{ ref('airbnb_amsterdam') }}
),

athens AS (
  SELECT *
  FROM {{ ref('airbnb_athens') }}
),

barcelona AS (
  SELECT *
  FROM {{ ref('airbnb_barcelona') }}
),

berlin AS (
  SELECT *
  FROM {{ ref('airbnb_berlin') }}
),

budapest AS (
  SELECT *
  FROM {{ ref('airbnb_budapest') }}
),

lisbon AS (
  SELECT *
  FROM {{ ref('airbnb_lisbon') }}
),

london AS (
  SELECT *
  FROM {{ ref('airbnb_london') }}
),

paris AS (
  SELECT *
  FROM {{ ref('airbnb_paris') }}
),

rome AS (
  SELECT *
  FROM {{ ref('airbnb_rome') }}
),

vienna AS (
  SELECT *
  FROM {{ ref('airbnb_vienna') }}
)

SELECT
  realSum,
  room_type,
  is_shared_room,
  is_private_room,
  is_superhost,
  is_multi_rooms,
  is_business,
  bedrooms,
  person_capacity,
  cleanliness_rating,
  guest_satisfaction_rating,
  central_distance,
  metro_distance,
  longitude,
  latitude,
  city,
  is_weekend
FROM (
  SELECT * FROM amsterdam
  UNION ALL
  SELECT * FROM athens
  UNION ALL
  SELECT * FROM barcelona
  UNION ALL
  SELECT * FROM berlin
  UNION ALL
  SELECT * FROM budapest
  UNION ALL
  SELECT * FROM lisbon
  UNION ALL
  SELECT * FROM london
  UNION ALL
  SELECT * FROM paris
  UNION ALL
  SELECT * FROM rome
  UNION ALL
  SELECT * FROM vienna
)
