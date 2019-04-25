from SI507project_tools import *
import csv

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

    approach = Approach.query.filter_by(name=approach_data_dictionary["Name"]).first()
    if not approach:
        # First create these instances to be able to refer to
        purpose = get_or_create_purpose(approach_data_dictionary["Purpose"])
        stage = get_or_create_stage(approach_data_dictionary["Stage"], purpose)

        # Now the car instance itself -- complex but mostly only gotta write this once...
        approach = Approach(name=approach_data_dictionary["Name"], purpose_id=purpose.id,stage_id=stage.id, task=approach_data_dictionary["Task"],image=approach_data_dictionary["Image"],time=approach_data_dictionary["Time"],when=approach_data_dictionary["When"],why=approach_data_dictionary["Why"],note=approach_data_dictionary["Note"],output=approach_data_dictionary["Output"],next=approach_data_dictionary["Next"])
        session.add(approach)
        session.commit()

    return approach

# Above functions all tools to be properly invoked in the main_populate function to do the full population of db; they are available should other types of data need to be handled with them (unlikely if you're depending on an existing dataset)

def main_populate(dataset_filename):
    """Accepts dataset filename with expected CSV format. Opens CSV file, loads contents, closes file appropriately, and invokes above functions to populate database"""
    try:
        with open(dataset_filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for ln in reader:
                get_or_create_approach(ln) # ln should be a dictionary
    except:
        return False # Could TODO raise exception to specify what went wrong, but this could be OK



if __name__ == "__main__":
    pass
