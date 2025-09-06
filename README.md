# Password Generator

A simple, clean password generator with a Tkinter GUI and a reusable core module.

## Features

- Strong random passwords with configurable length
- Choose character sets: lowercase, uppercase, digits, special
- Guarantees at least one character from each selected set
- Copy-to-clipboard button in the GUI
- Logic and UI are cleanly separated for reuse and testing

## Requirements

- Python 3.8+ (tested with 3.11)
- Tkinter (bundled with most standard Python installations on Windows)

## Project Structure

- `generator.py` — Core logic to generate passwords (no UI). Import this in tests or other apps.
- `app.py` — Tkinter GUI that uses `generator.py`.
- `pass.py` — Small entrypoint that launches the GUI (kept for backward compatibility).

## Run the App (Windows / PowerShell)

From this folder, run the GUI:

```powershell
# Either of these works
python .\app.py
python .\pass.py
```

If you have multiple Python versions, you may need `py -3`:

```powershell
py -3 .\app.py
```

## Use as a Library

```python
from generator import generate_password

# length=16, include digits but exclude special characters
print(generate_password(16, use_digits=True, use_special=False))
```

### Function Signature

```
generate_password(
	length: int = 12,
	*,
	use_lower: bool = True,
	use_upper: bool = True,
	use_digits: bool = True,
	use_special: bool = True,
) -> str
```

Rules:
- At least one character from each selected set is included.
- The password length must be >= the number of selected sets.

## Troubleshooting

- Error: "Select at least one character type" — Ensure at least one of the options is enabled.
- Error: "Password length must be at least N" — Increase the length to be at least the number of selected sets.
- Tkinter not found — Ensure you installed the standard Python from python.org. The Microsoft Store variant may lack Tkinter.

## Security Tips

- Prefer longer passwords (16+ characters) for better security.
- Store passwords in a reputable password manager instead of plain text files.
- Avoid reusing generated passwords across accounts.
