# Contributing to GradeEvaluator 🚀

First off, thank you for considering contributing to GradeEvaluator! It's people like you that make GradeEvaluator such a great tool for students.

## Where do I go from here?

If you've noticed a bug or have a feature request, make sure to check our [Issues](https://github.com/gemachistesfaye/GradeEvaluator/issues) page to see if someone else has already created a ticket. If not, go ahead and [make one](https://github.com/gemachistesfaye/GradeEvaluator/issues/new/choose)!

## Fork & create a branch

If this is something you think you can fix, then fork GradeEvaluator and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```sh
git checkout -b 325-add-localization-support
```

## Implementation Guidelines

### Frontend (Vanilla JS + CSS)
- We use Vanilla CSS (no Tailwind) to keep the project lightweight.
- Ensure that any new styles respect our `dark-theme` CSS variables located in `base.html`.
- Maintain the glassmorphism and modern UI aesthetics of the project.
- Write clean, modular Vanilla JavaScript. Keep scope contained.

### Backend (Python/Flask)
- Follow PEP 8 style guide for Python code.
- Ensure all new routes in `app.py` handle both GET and POST requests appropriately if form data is involved.
- Add logging where necessary, but keep it clean.

## Get the test suite running

Make sure your local environment is set up:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Make sure you can successfully run `python run.py` and interact with the application on `http://localhost:5000`. Test your changes manually to ensure no UI breakages occur.

## Make a Pull Request

When you're ready to submit a PR:
1. Ensure your code follows the style guidelines.
2. Provide a descriptive title for your PR.
3. Fill out the Pull Request Template completely.
4. Include screenshots if your PR introduces visual changes.

At this point, you're waiting on us. We like to at least comment on pull requests within three business days (and, typically, one business day). We may suggest some changes or improvements or alternatives.

Thank you for contributing! 🎉
