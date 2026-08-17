from app.services.processing.processing_service import ProcessingService


processing_service = ProcessingService()


text = """
Rajesh designed the Authentication Service.
The Authentication Service uses Redis.
"""


processed_document = processing_service.process(text)


print("\n========== CLEANED TEXT ==========")
print(processed_document.cleaned_text)


print("\n========== CHUNKS ==========")

for chunk in processed_document.chunks:

    print(
        f"\nChunk {chunk.chunk_index}"
    )

    print("Content:", chunk.content)

    print("Entities:")

    for entity in chunk.entities:

        print(
            " ",
            entity.text,
            "|",
            entity.entity_type
        )


print("\n========== RELATIONSHIPS ==========")

for relationship in processed_document.relationships:

    print(
        relationship.source_entity.text,
        "->",
        relationship.relationship_type,
        "->",
        relationship.target_entity.text
    )

    print(
        "Evidence:",
        relationship.evidence
    )


print("\n========== ASSERTIONS ==========")

relationship_types = [
    relationship.relationship_type
    for relationship in processed_document.relationships
]


assert "DESIGNED" in relationship_types
assert "USES" in relationship_types


assert len(processed_document.relationships) == 2


print("Relationship extraction verified.")

print("\n==============================")
print("COMPLETE PROCESSING PIPELINE TEST PASSED")
print("==============================")