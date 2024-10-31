import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        rect1 = hw2.create_rectangle(data.Point(2, 2), data.Point(10, 10))
        assert rect1.top_left.x == 2 and rect1.top_left.y == 10
        assert rect1.bottom_right.x == 10 and rect1.bottom_right.y == 2

    def test_create_rectangle2(self):
        rect2 = hw2.create_rectangle(data.Point(10, 10), data.Point(2, 2))
        assert rect2.top_left.x == 2 and rect2.top_left.y == 10
        assert rect2.bottom_right.x == 10 and rect2.bottom_right.y == 2

    # Part 2
    def test_shorter_duration_than(self):
        d1 = data.Duration(1,23)
        d2 = data.Duration(12,0)
        assert hw2.shorter_duration_than(d1, d2) == True

    def test_shorter_duration_than2(self):
        d3 = data.Duration(6,43)
        d4 = data.Duration(3,21)
        assert hw2.shorter_duration_than(d3, d4) == False

    # Part 3
    def test_song_shorter_than(self):
        song1 = data.Song("Song A","Camille Abetong", data.Duration(3, 30))  # 3 minutes 30 seconds
        song2 = data.Song("Song B", "Diego Rodriguez", data.Duration(4, 0))  # 4 minutes
        song3 = data.Song("Song C", "Camille Abetong", data.Duration(2, 45))  # 2 minutes 45 seconds
        song4 = data.Song("Song D", "Diego Rodriguez", data.Duration(5, 15))  # 5 minutes 15 seconds

        songs = [song1, song2, song3, song4]

        max_duration = data.Duration(3, 45)
        result = hw2.song_shorter_than(songs, max_duration)
        expected = [
            data.Song("Song A", "Camille Abetong", data.Duration(3, 30)),
            data.Song("Song C", "Camille Abetong", data.Duration(2, 45)),
        ]
        self.assertEqual(result, expected)

    def test_song_shorter_than2(self):
        song1 = data.Song("Song A","Camille Abetong", data.Duration(3, 30))  # 3 minutes 30 seconds
        song2 = data.Song("Song B", "Diego Rodriguez", data.Duration(4, 0))  # 4 minutes
        song3 = data.Song("Song C", "Camille Abetong", data.Duration(2, 45))  # 2 minutes 45 seconds
        song4 = data.Song("Song D", "Diego Rodriguez", data.Duration(5, 15))  # 5 minutes 15 seconds

        songs = [song1, song2, song3, song4]

        max_duration = data.Duration(10, 0)
        result = hw2.song_shorter_than(songs, max_duration)
        expected = [
            data.Song("Song A", "Camille Abetong", data.Duration(3, 30)),
            data.Song("Song B", "Diego Rodriguez", data.Duration(4, 0)),
            data.Song("Song C", "Camille Abetong", data.Duration(2, 45)),
            data.Song("Song D", "Diego Rodriguez", data.Duration(5, 15))
        ]
        self.assertEqual(result, expected)

    # Part 4
    def test_running_time(self):
        songs = [
            data.Song("June Hymn", "The Decemberists", data.Duration(4, 30)),
            data.Song("October", "Broken Bells", data.Duration(3, 40)),
            data.Song("Dust in the Wind", "Kansas", data.Duration(3, 29)),
            data.Song("Airplanes", "Local Natives", data.Duration(3, 58)),
            ]

        playlist = [0, 2, 1, 3, 0]  # June Hymn, Dust in the Wind, October, Airplanes, June Hymn
        result = hw2.running_time(songs, playlist)
        expected = data.Duration(20, 7)  # 20:07
        self.assertEqual(result, expected)

    def test_running_time2(self):
        songs = [
            data.Song("June Hymn", "The Decemberists", data.Duration(4, 30)),
            data.Song("October", "Broken Bells", data.Duration(3, 40)),
            data.Song("Dust in the Wind", "Kansas", data.Duration(3, 29)),
            data.Song("Airplanes", "Local Natives", data.Duration(3, 58)),
        ]
        playlist = [0, -1, 4, 1]  # Only valid indices are 0 and 1
        result = hw2.running_time(songs, playlist)
        expected = data.Duration(8, 10)  # 4:30 + 3:40
        self.assertEqual(result, expected)

    # Part 5
    def test_valid_route(self):
        city_links = [
            ["san luis obispo", "santa margarita"],
            ["santa margarita", "atascadero"],
            ["atascadero", "san luis obispo"],
            ["los angeles", "san diego"],
            ["san diego", "long beach"]
        ]

        route = ["san luis obispo", "santa margarita", "atascadero"]
        result = hw2.validate_route(city_links, route)
        self.assertTrue(result)


    def test_invalid_route(self):
        city_links = [
            ["san luis obispo", "santa margarita"],
            ["santa margarita", "atascadero"],
            ["atascadero", "san luis obispo"],
            ["los angeles", "san diego"],
            ["san diego", "long beach"]
        ]

        route = ["san luis obispo", "atascadero"]
        result = hw2.validate_route(city_links, route)
        self.assertTrue(result)

    # Part 6
    def test_longest_repetition(self):
        self.assertEqual(hw2.longest_repetition([1, 1, 2, 2, 1, 1, 1, 3]), 4)
        self.assertEqual(hw2.longest_repetition([1, 2, 2, 3, 3, 3]), 3)

    def test_no_repetition(self):
        self.assertEqual(hw2.longest_repetition([1, 2, 3, 4]), None)
        self.assertEqual(hw2.longest_repetition([]), None)




if __name__ == '__main__':
    unittest.main()
