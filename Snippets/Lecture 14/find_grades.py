def find_grades(grades, students):
    """
    * grades is a dict mapping student names (str) to grades (str)
    * students is a list of student names
    Returns a list containing the grades for students (in same order)
    """
    return [grades[name] for name in students]
# example
d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']
