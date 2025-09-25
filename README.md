# Description
___
This is a cli Report creator based on Registry and Factory patterns.


## Installation using pip
___
1. Clone the repository
2. Enter the folder, activate virtual env
3. run `pip install -r requirement.txt`


## Creating report
___
### Usage
```commandline
python -m cli --files file.csv --report reportKey
```
### args
- `--files` List the paths to the files for which a report needs to be created.
- `--report` Report key, that was specified for the subclass of Reporter. This parameter allows you to select which report to generate.

### Example
```commandline
python -m cli --files file1.csv file2.csv fileN.csv --report reportKey
```
output example
```text
+-----+----------------+---------+
|   # | student_name   |   grade |
+=====+================+=========+
|   1 | Maria          |     4.8 |
+-----+----------------+---------+
|   2 | Ivan           |     4.0 |
+-----+----------------+---------+
|   3 | Alice          |     3.5 |
+-----+----------------+---------+
|   4 | Bob            |     3.3 |
+-----+----------------+---------+
```

## An easy way to add a new report
___

To create a new report type, you must create a subclass of base class **Report**, add report_key to subclass attr, implement build_report method and import your class to src/reporter/\_\_init\_\_.py.

### Example

```python
# /reporter/new_report.py
from typing import Sequence, Any

from src.models.student import StudentDTO
from .base import Reporter


class ExampleReport(Reporter):

    report_key = "example-report"

    def build_report(self, students_data: Sequence[StudentDTO]) -> list[dict[str, Any]]:

        # building your report there...
        
        simple_report_example = [
            {
                "Date": s.date,
                "Student": s.student_name,
                "Subject": s.subject,
                "Teacher": s.teacher_name,
                "Grade": s.grade,
            } for s in students_data
        ]
        return simple_report_example
```

And then import this class to  src/reporter/\_\_init\_\_.py
```python
# src/reporter/__init__.py
from .base import Reporter
from .example_report import ExampleReport
```

Now you can create this report like this:
```commandline
python -m cli --files file1.csv file2.csv fileN.csv --report example-report
```
