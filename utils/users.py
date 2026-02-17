import os

USERS = {
    "standard": os.getenv("STANDARD_USER"),
    "locked": os.getenv("LOCKED_OUT_USER"),
    "problem": os.getenv("PROBLEM_USER"),
    "performance": os.getenv("PERFORMANCE_GLITCH_USER"),
    "error": os.getenv("ERROR_USER"),
    "visual": os.getenv("VISUAL_USER"),
}

PASSWORD = os.getenv("PASSWORD")

VALID_USERS = ["standard", "problem", "performance", "error", "visual"]
INVALID_USERS = ["locked"]