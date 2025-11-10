# Google 5-Day AI Agents Intensive Course

Working through Google's [5-Day AI Agents Intensive Course](https://www.kaggle.com/learn-guide/5-day-agents) using local Jupyter notebooks instead of Kaggle, with UV for Python package management and Claude Code for AI-assisted development.

Course details: [docs/00_course.md](docs/00_course.md)

## Setup

### 1. Install Dependencies

```bash
# Install all dependencies (including google-adk)
uv sync

# Configure git for clean notebook commits
uv run nbstripout --install

# Install pre-commit hooks
uv run pre-commit install
```

### 2. Configure Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/api-keys)
2. Create a new API key and save in new root file `.env`
3. Save into `.env` as: GOOGLE_API_KEY=your_actual_api_key_here

## Project Structure

- `notebooks/` - Jupyter notebooks for course exercises
- `src/agent_course_google/` - Reusable code modules
- `scripts/` - Standalone utilities
- `tests/` - Test files
- `docs/` - Course materials and documentation
