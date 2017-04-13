from unittest import TestCase
from dead_links import should_follow_link

class ShouldFollowTest(TestCase):
    def test_cases(self):
        inputs = [
            ('/display/~J.Doe', True),
            ('/download/attachments/4653456/2017-event-day-page-flyer.pub?version=1&modificationDate=174500292323&api=v2', False),
            ('#', False), 
            ('http://134.7.57.175:8090/display/~D.White', True),
            ('http://123.4.56.789:8090', False),
            ('http://122.2.57.215:8090/display/~J.Doe', False),
            ('/display/yourpage/2017+Random+Fundraiser+Day+Review', True),
            ('http://www.atlassian.com/c/conf/17470', False),
            ('http://www.google.com', False)
        ]

        for (src, should_be) in inputs:
            got = should_follow_link(src)
            self.assertEqual(got, should_be, f'Expected {should_be}, got {got} for "{src}"')

