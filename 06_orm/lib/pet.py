# Pet Attributes: 
# name: TEXT 
# species: TEXT
# breed: TEXT 
# temperament: TEXT

import ipdb

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect('lib/resources.db')

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

class Pet:
    
    # pass

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes

        # Default Argument => None

            # 1 => We Want Database to Assign ID
            # 2 => When We Retrieve Records From DB, We Want the DB-Assigned
            # ID to Take the Place of "None"

    def __init__(self, name, species, breed, temperament, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist

    @classmethod
    def create_table(cls):
        # Write Up SQL To Create pets Table

        sql = """
            CREATE TABLE IF NOT EXISTS pets
                (id INTEGER PRIMARY KEY,
                name STRING,
                species STRING,
                breed STRING,
                temperament STRING)
        """

        CURSOR.execute(sql)

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pets
        """

        CURSOR.execute(sql)

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB

    def save(self):
        
        # ipdb.set_trace()
        
        sql = """
            INSERT INTO pets (name, species, breed, temperament)
            VALUES (?, ?, ?, ?)
        """

        # self.id = CURSOR.lastrowid

        CURSOR.execute(sql, (self.name, self.species, self.breed, self.temperament))

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB

        # Instantiate Pet Class
        # Persist New Instance to pets Table

    @classmethod
    def create(cls, name, species, breed, temperament):

        # Invoking __init__ Method to Instantiate Pet Class
        pet = cls(name, species, breed, temperament)

        # Invoking save() Instance Method to Persist New Instance
        # to DB
        pet.save()

        return pet

        # To Verify Persistence:

            # pets = CURSOR.execute('SELECT * FROM pets')
            # [pet for pet in pets]

    # ✅ 6. Add "get_newest_pet" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB

    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB

    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB

        # If No "pet" Found, return "None"

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

        # If No "pet" Found, return "None"

    # ✅ 10. Add "find_or_create_by" Class Method to:

        #  Find and Retrieve "pet" Instance w/ All Attributes

        # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes
