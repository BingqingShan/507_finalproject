from SI507project_tools import *
import csv

#########################################

def get_or_create_stage(stage_type_str, purpose):
    stagetype = Stage.query.filter_by(name=stage_type_str).first()
    if not stagetype:
        stagetype = Stage(name=stage_type_str)
        stagetype.purposes.append(purpose)
        session.add(stagetype)
        session.commit()
    return stagetype

def get_or_create_purpose(purpose_name):
    purpose = Purpose.query.filter_by(name=purpose_name).first()
    if not purpose:
        purpose = Purpose(name=purpose_name)
        session.add(purpose)
        session.commit()
    return purpose


def get_or_create_approach(approach_data_dictionary):
    """Accepts list of data about a car -- can assume this is a dictionary of the format of a row of the sample cars.csv file -- and uses that to save a new car and build relationships appropriately."""
    # City mpg,Classification,Driveline,Engine Type,Fuel Type,Height,Highway mpg,Horsepower,Hybrid,ID,Length,Make,Model Year,Number of Forward Gears,Torque,Transmission,Width,Year
    ## ^ Copy in headers from CSV file to refer to

    # Decide what makes a car unique to query for it -- under what case do I NOT want to add this row of data?
    # Model Year, automatic_transmission bool val, and torque ...

    # # City mpg,Classification,Driveline,Engine Type,Fuel Type,Height,Highway mpg,Horsepower,Hybrid,ID,Length,Make,Model Year,Number of Forward Gears,Torque,Transmission,Width,Year

    # print(approach_data_dictionary)
    # print(approach_data_dictionary[0])

    approach = Approach.query.filter_by(name=approach_data_dictionary["Name"]).first() # "Find the first car that has this dictionary's same model yr, torque, and value of automatic_transmission -- True if this one should be True and False otherwise" -- transmission data re: looking at data
    if not approach: # If there isn't one like that
        # Then create a new car instance with same var

        # First create these instances to be able to refer to
        purpose = get_or_create_purpose(approach_data_dictionary["Purpose"])
        stage = get_or_create_stage(approach_data_dictionary["Stage"], purpose)

        # Now the car instance itself -- complex but mostly only gotta write this once...
        approach = Approach(name=approach_data_dictionary["Name"], purpose_id=purpose.id,stage_id=stage.id, task=approach_data_dictionary["Task"],image=approach_data_dictionary["Image"],time=approach_data_dictionary["Time"],when=approach_data_dictionary["When"],why=approach_data_dictionary["Why"],note=approach_data_dictionary["Note"],output=approach_data_dictionary["Output"],next=approach_data_dictionary["Next"])
        session.add(approach)
        session.commit()

    return approach
    # Note that this function ^ does NOT allow for updating info easily -- this is showing a simpler version of code that creates if it doesn't exist, but doesn't update existing data thru this manual population format -- if a car with this info exists...

# Above functions all tools to be properly invoked in the main_populate function to do the full population of db; they are available should other types of data need to be handled with them (unlikely if you're depending on an existing dataset)

def main_populate(dataset_filename):
    """Accepts dataset filename with expected CSV format. Opens CSV file, loads contents, closes file appropriately, and invokes above functions to populate database"""
    # We'll use CSV module to handle CSV data
    # First we'll want to run a quick test to see if one of those things works... see in app.py running
    try:
        with open(dataset_filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for ln in reader:
                # print(ln) # an OrderedDict
                get_or_create_approach(ln) # ln should be a dictionary
    except:
        return False # Could TODO raise exception to specify what went wrong, but this could be OK



if __name__ == "__main__":
    pass
