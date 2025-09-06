"""Password generation utilities with simple, typed APIs.

This module contains the core password generation logic, independent
from any user interface (CLI/GUI). Keep UI code elsewhere and import
these functions for reuse and testing.
"""

from __future__ import annotations

import random
import string
from typing import List


def generate_password(
    length: int = 12,
    *,
    use_lower: bool = True,
    use_upper: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
) -> str:
    """Generate a random password.

    Rules:
    - At least one character from each selected character set is included.
    - The total length must be >= the number of selected sets.

    Args:
        length: Desired password length.
        use_lower: Include lowercase letters.
        use_upper: Include uppercase letters.
        use_digits: Include digits.
        use_special: Include punctuation/special characters.

    Returns:
        A random password string.

    Raises:
        ValueError: If no character sets are selected or length is too small.
    """

    pools: List[str] = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_special:
        pools.append(string.punctuation)

    if not pools:
        raise ValueError("Select at least one character type (lower/upper/digits/special).")

    min_len = len(pools)
    if length < min_len:
        raise ValueError(f"Password length must be at least {min_len} for the selected options.")

    # Ensure at least one from each selected pool
    password_chars = [random.choice(pool) for pool in pools]

    # Fill the remainder from the combined pool
    all_chars = "".join(pools)
    password_chars += random.choices(all_chars, k=length - len(password_chars))

    random.shuffle(password_chars)
    return "".join(password_chars)
