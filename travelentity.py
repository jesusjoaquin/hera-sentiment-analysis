from textblob import TextBlob


class TravelEntity():

    def __init__(self, name):
        self.name = name
        self.reviews = list()
        self.sentiment = 0

    # Name and sentiment of the instance is reported. Nothing is returned.
    def report_sent(self):
        print('%s sentiment: %f' % (self.name, self.sentiment))

    # Given a review, it adds it to the private list of reviews associated
    # with the instance. Nothing is returned.
    def insert_review(self, review):
        self.reviews.append(review)

    # Utilizing textblob library, the polarity for a given review is returned.
    def _get_polarity(self, review):
        # Review (string) converted to a TextBlob instance.
        rev_blob = TextBlob(review)

        # The polarity attribute of the blob is returned.
        return rev_blob.polarity

    # Sentiment analysis is performed on reviews for the current instance.
    def find_sent(self):
        sent_list = list()

        # The sentiment for each review is found.
        for rev in self.reviews:
            sent_list.append(self._get_polarity(rev))

        # Found sentiments are then averaged.
        self.sentiment = sum(sent_list)/len(sent_list)


