"""Run Leo: Multi-Agent AI Tutor locally (Python 3.10+)."""
import asyncio
from src.config import configure_llm
from src.memory import load_memory, save_memory
from src.workflow import run_learning_phase, evaluate_answers, score_from_feedback, re_teach_weak_area


def main():
    llm, model_name = configure_llm()
    print(f"CrewAI Gemini model configured: {model_name}")

    saved = load_memory()
    student_name = input(f"Student name [{saved.get('student_name', 'Student')}]: ").strip()
    student_name = student_name or saved.get("student_name", "Student")
    level = input("Level (beginner/intermediate/advanced) [beginner]: ").strip() or "beginner"
    topic = input(f"Topic [{saved.get('last_topic', 'Python Basics')}]: ").strip()
    topic = topic or saved.get("last_topic", "Python Basics")
    previous_context = f"Previously studied: {saved.get('last_topic')}" if saved.get("last_topic") else ""

    print("\nStarting Coordinator -> Explainer -> Quiz Master...")
    plan, lesson, quiz = asyncio.run(run_learning_phase(
        llm, student_name, level, topic, previous_context
    ))
    print("\n" + "=" * 68 + "\nCOORDINATOR: LEARNING PLAN\n" + "=" * 68)
    print(plan)
    print("\n" + "=" * 68 + "\nEXPLAINER: LESSON\n" + "=" * 68)
    print(lesson)
    print("\n" + "=" * 68 + "\nQUIZ MASTER: QUIZ\n" + "=" * 68)
    print(quiz)

    answers = input("Write your answers (number them 1-5): ").strip()
    if not answers:
        answers = "The student did not submit answers."
    print("\nQuiz Master -> Evaluator: passing lesson, quiz, and student answers...")
    feedback = asyncio.run(evaluate_answers(llm, student_name, topic, lesson, quiz, answers))
    print("\n" + "=" * 68 + "\nEVALUATOR: FEEDBACK\n" + "=" * 68)
    print(feedback)

    score = score_from_feedback(feedback)
    if score is not None and score < 4:
        print(f"Score {score}/5: starting Evaluator -> Explainer re-teaching loop.")
        remedial = asyncio.run(re_teach_weak_area(llm, student_name, level, topic, feedback))
        print("\n" + "=" * 68 + "\nEXPLAINER: REMEDIAL LESSON\n" + "=" * 68)
        print(remedial)
    elif score is None:
        print("Score format not detected. Review evaluator feedback manually; loop not auto-triggered.")
    else:
        print(f"Score {score}/5: re-teaching loop not needed.")

    memory = save_memory(student_name, topic, level, score, feedback)
    print("\nStudent memory saved to data/leo_memory.json")
    print(memory)


if __name__ == "__main__":
    main()
