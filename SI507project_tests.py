from SI507project_tools import *
import unittest


class PartOne(unittest.TestCase):
    def test_data(self):
        file = open('data.csv','r')
        self.contents = file.readlines()
        file.close()
        self.assertTrue("1-on-1 interview,1.Specify the goal of the interview and select questions and subjects around the topic carefully.\n2. Define if there is a need for a structured interview or semi-structured interview. Structured interviews have a clear guide that needs to be followed, semi-structured interviews allow for flexibility within the interview.\n3. Conduct a pre-interview during the recruitment phase, to refine the guide.\n4. Talk, watch, listen and observe as you conduct the interview.\n5. Document the interview by recording audio/video (if possible) and take notes.\n6. Analyze and compare the information gathered from the interview(s).,https://toolkits.dss.cloud/design/wp-content/uploads/sites/2/2016/06/DMT_icons-04-wpcf_120x120.png,4 HOURS - 1 DAY,research,When there is a need for information from users and/or experts.,Facilitates quick and early discovery; best for personal information; works well in combination with other methods.,For structured interviews, the interviewer should be consistent across interviews.,Notes and recordings of the interviews.,Analyse recordings to uncover insights and identify possible ways to incorporate them into a solution." in self.contents, "Testing that 1-on-1 interview method exists in the file")

class PartTwo(unittest.TestCase):
    def test_data_amount(self):
        file = open('data.csv','r')
        self.contents = file.readlines()
        row_count = sum(1 for row in fileObject)
        file.close()
        self.assertTrue(row_count >= 60, "Testing that there are 80 lines in data csv file")

class PartThree(unittest.TestCase): #the form won’t allow you to save if you give it an empty item text.
    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'],["You can't have an empty list item"])

class PartFour(unittest.TestCase):
    def Random_Method(self):
        self.assertTrue(len(list(randome_method)) = 1, "Testing that if the randome method generating function only returns one instance out)")




if __name__ == '__main__':
    unittest.main()
