"""
Score Tracker - a small program that lets a user enter student names and quiz
scores.
"""

student_scores = []


def input_student_name():
    """Prompt the user for a student name."""
    name = input("\nEnter student name (or 'done'): ").strip()

    return name


def input_student_quiz_score():
    """Prompt the student for a quiz score."""
    while True:
        try:
            quiz_score = float(input("Enter quiz score: ").strip())
            if quiz_score < 0:
                raise ValueError("\nThe quiz grade must be a positive number!\n")
            if quiz_score == -0:
                raise ValueError("\nThe quiz grade must be a positive number!\n")
        except ValueError:
            print("\nThe quiz grade must be a whole or mixed number!\n")
        else:
            return quiz_score


def display_student_quiz_scores():
    """Print the student quiz scores."""
    print("--- Score Summary ---")



def run_score_tracker():
    while True:
        name = input_student_name()
        if name.lower() == "done":
            break
        score = input_student_quiz_score()
        student_scores.append({"name": name, "score": score})

    display_student_quiz_scores()



run_score_tracker()



