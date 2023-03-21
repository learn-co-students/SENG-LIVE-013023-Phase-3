
# 3. ✅ CRUD Practice

# To run the file, run `python3 debug.py` in the app directory

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)

# Store code that should only run when your file is executed as a script
# https://realpython.com/if-name-main-python/#in-short-it-allows-you-to-execute-code-when-the-file-runs-as-a-script-but-not-when-its-imported-as-a-module
if __name__ == '__main__':
    
    #3.1 ✅ Uncomment below to create the engine.
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
    
    #3.2 ✅ Uncomment below to create sessions and bind to the engine.
    Session = sessionmaker(bind=engine)
    session = Session()

    #3.3 ✅ Create
    
    # Create a pet and save it to the database with 'session.add' and 'session.commit'
    
    rose = Pet(name="rose", species="cat", breed="domestic longhair", temperament="relaxed", owner_id=1)
    spot = Pet(name="spot", species="dog", breed="boxer", temperament="feisty", owner_id=2)

    # Persisting an Individual Instance to DB
    session.add(rose)
    session.commit()

    # Create multiple pets and bulk save them with  'session.bulk_save_objects' and 'session.commit'

        # Note: Bulk save will not contain the id

    session.bulk_save_objects([rose, spot])
    session.commit()

    # Verify results by checking the db 

    #3.4 ✅ Read
        
    # Retrieve all pets with session.query
        
        # resources = session.query(Resource)

    pets = session.query(Pet)    

    # Print the pets 
    print([pet for pet in pets])

    # Get all of the pet names and print them with session.query
    names = session.query(Pet.name)
    print([name for name in names])

    # Get all the pet names and print them in order with session.query and order_by
    names_in_order = session.query(Pet.name).order_by(Pet.name)
    print([name for name in names_in_order])

    # Get the first pet with session.query and first
    first_pet = session.query(Pet).first()
    print(first_pet)

    # Filter pet by temperament with session.query and filter 
    query_results = session.query(Pet).filter(Pet.temperament.like('%feisty%'))
    
    for record in query_results:
        print(record)

    #3.5 ✅ Update 
        
    # Update the first pet's name and print the updated pet info
    first_pet = session.query(Pet).first()
    first_pet.name = "Bud"
    session.commit()

    # Update all the pets' temperaments to 'cool' and print the pets 
    session.query(Pet).update({Pet.temperament: 'Relaxed'})
    pets = session.query(Pet)
    print([pet for pet in pets])

    #3.6 ✅ Delete
        
    # Delete one item by querying the first pet, deleting it and committing
    first_pet = session.query(Pet).first()
    session.delete(first_pet)

    # Delete all the pets with session.query and .delete
    session.query(Pet).delete()

    pets = session.query(Pet)
    print([pet for pet in pets])

    # optional Break point for debugging and testing
    import ipdb; ipdb.set_trace()