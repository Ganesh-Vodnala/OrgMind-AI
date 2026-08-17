from app.engines.processing.models.entity import Entity

from app.engines.processing.relationship_extractors.implementations.basic_relationship_extractor import (
    BasicRelationshipExtractor
)


extractor = BasicRelationshipExtractor()


# ==========================================
# Test 1: USES
# ==========================================

text = "Rajesh uses Redis."

entities = [
    Entity(
        text="Rajesh",
        entity_type="PERSON",
        start_offset=0,
        end_offset=6
    ),
    Entity(
        text="Redis",
        entity_type="TECHNOLOGY",
        start_offset=13,
        end_offset=18
    )
]

relationships = extractor.extract(
    text,
    entities
)

print("\nTest 1")

for relationship in relationships:
    print(
        relationship.source_entity.text,
        "->",
        relationship.relationship_type,
        "->",
        relationship.target_entity.text
    )

assert len(relationships) == 1

assert relationships[0].source_entity.text == "Rajesh"
assert relationships[0].target_entity.text == "Redis"
assert relationships[0].relationship_type == "USES"


# ==========================================
# Test 2: DEPENDS_ON
# ==========================================

text = "Payment Service depends on Redis."

entities = [
    Entity(
        text="Payment Service",
        entity_type="SERVICE",
        start_offset=0,
        end_offset=15
    ),
    Entity(
        text="Redis",
        entity_type="TECHNOLOGY",
        start_offset=28,
        end_offset=33
    )
]

relationships = extractor.extract(
    text,
    entities
)

print("\nTest 2")

for relationship in relationships:
    print(
        relationship.source_entity.text,
        "->",
        relationship.relationship_type,
        "->",
        relationship.target_entity.text
    )

assert len(relationships) == 1

assert relationships[0].source_entity.text == "Payment Service"
assert relationships[0].target_entity.text == "Redis"
assert relationships[0].relationship_type == "DEPENDS_ON"


# ==========================================
# Test 3: USED_BY
# ==========================================

text = "Redis is used by Authentication Service."

entities = [
    Entity(
        text="Redis",
        entity_type="TECHNOLOGY",
        start_offset=0,
        end_offset=5
    ),
    Entity(
        text="Authentication Service",
        entity_type="SERVICE",
        start_offset=17,
        end_offset=39
    )
]

relationships = extractor.extract(
    text,
    entities
)

print("\nTest 3")

for relationship in relationships:
    print(
        relationship.source_entity.text,
        "->",
        relationship.relationship_type,
        "->",
        relationship.target_entity.text
    )

assert len(relationships) == 1

assert relationships[0].source_entity.text == "Authentication Service"
assert relationships[0].target_entity.text == "Redis"

assert relationships[0].relationship_type == "USED_BY"


# ==========================================
# Test 4: No relationship
# ==========================================

text = "Rajesh works at Microsoft."

entities = [
    Entity(
        text="Rajesh",
        entity_type="PERSON",
        start_offset=0,
        end_offset=6
    ),
    Entity(
        text="Microsoft",
        entity_type="ORGANIZATION",
        start_offset=17,
        end_offset=26
    )
]

relationships = extractor.extract(
    text,
    entities
)

print("\nTest 4")

assert len(relationships) == 0


print("\n==============================")
print("ALL RELATIONSHIP TESTS PASSED")
print("==============================")