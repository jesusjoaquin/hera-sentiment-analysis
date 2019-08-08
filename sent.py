from travelentity import TravelEntity
import json


LODGING = 'marriott.json'
FOOD = 'shake_shack.json'
ACTIVITY = 'dave.json'


def main():
    marriot = TravelEntity('Marriot')
    shake = TravelEntity('Shake Shack')
    dave = TravelEntity('Dave & Busters')

    load_reviews(LODGING, marriot)
    load_reviews(FOOD, shake)
    load_reviews(ACTIVITY, dave)

    marriot.find_sent()
    shake.find_sent()
    dave.find_sent()

    marriot.report_sent()
    shake.report_sent()
    dave.report_sent()



# Reads in the reviews from a given file and adds them to the given travel
# entity
def load_reviews(filename, travel_entity):

    # Load in the json file
    with open(filename, 'r') as file:
        data = json.load(file)

    # Extract the reviews from the json
    reviews = data['reviews']

    # Insert each review into the TravelEntity instance
    for rev in reviews:
        travel_entity.insert_review(rev)



if  __name__ == '__main__':
    main()

