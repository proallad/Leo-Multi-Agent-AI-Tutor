# Suggested Git commit sequence

Use these as separate commits so the repository history tells the story of the build. Do not create commits for work that was not actually added.

1. `chore: initialize Leo AI tutor repository` — add `.gitignore`, `requirements.txt`, and the initial README skeleton.
2. `feat: add secure Gemini and CrewAI configuration` — add `src/config.py` and `.env.example`.
3. `feat: define the four tutoring agents` — add `src/agents.py`.
4. `feat: implement sequential learning handoffs` — add `src/workflow.py`.
5. `feat: add persistent student learning memory` — add `src/memory.py`.
6. `feat: add local tutor entry point` — add `main.py`.
7. `docs: add Google Colab assignment notebook` — add `Leo_Multi_Agent_AI_Tutor_v2.ipynb`.
8. `docs: complete setup and assignment documentation` — finish `README.md` and this commit plan.

The notebook remains the primary Colab assignment artifact. The Python files are the modular local-run version of the same workflow.
