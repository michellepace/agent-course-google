# Google 5-Day AI Agents Intensive Course

Working through Google's [5-Day AI Agents Intensive Course](https://www.kaggle.com/learn-guide/5-day-agents) using local Jupyter notebooks instead of Kaggle, with UV for Python package management and Claude Code for AI-assisted development.

Course details: [docs/00_course.md](docs/00_course.md)

## Setup

```bash
# Install dependencies
uv sync

# Configure git for clean notebook commits
uv run nbstripout --install

# Install pre-commit hooks
uv run pre-commit install
```

## Project Structure

- `notebooks/` - Jupyter notebooks for course exercises
- `src/agent_course_google/` - Reusable code modules
- `scripts/` - Standalone utilities
- `tests/` - Test files
- `docs/` - Course materials and documentation
