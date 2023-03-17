-- Classes => Singular / Capitalized

--     Pet
--     Owner

-- Tables => Plural / Lowercase

--     pets
--     owners

DROP TABLE owners;

DROP TABLE pets;

-- Create Owners / Pets Tables

CREATE TABLE owners(
    id INTEGER PRIMARY KEY,
    name STRING,
    address STRING,
    email STRING,
    phone INTEGER
)

CREATE TABLE pets(
    id INTEGER PRIMARY KEY,
    name STRING,
    age INTEGER,
    breed STRING,
    birthdate INTEGER,
    favorite_treats TEXT,
    last_fed_at DATETIME,
    last_walked_at DATETIME,
    owner_id INTEGER,
        FOREIGN KEY(owner_id) REFERENCES owners(id)
)

-- Alter Tables

ALTER TABLE pets
ADD COLUMN image_url TEXT;

ALTER TABLE pets
RENAME COLUMN xyz TO dob;

-- DELETING COLUMN
ALTER TABLE pets
DROP COLUMN age;

-- Seeding => Populating DB w/ Records

    -- INSERT INTO

    -- C => Create

-- Insert Two Owners

INSERT INTO owners(name, address, email, phone) 
VALUES ('ix', '999 8th st Seattle Wa 90000', 'ix_is_cool@gmail.com', '9991231234');

INSERT INTO owners(name, address, email, phone) 
VALUES ('john', '123 East St Seattle Wa 90000', 'john_is_cool@gmail.com', '123456789');

-- Insert Four Pets

INSERT INTO pets(name, age, breed, favorite_treats, image_url, owner_id) 
VALUES ('Luke', '2', 'domestic longhair', 'bacon', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1631229064/zx6CPsp_d_utkmww.webp', 2);

INSERT INTO pets(name, age, breed, favorite_treats, image_url, owner_id) 
VALUES ('rose', '11', 'domestic longhair', 'house plants', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1631229038/EEE90-E50-25-F0-4-DF0-98-B2-0-E0-B6-F9-BAA89_menwgg.jpg', 1);

INSERT INTO pets(name, age, breed, favorite_treats, image_url, owner_id) 
VALUES ('leia', '2', 'domestic Shorthair', 'bacon', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1631229011/8136c615d670e214f80de4e7fcdf8607--cattle-dogs-mans_vgyqqa.jpg', 2);

INSERT INTO pets(name, age, breed, favorite_treats, image_url, owner_id) 
VALUES ('Chop', '5', 'shiba inu', 'cheese', 'https://res.cloudinary.com/dnocv6uwb/image/upload/v1629822267/cdbd77592e3ef91e8cc1cf67d936f94f_fkozjt.jpg', 1);

-- CRUD Actions

-- API Endpoints

    -- /all => Not Descriptive
    -- /pets => Descriptive 
        -- /pets/1
        -- /pets/2

-- R => Read

SELECT * from pets;

SELECT * FROM pets
WHERE name = "rose";

SELECT * FROM pets
WHERE favorite_treats = "bacon";

SELECT * FROM pets
WHERE age < 50;

-- U => Update

UPDATE pets
SET age = 12, breed = "siamese"
WHERE name = "rose";

UPDATE pets
SET favorite_treats = "cheese"

UPDATE pets
SET dob = 010123
WHERE name = "Luke";

-- D => Destroy

DELETE FROM pets 
WHERE name = "rose";

DELETE FROM pets 
WHERE age > 2;

-- Reading Information Through One to Many Association
-- Between pets And owners

    -- Pet: Luke
    -- Owner: john

    -- Pet: rose
    -- Owner: ix

    -- SORT BY OWNER NAME (Alphabetically)

SELECT pets.name, owners.name as 'owner_name'
FROM pets
JOIN owners ON pets.owner_id = owners.id

-- Many to Many

CREATE TABLE handlers(
    id INTEGER PRIMARY KEY,
    name STRING,
    email STRING,
    phone INTEGER
)

CREATE TABLE appointments(
    id INTEGER PRIMARY KEY,
    time DATETIME,
    request STRING,
    handler_id INTEGER,
    pet_id INTEGER,
        FOREIGN KEY(handler_id) REFERENCES handlers(id),
        FOREIGN KEY(pet_id) REFERENCES pets(id)
)

DROP TABLE appointments;

-- Seed Our New Tables

INSERT INTO handlers (name, email, phone) 
VALUES ('gannie', 'grannie52@gmail.com', '1239087654');

INSERT INTO handlers (name, email, phone) 
VALUES ('dorian', 'blue_boy@gmail.com', '8887776666');

SELECT * FROM handlers;

INSERT INTO appointments (time, request, pet_id, handler_id) 
VALUES ('2022-07-31 00:00:00', 'drop-in', 1,1);

INSERT INTO appointments (time, request, pet_id, handler_id) 
VALUES ('2022-03-01 00:00:00', 'drop-in', 1,1);

INSERT INTO appointments (time, request, pet_id, handler_id) 
VALUES ('2022-06-01 00:00:00', 'drop-in', 1,2);

INSERT INTO appointments (time, request, pet_id, handler_id) 
VALUES ('2022-05-21 00:00:00', 'walk', 2,2);

-- Option 1: Pull All Owners / Use Python To Order 
-- Alphabetically By Name

SELECT * FROM owners;

-- Option 2: SQL Query To Perform Sorting Before
-- Returning Data

SELECT * FROM owners
ORDER BY name ASC;

-- json-server
    -- JSON
    -- Light Introduction to Persisting Data
    -- No Association-Building Capabilities 

-- SQL
    -- Real World Application
    -- More Appropriate for Larger Bodies Of Data

    -- Pet.all()

        -- SELECT * from pets;
        
-- R => Read

SELECT
    pets.name,
    handlers.name,
    appointments.request,
    appointments.time
FROM appointments
JOIN pets
    ON appointments.pet_id = pets.id
JOIN handlers
    ON appointments.handler_id = handlers.id

SELECT DISTINCT
    pets.name,
    handlers.name
FROM appointments
JOIN pets
    ON appointments.pet_id = pets.id
JOIN handlers
    ON appointments.handler_id = handlers.id
AND pets.name = "rose"
