import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1: data.Point, point2: data.Point) -> data.Rectangle:
    """
    Purpose:
    Creates a Rectangle object from two Point objects by determining
    the top-left and bottom-right corners based on their x and y coordinates.

    Input: Points
    Output: Rectangle

    Parameters:
    point1 (Point): The first point.
    point2 (Point): The second point.

    Returns:
    Rectangle: A rectangle defined by the top-left and bottom-right points.
    """
    # Determine top-left and bottom-right points
    top_left_x = min(point1.x, point2.x)
    top_left_y = max(point1.y, point2.y)
    bottom_right_x = max(point1.x, point2.x)
    bottom_right_y = min(point1.y, point2.y)

    top_left = data.Point(top_left_x, top_left_y)
    bottom_right = data.Point(bottom_right_x, bottom_right_y)

    return data.Rectangle(top_left, bottom_right)

# Part 2
def shorter_duration_than(duration1: data.Duration, duration2: data.Duration) -> bool:
    """
    Purpose:
    Compares two Duration objects to determine if the first duration
    is shorter than the second.

    Input: Duration
    Output: Boolean (True or False)

    Parameters:
    duration1 (Duration): The first duration to compare.
    duration2 (Duration): The second duration to compare.

    Returns:
    bool: True if duration1 is shorter than duration2, False otherwise.
    """

    if duration1.total_seconds() < duration2.total_seconds():
        return True
    else:
        return False

# Part 3
def song_shorter_than(self:list[data.Song], max_duration: data.Duration) -> list[data.Song]:
    """
    Purpose:
    Filters a list of Song objects to return only those with a duration
    shorter than the specified maximum duration.

    Input: List & Duration
    Output: List

    Parameters:
    songs (list[Song]): A list of Song objects to filter.
    max_duration (Duration): The upper bound on the song's length.

    Returns:
    list[Song]: A list of songs with durations shorter than max_duration.
    """
    return [song for song in self if song.duration.total_seconds() < max_duration.total_seconds()]

# Part 4
def running_time(songs: list[data.Song], playlist: list[int]) -> data.Duration:
    """
    Purpose:
    Calculate the total running time of a playlist of songs.

    Input: list & list
    Output: Duration

    Parameters:
    - songs: A list of Song objects.
    - playlist: A list of integers representing song indices.

    Returns:
    A Duration object representing the total running time.
    """
    total_minutes = 0
    total_seconds = 0

    for index in playlist:
        if 0 <= index < len(songs):
            total_minutes += songs[index].duration.minutes
            total_seconds += songs[index].duration.seconds

    # Convert total seconds to minutes and seconds
    total_minutes += total_seconds // 60
    total_seconds %= 60

    return data.Duration(total_minutes, total_seconds)

# Part 5
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    """
    Purpose:
    Validate if a given route is valid based on city links.

    Input: Lists
    Output: Boolean (True or False)

    Parameters:
    - city_links: A list of lists where each inner list contains city names that are directly connected.
    - route: A list of city names representing the route from the first city to the last, including intermediate cities.

    Returns:
    True if the route is valid (i.e., there are links between consecutive cities), False otherwise.
    """
    connections = {}
    for link in city_links:
        for city in link:
            if city not in connections:
                connections[city] = set()
            connections[city].update(link)
            connections[city].remove(city)

    for i in range(len(route) - 1):
        if route[i + 1] not in connections.get(route[i], []):
            return False

    return True

# Part 6
def longest_repetition(nums: list[int]):
    """
    Purpose:
    Find the index of the longest contiguous repetition of a single number in a list.

    Input: list
    Output: Integer

    Parameters:
    - nums: A list of integers.

    Returns:
    The index of the first occurrence of the longest contiguous repetition, or None if the list is empty.
    """

    max_length = 1
    max_index = 0
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_index = i - current_length
            current_length = 1

    if current_length > max_length:
        max_index = len(nums) - current_length

    return max_index if max_length > 1 else None