from app.engines.processing.models.entity import Entity
from app.engines.processing.models.relationship import Relationship


source = Entity(
    text="Rajesh",
    entity_type="PERSON",
    start_offset=0,
    end_offset=6
)

target = Entity(
    text="Redis",
    entity_type="TECHNOLOGY",
    start_offset=17,
    end_offset=22
)


relationship = Relationship(
    source_entity=source,
    target_entity=target,
    relationship_type="USES",
    evidence="Rajesh uses Redis."
)


print("Source:")
print(relationship.source_entity)

print("\nTarget:")
print(relationship.target_entity)

print("\nRelationship:")
print(relationship.relationship_type)

print("\nEvidence:")
print(relationship.evidence)


assert relationship.source_entity.text == "Rajesh"
assert relationship.target_entity.text == "Redis"

assert relationship.relationship_type == "USES"

assert relationship.evidence == "Rajesh uses Redis."

assert relationship.confidence is None


print("\n==============================")
print("RELATIONSHIP MODEL TEST PASSED")
print("==============================")