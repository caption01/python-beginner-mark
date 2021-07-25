class Student:
    """Represent a student"""

    def __init__(self, name):
        """Initial data."""
        self._name = name
        self._results = {}

    def _calc_predicted_result(self):
        """Calcalate the student predict result"""
        result = self._results.values()
        return sum(result) / len(result)

    def add_result(self, year, result):
        """Add result to the student"""
        self._results[year] = result

    def display_predicted_result(self):
        """Display predicted result."""
        result = self._calc_predicted_result()
        print(f'Student {self._name} is predicted: {result}')


s = Student('One')
s.add_result(2020, 88)
s.add_result(2019, 76)
s.add_result(2018, 22)
s.display_predicted_result()