import pandas as pd
from io import StringIO

# Embedded attendance data as fallback with updated header
data = """
SL,StudentID,StudentName,attandence
1,211002062,Md. Kamruzzaman,AAPAPAAPPPAAAAAAAAA
2,212002042,Shuvo Ray,PPAAAPPAAPPPAPAPAAPPPA
3,212902037,Shamsul Islam Rana,AAAAAPPAAAAPPPAAAAPP
4,213002171,Lima Islam,PAAAPPPPPPPPPAAPPP
6,213002184,Nurjahan Khanom Oishi,PPPPAPPPPAAAPPA
7,221002011,Abdullah Al Mamun,PPPAPPPPPAAPAPPAAAAA
9,221002016,Chinmoy Chakma,AAAPAPPAPAAPPPP
10,221002042,Asadullah,PAAAPPPPPAPAP
11,221002044,Abdullha Hill Oneir,AAPAPPPPPPPAPPPAAPAP
12,221002048,Md. Mehedi Hasan,AAAAAAPAPPPPPP
13,221002057,Md. Torikul Islam,AAPAAPPPPPPPPPPPPPP
14,221002078,Fuad Ahammed,AAAAAPPPPPPAAPPAPAAP
15,221002234,Israt Jahan Shela,AAPPAPPPPPPPPAPPA
21,221002251,Md. Sajeeb Mia,PPPPPPPPPPPPPPPPP
27,221002570,Afnan Khan Sopnil,AAPAAPPPPPPPPAAAPPPP
28,221002578,Monowar Hossen Sourav,PAPPPPPAAPPAPPAPPPPA
31,221002612,Gazi Shaplur Rahman,APPPPPPPPAAPPPPAAPAP
37,221902236,Md. Nazir Ahmed,PPPPP
38,221902243,Kakoli Akter,PPPPPPPP
39,221902262,Maymuna Akter,AAAAAAAA
40,221902307,Md. Kamrul Hasan,PPPPPPPPPPPPPPPP
"""

def load_data():
    """
    Load attendance data from embedded data only.
    Returns a pandas DataFrame.
    """
    df = pd.read_csv(StringIO(data))
    return df

def calculate_attendance(df):
    """
    Calculate attendance percentage and assign marks for each student.
    Returns a DataFrame with Name, ID, Percentage, and Marks columns.
    """
    df = df.dropna(subset=["StudentID", "StudentName"])

    names = []
    ids = []
    percentages = []
    marks = []

    for index, row in df.iterrows():
        student_name = row["StudentName"]
        student_id = row["StudentID"]
        attendance_cols = row.index[3:]
        if len(attendance_cols) == 1:
            attendance_record = str(row[attendance_cols[0]])
        else:
            attendance_record = ''.join(str(row[col]) for col in attendance_cols if pd.notna(row[col]))

        total_days = len(attendance_record)
        present_days = attendance_record.count("P")

        # Handle division by zero if no attendance data
        percentage = (present_days / total_days) * 100 if total_days > 0 else 0

        # Assign marks based on attendance percentage
        if percentage >= 70:
            mark = 5
        elif percentage >= 60:
            mark = 4
        elif percentage >= 45:
            mark = 3
        elif percentage <= 30:
            mark = 2
        else:
            mark = 2  # Default mark if none of the above

        names.append(student_name)
        ids.append(student_id)
        percentages.append(round(percentage, 2))
        marks.append(mark)

    results_df = pd.DataFrame({
        "Name": names,
        "ID": ids,
        "Percentage": percentages,
        "Marks": marks
    })

    return results_df

def print_report(results_df, full_results_df):
    """
    Print the attendance report for filtered students and summary counts for all students.
    """
    print("Calculated Attendance Percentage:\n")
    try:
        print(results_df.to_markdown(index=False, numalign="left", stralign="left"))
    except ImportError:
        # Fallback if tabulate is not installed
        print(results_df)

    # Count how many students fall into each percentage category in the filtered dataset
    # 70% and above
    count_70 = (results_df['Percentage'] >= 70).sum()
    # 60% to less than 70%
    count_60 = ((results_df['Percentage'] >= 60) & (results_df['Percentage'] < 70)).sum()
    # 45% to less than 60%
    count_45 = ((results_df['Percentage'] >= 45) & (results_df['Percentage'] < 60)).sum()
    # 31% to less than 45%
    count_31_44 = ((results_df['Percentage'] >= 31) & (results_df['Percentage'] < 45)).sum()
    # 30% and below
    count_30 = (results_df['Percentage'] <= 30).sum()

    print("\n\nAttendance Percentage (Student Count):\n")
    # Print summary counts as a table
    categories = [
        ("70%", count_70),
        ("60%", count_60),
        ("45%", count_45),
        ("31-44%", count_31_44),
        ("30%", count_30)
    ]
    summary_df = pd.DataFrame({
        "No.": range(1, len(categories) + 1),
        "Percentage": [cat[0] for cat in categories],
        "StudentCount": [cat[1] for cat in categories]
    })
    try:
        print(summary_df.to_markdown(index=False, numalign="left", stralign="left"))
    except ImportError:
        print(summary_df)


def main():
    print("Attendance Percentage Calculator\n")
    while True:
        try:
            num_students = input("Please enter the Number of Students (or press Enter for all): ")
            if num_students == "":
                num_students = None
                break
            num_students = int(num_students)
            if num_students <= 0:
                print("Please enter a positive integer or press Enter for all students.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer or press Enter for all students.")

    full_df = load_data()
    full_results_df = calculate_attendance(full_df)

    if num_students is not None:
        filtered_df = full_df.head(num_students)
        results_df = calculate_attendance(filtered_df)
    else:
        results_df = full_results_df

    print_report(results_df, full_results_df)

if __name__ == "__main__":
    main()
