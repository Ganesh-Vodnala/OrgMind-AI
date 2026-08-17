from app.engines.processing.entity_extractors.implementations.basic_entity_extractor import (
    BasicEntityExtractor
)


extractor = BasicEntityExtractor()


# --------------------------------------------------
# Test 1: Basic extraction
# --------------------------------------------------

text = "Python and Java are programming languages."

entities = extractor.extract(text)

print("\nTest 1")
for entity in entities:
    print(entity)

assert len(entities) == 2
assert entities[0].text == "Python"
assert entities[0].entity_type == "TECHNOLOGY"
assert entities[1].text == "Java"
assert entities[1].entity_type == "TECHNOLOGY"


# --------------------------------------------------
# Test 2: Case insensitive
# --------------------------------------------------

text = "python and PYTHON"

entities = extractor.extract(text)

print("\nTest 2")
for entity in entities:
    print(entity)

assert len(entities) == 2


# --------------------------------------------------
# Test 3: Java vs JavaScript
# --------------------------------------------------

text = "JavaScript is different from Java."

entities = extractor.extract(text)

print("\nTest 3")
for entity in entities:
    print(entity)

entity_texts = [entity.text for entity in entities]

assert "JavaScript" in entity_texts
assert "Java" in entity_texts
assert len(entities) == 2


# --------------------------------------------------
# Test 4: Multiple occurrences
# --------------------------------------------------

text = "Python is easy. Python is powerful."

entities = extractor.extract(text)

print("\nTest 4")
for entity in entities:
    print(entity)

assert len(entities) == 2


# --------------------------------------------------
# Test 5: Offset correctness
# --------------------------------------------------

text = "The API uses Redis."

entities = extractor.extract(text)

print("\nTest 5")
for entity in entities:
    print(entity)

for entity in entities:

    assert entity.text == text[
        entity.start_offset:entity.end_offset
    ]


# --------------------------------------------------
# Test 6: Empty text
# --------------------------------------------------

entities = extractor.extract("")

assert entities == []


print("\n==============================")
print("ALL ENTITY TESTS PASSED")
print("==============================")