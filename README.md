# Leo: Multi-Agent AI Tutor

A CrewAI + Google Gemini learning assistant that coordinates a personalised learning session through four specialised agents. The Google Colab notebook is the primary assignment deliverable; a modular Python entry point is also included for local execution.

## Project overview

Leo uses a sequential multi-agent workflow:

1. **Learning Coordinator** — gathers the student's level and topic, then creates a learning plan.
2. **Concept Explainer** — teaches the topic using the Coordinator's plan, a worked example, and a recap.
3. **Quiz Master** — creates five practice questions based on the plan and lesson.
4. **Answer Evaluator** — reviews the student's answers, provides a score out of five, and identifies strengths and weak areas.

**Bonus feedback loop:** if the detected score is below 4/5, the Explainer receives the evaluator's feedback and produces a remedial mini-lesson with two check questions.

Student name, last topic, and session summaries are stored in a local JSON memory file.

## Repository contents

```text
Leo-Multi-Agent-AI-Tutor/
├── Leo_Multi_Agent_AI_Tutor_v2.ipynb  # Google Colab assignment notebook
├── main.py                            # Local Python entry point
├── requirements.txt                   # Python dependencies
├── .env.example                       # Safe environment-variable template
├── .gitignore                         # Excludes secrets and local memory
├── README.md                          # Project documentation
├── COMMIT_PLAN.md                     # Suggested meaningful commit sequence
├── src/
│   ├── __init__.py
│   ├── config.py                       # Gemini/CrewAI configuration
│   ├── agents.py                       # Four agent definitions
│   ├── memory.py                       # JSON student memory
│   └── workflow.py                     # Handoffs, evaluation, re-teaching
└── data/                               # Runtime-created local memory (not committed)
```

## Run in Google Colab (recommended for the assignment)

1. Open `Leo_Multi_Agent_AI_Tutor_v2.ipynb` in Google Colab.
2. Run the notebook cells in order, from package installation through the assignment checklist.
3. When prompted, enter a Gemini API key from Google AI Studio in the hidden prompt.
4. Enter the student name, learning level, and topic.
5. Answer all five quiz questions when prompted.
6. Review the evaluator feedback, optional re-teaching output, and saved-memory confirmation.

Do not put the API key in a notebook code cell, notebook output, screenshot, or Git commit.

## Run locally

Requires Python 3.10 or newer.

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

The program asks for a Gemini API key through a hidden prompt if `GEMINI_API_KEY` or `GOOGLE_API_KEY` is not already set. You may optionally copy `.env.example` to `.env` and set the environment variable yourself; `.env` is ignored by Git.

## Configuration

- Default model: `gemini-3.5-flash-lite`
- Override the model with `GEMINI_MODEL`.
- API key: `GEMINI_API_KEY` or `GOOGLE_API_KEY`.
- Colab memory file: `/content/leo_memory.json`.
- Local memory file: `data/leo_memory.json`.

Model availability, API quota, and temporary Google API service load can affect live runs. A `503 UNAVAILABLE` response generally indicates that the model service is temporarily unavailable or under heavy demand; it is not by itself proof that the notebook code is invalid. Retry later and check Google AI Studio model access and quota.

## Security

- Never commit a real Gemini API key.
- `.env` and local student memory are excluded by `.gitignore`.
- `.env.example` contains only a placeholder, not a working secret.
- Check notebook cells and outputs before publishing to ensure no key was accidentally saved.

## Assignment checklist

- [x] Four distinct agents with separate roles, goals, and backstories
- [x] CrewAI framework
- [x] Sequential task orchestration and context handoffs
- [x] Coordinator plan → Explainer lesson → Quiz Master quiz
- [x] Quiz, lesson, and student answers → Evaluator
- [x] Student/topic memory stored in JSON
- [x] Bonus Evaluator → Explainer re-teaching loop for scores below 4/5
- [x] Secure Gemini API-key prompt and API preflight test

## Demo video

Record a 3–5 minute screen video showing one complete learning session, agent handoffs, the quiz, evaluation, and the re-teaching loop if it is triggered. The video must be recorded by the student.
