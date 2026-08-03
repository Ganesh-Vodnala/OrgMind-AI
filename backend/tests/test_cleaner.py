from app.engines.processing.cleaners.implementations.basic_text_cleaner import (
    BasicTextCleaner
)


text = """
        Python        Java        SQL


Artificial Intelligence


Machine Learning



Deep Learning
"""

cleaner = BasicTextCleaner()

cleaned_text = cleaner.clean(text)

print("========== BEFORE ==========")
print(text)

print("\n========== AFTER ==========")
print(cleaned_text)