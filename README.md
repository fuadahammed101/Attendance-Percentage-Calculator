# 🎓 Attendance Percentage Calculator

This is a simple Python script that calculates student attendance percentages from raw attendance records and assigns marks based on predefined rules.

## 📋 Features

* Reads attendance data from an embedded CSV string.
* Calculates attendance percentage per student.
* Assigns marks based on attendance percentage:

  * `5 marks` → 70% and above
  * `4 marks` → 60% to less than 70%
  * `3 marks` → 45% to less than 60%
  * `2 marks` → Less than 45%
* Prints a formatted attendance report.
* Shows a summary of how many students fall into each attendance category.

## 📦 Requirements

This script uses the following Python libraries:

* `pandas`
* `io.StringIO`
* (Optional) `tabulate` (for better markdown-style table display in terminal)

Install dependencies (if not already installed):

```bash
pip install pandas tabulate
```

> Note: The script will fallback to basic printing if `tabulate` is not installed.

## ▶️ How to Use

### Run the script

```bash
python attendance_calculator.py
```

You will be prompted to enter the number of students to calculate attendance for:

* Enter a **number** to limit the results (e.g., `5` to process the first 5 students).
* Press **Enter** without typing anything to calculate for **all students**.

### Example Output

```
Please enter the Number of Students (or press Enter for all): 5

Calculated Attendance Percentage:

| Name                   | ID         | Percentage   | Marks   |
|------------------------|------------|--------------|---------|
| Md. Kamruzzaman        | 211002062  | 31.58        | 2       |
| Shuvo Ray              | 212002042  | 52.0         | 3       |
| Shamsul Islam Rana     | 212902037  | 38.1         | 2       |
| Lima Islam             | 213002171  | 61.11        | 4       |
| Nurjahan Khanom Oishi  | 213002184  | 53.33        | 3       |

Attendance Percentage (Student Count):

| No.   | Percentage   | StudentCount   |
|-------|--------------|----------------|
| 1     | 70%          | 0              |
| 2     | 60%          | 1              |
| 3     | 45%          | 2              |
| 4     | 31-44%       | 1              |
| 5     | 30%          | 1              |
```



## 🛠️ Customization

You can update or replace the embedded `data` string with your own CSV-format attendance data. Ensure it follows this format:

```
SL,StudentID,StudentName,attandence
1,211002062,John Doe,AAPAPAAPPPAAAAAAAAA
...
```

* `"P"` for Present
* `"A"` for Absent

