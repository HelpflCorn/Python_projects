# from django.test import TestCase
from polls.models import Question
from unittest import TestCase

class QuestionTest(TestCase):
    def setUp(self):
        Question.objects.create(question_text="Test Question", pub_date="2023-09-16 07:36:29")

    def test_ORM(self):
        TestObject = Question.objects.filter(pub_date="2023-09-16 07:36:29").first()
        test_1 = TestObject.question_text
        self.assertEqual(test_1, "Test Question")


# if __name__ == "__main__":
#     unittest.main()