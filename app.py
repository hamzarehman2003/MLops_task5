from flask import Flask, request

app = Flask(__name__)

def calculate_gpa(grades, credits):
    total_points = sum([grade * credit for grade, credit in zip(grades, credits)])
    total_credits = sum(credits)
    gpa = total_points / total_credits if total_credits > 0 else 0
    return round(gpa, 2)

@app.route('/')
def home():
    # Example grades and credits (replace with your data source or request input)
    grades = [4.0, 3.7, 3.0, 3.3]  # Example grades (A=4.0, B+=3.7, etc.)
    credits = [3, 3, 4, 2]          # Corresponding credits for each course

    gpa = calculate_gpa(grades, credits)
    return f"Your GPA is: {gpa}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
