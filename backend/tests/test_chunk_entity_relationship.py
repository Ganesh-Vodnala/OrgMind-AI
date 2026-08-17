from app.engines.processing.models.entity import Entity
from app.engines.processing.models.text_chunk import TextChunk


chunk = TextChunk(
    content="Python uses Redis",
    chunk_index=0,
    start_offset=0,
    end_offset=17
)

python_entity = Entity(
    text="Python",
    entity_type="TECHNOLOGY",
    start_offset=0,
    end_offset=6
)

redis_entity = Entity(
    text="Redis",
    entity_type="TECHNOLOGY",
    start_offset=12,
    end_offset=17
)

chunk.entities.append(python_entity)
chunk.entities.append(redis_entity)


print("Chunk:")
print(chunk.content)

print("\nEntities:")

for entity in chunk.entities:
    print(
        entity.text,
        entity.entity_type,
        entity.start_offset,
        entity.end_offset
    )


assert len(chunk.entities) == 2

assert chunk.entities[0].text == "Python"
assert chunk.entities[1].text == "Redis"

assert chunk.entities[0].entity_type == "TECHNOLOGY"
assert chunk.entities[1].entity_type == "TECHNOLOGY"

print("\n==============================")
print("CHUNK-ENTITY TEST PASSED")
print("==============================")