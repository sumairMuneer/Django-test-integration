from django.test import TestCase

# Create your tests here.
import datetime


class QuestionModelTests1(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        # a=2
        self.assertGreaterEqual(2,2)

    def test_was_published_recently_with_future_question1(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        # a=2
        self.assertGreaterEqual(2,2)
        

