-- CREATE DATABASE "pet_hotel";

-- owners 
CREATE TABLE "owners" (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR (80) UNIQUE NOT NULL
);

-- pets 
CREATE TABLE "pets" (
    "id" SERIAL PRIMARY KEY,
    "owner_id" INT REFERENCES "owners" ON DELETE CASCADE,
    "name" VARCHAR (80) NOT NULL,
    "breed" VARCHAR (100) NOT NULL,
    "color" VARCHAR (80) NOT NULL,
    "checked_date" DATE DEFAULT NULL,
    "checked_in" BOOLEAN NOT NULL
);

INSERT INTO "owners" ("name")
VALUES ('John B'), ('John S'), ('George'), ('Jason');

INSERT INTO "pets" ("owner_id", "name", "breed", "color", "checked_date", "checked_in")
VALUES 
(1, 'Fluffy', 'Golden Retriever', 'Gold', NULL, TRUE),
(1, 'Snuffy', 'Hamster', 'Brown', NULL, TRUE),
(2, 'Bingo', 'Fish', 'Orange', NULL, TRUE),
(2, 'Slinky', 'Snake', 'Black', NULL, TRUE),
(3, 'Jack', 'Rabbit', 'White', NULL, TRUE),
(3, 'Sher Khan', 'Tiger', 'Orange', NULL, TRUE),
(4, 'Sparkles', 'Unicorn', 'Rainbow', NULL, TRUE),
(4, 'Flipper', 'Dolphin', 'Grey', NULL, TRUE);


-- CREATE TABLE "petowner"