import unittest
from jsonapi.actions.Sendrequest import Sendrequest
import json

class TestCall(unittest.TestCase):

    # Test one to check if the response is correct
    def testRequestone(self):

        mockResponse = [{'author': 'Tia Roberson', 'authorId': 2, 'id': 99, 'likes': 473, 'popularity': 0.34, 'reads': 97868, 'tags': ['culture', 'startups', 'tech']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 95, 'likes': 985, 'popularity': 0.42, 'reads': 55875, 'tags': ['politics', 'tech', 'health', 'history']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 93, 'likes': 881, 'popularity': 0.41, 'reads': 73964, 'tags': ['tech', 'history']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 89, 'likes': 251, 'popularity': 0.6, 'reads': 75503, 'tags': ['politics', 'startups', 'tech', 'history']}, {'author': 'Bryson Bowers', 'authorId': 6, 'id': 85, 'likes': 25, 'popularity': 0.18, 'reads': 16861, 'tags': ['tech']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 84, 'likes': 233, 'popularity': 0.65, 'reads': 17854, 'tags': ['politics', 'tech', 'history']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 82, 'likes': 140, 'popularity': 0.09, 'reads': 3201, 'tags': ['tech']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 77, 'likes': 407, 'popularity': 0.21, 'reads': 664, 'tags': ['politics', 'startups', 'tech', 'science']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 76, 'likes': 122, 'popularity': 0.01, 'reads': 75771, 'tags': ['tech', 'health', 'politics']}, {'author': 'Tia Roberson', 'authorId': 2, 'id': 59, 'likes': 971, 'popularity': 0.21, 'reads': 36154, 'tags': ['politics', 'tech']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 58, 'likes': 466, 'popularity': 0.1, 'reads': 17389, 'tags': ['science', 'tech']}, {'author': 'Bryson Bowers', 'authorId': 6, 'id': 54, 'likes': 723, 'popularity': 0.56, 'reads': 312, 'tags': ['culture', 'tech']}, {'author': 'Jaden Bryant', 'authorId': 3, 'id': 51, 'likes': 487, 'popularity': 0.01, 'reads': 98798, 'tags': ['design', 'startups', 'tech']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 46, 'likes': 89, 'popularity': 0.96, 'reads': 79298, 'tags': ['culture', 'tech']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 43, 'likes': 149, 'popularity': 0.07, 'reads': 77776, 'tags': ['science', 'tech']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 37, 'likes': 107, 'popularity': 0.55, 'reads': 35946, 'tags': ['tech', 'health', 'history']}, {'author': 'Kinley Crosby', 'authorId': 10, 'id': 35, 'likes': 868, 'popularity': 0.2, 'reads': 66926, 'tags': ['tech']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 26, 'likes': 748, 'popularity': 0.75, 'reads': 28239, 'tags': ['tech']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 25, 'likes': 365, 'popularity': 0.12, 'reads': 32949, 'tags': ['politics', 'tech']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 24, 'likes': 940, 'popularity': 0.74, 'reads': 89299, 'tags': ['culture', 'tech', 'politics']}, {'author': 'Jaden Bryant', 'authorId': 3, 'id': 18, 'likes': 983, 'popularity': 0.09, 'reads': 33952, 'tags': ['tech', 'history']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 15, 'likes': 560, 'popularity': 0.8, 'reads': 81549, 'tags': ['culture', 'startups', 'tech']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 14, 'likes': 311, 'popularity': 0.67, 'reads': 25644, 'tags': ['tech', 'history']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 13, 'likes': 230, 'popularity': 0.31, 'reads': 64058, 'tags': ['design', 'tech']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 12, 'likes': 590, 'popularity': 0.32, 'reads': 80351, 'tags': ['tech']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 4, 'likes': 728, 'popularity': 0.88, 'reads': 19645, 'tags': ['science', 'design', 'tech']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 2, 'likes': 469, 'popularity': 0.68, 'reads': 90406, 'tags': ['startups', 'tech', 'history']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 1, 'likes': 960, 'popularity': 0.13, 'reads': 50361, 'tags': ['tech', 'health']}]
        jsonResponse = json.dumps(mockResponse, indent=4)

        sr = Sendrequest()

        response, status_code = sr.hitLink("tech", "id", "desc")

        self.assertEqual(status_code, 200)
        self.assertEqual(response, jsonResponse)



    # Test two to check with multiple parameters
    def testRequesttwo(self):
        mockResponse = [{'author': 'Kinley Crosby', 'authorId': 10, 'id': 75, 'likes': 733, 'popularity': 0.98, 'reads': 94910, 'tags': ['science', 'design', 'culture']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 46, 'likes': 89, 'popularity': 0.96, 'reads': 79298, 'tags': ['culture', 'tech']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 74, 'likes': 660, 'popularity': 0.95, 'reads': 51324, 'tags': ['science']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 7, 'likes': 499, 'popularity': 0.93, 'reads': 95434, 'tags': ['science', 'health']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 19, 'likes': 779, 'popularity': 0.91, 'reads': 3041, 'tags': ['science']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 45, 'likes': 31, 'popularity': 0.89, 'reads': 63432, 'tags': ['science', 'history']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 4, 'likes': 728, 'popularity': 0.88, 'reads': 19645, 'tags': ['science', 'design', 'tech']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 17, 'likes': 527, 'popularity': 0.88, 'reads': 52454, 'tags': ['science', 'health']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 6, 'likes': 387, 'popularity': 0.83, 'reads': 50062, 'tags': ['science', 'startups']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 62, 'likes': 135, 'popularity': 0.83, 'reads': 87712, 'tags': ['culture', 'science']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 97, 'likes': 382, 'popularity': 0.83, 'reads': 47484, 'tags': ['politics', 'science', 'design', 'culture']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 21, 'likes': 406, 'popularity': 0.81, 'reads': 88797, 'tags': ['science', 'startups']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 15, 'likes': 560, 'popularity': 0.8, 'reads': 81549, 'tags': ['culture', 'startups', 'tech']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 28, 'likes': 713, 'popularity': 0.8, 'reads': 89173, 'tags': ['design']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 26, 'likes': 748, 'popularity': 0.75, 'reads': 28239, 'tags': ['tech']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 24, 'likes': 940, 'popularity': 0.74, 'reads': 89299, 'tags': ['culture', 'tech', 'politics']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 33, 'likes': 289, 'popularity': 0.73, 'reads': 31629, 'tags': ['science']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 41, 'likes': 715, 'popularity': 0.69, 'reads': 47876, 'tags': ['design', 'health']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 2, 'likes': 469, 'popularity': 0.68, 'reads': 90406, 'tags': ['startups', 'tech', 'history']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 14, 'likes': 311, 'popularity': 0.67, 'reads': 25644, 'tags': ['tech', 'history']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 87, 'likes': 619, 'popularity': 0.66, 'reads': 61622, 'tags': ['culture', 'startups', 'science']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 84, 'likes': 233, 'popularity': 0.65, 'reads': 17854, 'tags': ['politics', 'tech', 'history']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 63, 'likes': 682, 'popularity': 0.62, 'reads': 54374, 'tags': ['culture', 'design']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 89, 'likes': 251, 'popularity': 0.6, 'reads': 75503, 'tags': ['politics', 'startups', 'tech', 'history']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 10, 'likes': 853, 'popularity': 0.6, 'reads': 35913, 'tags': ['science', 'health', 'history']}, {'author': 'Bryson Bowers', 'authorId': 6, 'id': 54, 'likes': 723, 'popularity': 0.56, 'reads': 312, 'tags': ['culture', 'tech']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 69, 'likes': 425, 'popularity': 0.56, 'reads': 5149, 'tags': ['science', 'history']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 37, 'likes': 107, 'popularity': 0.55, 'reads': 35946, 'tags': ['tech', 'health', 'history']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 11, 'likes': 750, 'popularity': 0.54, 'reads': 6183, 'tags': ['science', 'design']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 40, 'likes': 968, 'popularity': 0.54, 'reads': 90784, 'tags': ['culture', 'science']}, {'author': 'Tia Roberson', 'authorId': 2, 'id': 98, 'likes': 934, 'popularity': 0.5, 'reads': 17307, 'tags': ['design']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 56, 'likes': 319, 'popularity': 0.49, 'reads': 96864, 'tags': ['design', 'health', 'culture']}, {'author': 'Tia Roberson', 'authorId': 2, 'id': 38, 'likes': 105, 'popularity': 0.45, 'reads': 45896, 'tags': ['design', 'history']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 96, 'likes': 395, 'popularity': 0.44, 'reads': 99575, 'tags': ['science', 'history']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 100, 'likes': 573, 'popularity': 0.43, 'reads': 89894, 'tags': ['science', 'design', 'history']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 95, 'likes': 985, 'popularity': 0.42, 'reads': 55875, 'tags': ['politics', 'tech', 'health', 'history']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 93, 'likes': 881, 'popularity': 0.41, 'reads': 73964, 'tags': ['tech', 'history']}, {'author': 'Kinley Crosby', 'authorId': 10, 'id': 88, 'likes': 371, 'popularity': 0.35, 'reads': 21916, 'tags': ['culture', 'science', 'history']}, {'author': 'Tia Roberson', 'authorId': 2, 'id': 99, 'likes': 473, 'popularity': 0.34, 'reads': 97868, 'tags': ['culture', 'startups', 'tech']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 12, 'likes': 590, 'popularity': 0.32, 'reads': 80351, 'tags': ['tech']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 13, 'likes': 230, 'popularity': 0.31, 'reads': 64058, 'tags': ['design', 'tech']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 16, 'likes': 749, 'popularity': 0.29, 'reads': 71754, 'tags': ['design', 'history']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 52, 'likes': 602, 'popularity': 0.26, 'reads': 76359, 'tags': ['science', 'health']}, {'author': 'Tia Roberson', 'authorId': 2, 'id': 59, 'likes': 971, 'popularity': 0.21, 'reads': 36154, 'tags': ['politics', 'tech']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 77, 'likes': 407, 'popularity': 0.21, 'reads': 664, 'tags': ['politics', 'startups', 'tech', 'science']}, {'author': 'Kinley Crosby', 'authorId': 10, 'id': 35, 'likes': 868, 'popularity': 0.2, 'reads': 66926, 'tags': ['tech']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 91, 'likes': 455, 'popularity': 0.19, 'reads': 90395, 'tags': ['science', 'health']}, {'author': 'Bryson Bowers', 'authorId': 6, 'id': 85, 'likes': 25, 'popularity': 0.18, 'reads': 16861, 'tags': ['tech']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 1, 'likes': 960, 'popularity': 0.13, 'reads': 50361, 'tags': ['tech', 'health']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 73, 'likes': 315, 'popularity': 0.13, 'reads': 8966, 'tags': ['design']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 25, 'likes': 365, 'popularity': 0.12, 'reads': 32949, 'tags': ['politics', 'tech']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 58, 'likes': 466, 'popularity': 0.1, 'reads': 17389, 'tags': ['science', 'tech']}, {'author': 'Jaden Bryant', 'authorId': 3, 'id': 18, 'likes': 983, 'popularity': 0.09, 'reads': 33952, 'tags': ['tech', 'history']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 82, 'likes': 140, 'popularity': 0.09, 'reads': 3201, 'tags': ['tech']}, {'author': 'Bryson Bowers', 'authorId': 6, 'id': 81, 'likes': 552, 'popularity': 0.09, 'reads': 22975, 'tags': ['design', 'history']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 36, 'likes': 709, 'popularity': 0.08, 'reads': 65277, 'tags': ['health', 'design']}, {'author': 'Bryson Bowers', 'authorId': 6, 'id': 42, 'likes': 452, 'popularity': 0.08, 'reads': 39721, 'tags': ['design']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 43, 'likes': 149, 'popularity': 0.07, 'reads': 77776, 'tags': ['science', 'tech']}, {'author': 'Jaden Bryant', 'authorId': 3, 'id': 51, 'likes': 487, 'popularity': 0.01, 'reads': 98798, 'tags': ['design', 'startups', 'tech']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 76, 'likes': 122, 'popularity': 0.01, 'reads': 75771, 'tags': ['tech', 'health', 'politics']}]
        jsonResponse = json.dumps(mockResponse, indent=4)

        sr = Sendrequest()

        response, status_code = sr.hitLink("tech,science,design", "popularity", "desc")

        self.assertEqual(status_code, 200)
        self.assertEqual(response, jsonResponse)



    # Test three to check with multiple parameters
    def testRequestthree(self):

        mockResponse = [{'author': 'Jon Abbott', 'authorId': 4, 'id': 95, 'likes': 985, 'popularity': 0.42, 'reads': 55875, 'tags': ['politics', 'tech', 'health', 'history']}, {'author': 'Jaden Bryant', 'authorId': 3, 'id': 18, 'likes': 983, 'popularity': 0.09, 'reads': 33952, 'tags': ['tech', 'history']}, {'author': 'Tia Roberson', 'authorId': 2, 'id': 59, 'likes': 971, 'popularity': 0.21, 'reads': 36154, 'tags': ['politics', 'tech']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 40, 'likes': 968, 'popularity': 0.54, 'reads': 90784, 'tags': ['culture', 'science']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 1, 'likes': 960, 'popularity': 0.13, 'reads': 50361, 'tags': ['tech', 'health']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 24, 'likes': 940, 'popularity': 0.74, 'reads': 89299, 'tags': ['culture', 'tech', 'politics']}, {'author': 'Tia Roberson', 'authorId': 2, 'id': 98, 'likes': 934, 'popularity': 0.5, 'reads': 17307, 'tags': ['design']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 93, 'likes': 881, 'popularity': 0.41, 'reads': 73964, 'tags': ['tech', 'history']}, {'author': 'Kinley Crosby', 'authorId': 10, 'id': 35, 'likes': 868, 'popularity': 0.2, 'reads': 66926, 'tags': ['tech']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 10, 'likes': 853, 'popularity': 0.6, 'reads': 35913, 'tags': ['science', 'health', 'history']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 19, 'likes': 779, 'popularity': 0.91, 'reads': 3041, 'tags': ['science']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 11, 'likes': 750, 'popularity': 0.54, 'reads': 6183, 'tags': ['science', 'design']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 16, 'likes': 749, 'popularity': 0.29, 'reads': 71754, 'tags': ['design', 'history']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 26, 'likes': 748, 'popularity': 0.75, 'reads': 28239, 'tags': ['tech']}, {'author': 'Kinley Crosby', 'authorId': 10, 'id': 75, 'likes': 733, 'popularity': 0.98, 'reads': 94910, 'tags': ['science', 'design', 'culture']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 4, 'likes': 728, 'popularity': 0.88, 'reads': 19645, 'tags': ['science', 'design', 'tech']}, {'author': 'Bryson Bowers', 'authorId': 6, 'id': 54, 'likes': 723, 'popularity': 0.56, 'reads': 312, 'tags': ['culture', 'tech']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 41, 'likes': 715, 'popularity': 0.69, 'reads': 47876, 'tags': ['design', 'health']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 28, 'likes': 713, 'popularity': 0.8, 'reads': 89173, 'tags': ['design']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 36, 'likes': 709, 'popularity': 0.08, 'reads': 65277, 'tags': ['health', 'design']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 63, 'likes': 682, 'popularity': 0.62, 'reads': 54374, 'tags': ['culture', 'design']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 74, 'likes': 660, 'popularity': 0.95, 'reads': 51324, 'tags': ['science']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 87, 'likes': 619, 'popularity': 0.66, 'reads': 61622, 'tags': ['culture', 'startups', 'science']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 52, 'likes': 602, 'popularity': 0.26, 'reads': 76359, 'tags': ['science', 'health']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 12, 'likes': 590, 'popularity': 0.32, 'reads': 80351, 'tags': ['tech']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 100, 'likes': 573, 'popularity': 0.43, 'reads': 89894, 'tags': ['science', 'design', 'history']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 15, 'likes': 560, 'popularity': 0.8, 'reads': 81549, 'tags': ['culture', 'startups', 'tech']}, {'author': 'Bryson Bowers', 'authorId': 6, 'id': 81, 'likes': 552, 'popularity': 0.09, 'reads': 22975, 'tags': ['design', 'history']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 17, 'likes': 527, 'popularity': 0.88, 'reads': 52454, 'tags': ['science', 'health']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 7, 'likes': 499, 'popularity': 0.93, 'reads': 95434, 'tags': ['science', 'health']}, {'author': 'Jaden Bryant', 'authorId': 3, 'id': 51, 'likes': 487, 'popularity': 0.01, 'reads': 98798, 'tags': ['design', 'startups', 'tech']}, {'author': 'Tia Roberson', 'authorId': 2, 'id': 99, 'likes': 473, 'popularity': 0.34, 'reads': 97868, 'tags': ['culture', 'startups', 'tech']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 2, 'likes': 469, 'popularity': 0.68, 'reads': 90406, 'tags': ['startups', 'tech', 'history']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 58, 'likes': 466, 'popularity': 0.1, 'reads': 17389, 'tags': ['science', 'tech']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 91, 'likes': 455, 'popularity': 0.19, 'reads': 90395, 'tags': ['science', 'health']}, {'author': 'Bryson Bowers', 'authorId': 6, 'id': 42, 'likes': 452, 'popularity': 0.08, 'reads': 39721, 'tags': ['design']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 69, 'likes': 425, 'popularity': 0.56, 'reads': 5149, 'tags': ['science', 'history']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 77, 'likes': 407, 'popularity': 0.21, 'reads': 664, 'tags': ['politics', 'startups', 'tech', 'science']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 21, 'likes': 406, 'popularity': 0.81, 'reads': 88797, 'tags': ['science', 'startups']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 96, 'likes': 395, 'popularity': 0.44, 'reads': 99575, 'tags': ['science', 'history']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 6, 'likes': 387, 'popularity': 0.83, 'reads': 50062, 'tags': ['science', 'startups']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 97, 'likes': 382, 'popularity': 0.83, 'reads': 47484, 'tags': ['politics', 'science', 'design', 'culture']}, {'author': 'Kinley Crosby', 'authorId': 10, 'id': 88, 'likes': 371, 'popularity': 0.35, 'reads': 21916, 'tags': ['culture', 'science', 'history']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 25, 'likes': 365, 'popularity': 0.12, 'reads': 32949, 'tags': ['politics', 'tech']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 56, 'likes': 319, 'popularity': 0.49, 'reads': 96864, 'tags': ['design', 'health', 'culture']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 73, 'likes': 315, 'popularity': 0.13, 'reads': 8966, 'tags': ['design']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 14, 'likes': 311, 'popularity': 0.67, 'reads': 25644, 'tags': ['tech', 'history']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 33, 'likes': 289, 'popularity': 0.73, 'reads': 31629, 'tags': ['science']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 89, 'likes': 251, 'popularity': 0.6, 'reads': 75503, 'tags': ['politics', 'startups', 'tech', 'history']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 84, 'likes': 233, 'popularity': 0.65, 'reads': 17854, 'tags': ['politics', 'tech', 'history']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 13, 'likes': 230, 'popularity': 0.31, 'reads': 64058, 'tags': ['design', 'tech']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 43, 'likes': 149, 'popularity': 0.07, 'reads': 77776, 'tags': ['science', 'tech']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 82, 'likes': 140, 'popularity': 0.09, 'reads': 3201, 'tags': ['tech']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 62, 'likes': 135, 'popularity': 0.83, 'reads': 87712, 'tags': ['culture', 'science']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 76, 'likes': 122, 'popularity': 0.01, 'reads': 75771, 'tags': ['tech', 'health', 'politics']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 37, 'likes': 107, 'popularity': 0.55, 'reads': 35946, 'tags': ['tech', 'health', 'history']}, {'author': 'Tia Roberson', 'authorId': 2, 'id': 38, 'likes': 105, 'popularity': 0.45, 'reads': 45896, 'tags': ['design', 'history']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 46, 'likes': 89, 'popularity': 0.96, 'reads': 79298, 'tags': ['culture', 'tech']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 45, 'likes': 31, 'popularity': 0.89, 'reads': 63432, 'tags': ['science', 'history']}, {'author': 'Bryson Bowers', 'authorId': 6, 'id': 85, 'likes': 25, 'popularity': 0.18, 'reads': 16861, 'tags': ['tech']}]
        jsonResponse = json.dumps(mockResponse, indent=4)

        sr = Sendrequest()

        response, status_code = sr.hitLink("science,design,tech", "likes", "desc")

        self.assertEqual(status_code, 200)
        self.assertEqual(response, jsonResponse)


if __name__ == "__main__":
    unittest.main()