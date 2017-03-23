# -*- coding: utf-8 -*-

from rss import Scrapper
import unittest
import mock


class CoreTestSuite(unittest.TestCase):

    @mock.patch.object(Scrapper.parse_xml, 'url', autospec=True)
    def test_scrapper_check_url(self, mock_put_object):

        test = Scrapper('https://www.theguardian.com/international/rss')
        test.parse_xml('https://www.theguardian.com/international/rss')
        mock_put_object.assert_called_with(url = "https://www.theguardian.com/international/rss")

if __name__ == '__main__':
    unittest.main()


