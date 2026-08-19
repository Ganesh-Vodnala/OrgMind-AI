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
    print(
    "Embedding dimensions:",
    len(chunk.embedding)
    if chunk.embedding
    else None
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

print("\n========== METADATA ==========")

metadata = processed_document.metadata

print("Knowledge Type:", metadata.knowledge_type)
print("Importance:", metadata.importance)
print("Tags:", metadata.tags)
print("Author:", metadata.author)
print("Project:", metadata.project)
print("Module:", metadata.module)
print("Confidence:", metadata.confidence)

print("\n========== CLASSIFICATION ==========")

classification = processed_document.classification

print(
    "Knowledge Type:",
    classification.knowledge_type
)

print(
    "Confidence:",
    classification.confidence
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

assert processed_document.metadata is not None

assert processed_document.metadata.knowledge_type == "TECHNICAL"

assert processed_document.metadata.importance == "MEDIUM"

assert "Rajesh" in processed_document.metadata.tags

assert "Redis" in processed_document.metadata.tags

assert classification is not None

assert classification.knowledge_type == "TECHNICAL_KNOWLEDGE"

assert classification.confidence == 0.70

assert len(processed_document.chunks) > 0

for chunk in processed_document.chunks:

    assert chunk.embedding is not None

    assert len(chunk.embedding) == 384

print("\n==============================")
print("COMPLETE PROCESSING PIPELINE TEST PASSED")
print("==============================")