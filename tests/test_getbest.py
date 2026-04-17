import unittest
import io
import sys
import os

# Creating a temporary CSV file for getbest.py
#Because getbest.py tries to open a real file
#using sys.argv[1], it provides an actual file
dummy_file = "dummy.csv"

with open(dummy_file, "w") as f:
    f.write(
        "Course,Student Number,Mark,Comment\n"
        "ELEN3020,160001,72,OK\n"
        "ELEN3020,167381,90,Check\n"
        "ELEN3020,143211,83,-\n"
        "ELEN3020,17171,48,Redo\n"
        "ELEN3020,191919,73,-\n"
    )

# getbest.py uses sys.argv[1] to read filename
#so we simulate running: python getbest.py dummy.csv
sys.argv = ["getbest.py", dummy_file]

#Then importing functions after sys.argv is set correctly
from getbest import getCols, findTop


class TestGetBest(unittest.TestCase):

    def setUp(self):
        
        # creating in-memory fake CSV data for unit testing
    
        self.data = io.StringIO(
            "Course,Student Number,Mark,Comment\n"
            "ELEN3020,160001,72,OK\n"
            "ELEN3020,167381,90,Check\n"
            "ELEN3020,143211,83,-\n"
            "ELEN3020,17171,48,Redo\n"
            "ELEN3020,191919,73,-\n"
        )

    def test_getColumns(self):

        # Test if correct column indexes are detected
        num_cols, mark_cols = getCols(self.data)
        self.assertEqual(num_cols, 1) # Student Number column
        self.assertEqual(mark_cols, 2) # Mark column

    
    def test_find_the_top(self):
        #Reset file pointer to start of StringIO object
        #because getCols() already moved it forward
        self.data.seek(0)
        getCols(self.data)

        # Test function that finds highest student mark
        best_idx, best = findTop(self.data, 1, 2)

        self.assertEqual(best_idx, "167381") #top student
        self.assertEqual(best, 90) # highest mark


if __name__ == "__main__":
    unittest.main()

os.remove(dummy_file) # This clean up temporary files after tests finish