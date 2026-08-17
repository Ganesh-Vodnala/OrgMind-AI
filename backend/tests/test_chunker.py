from app.engines.processing.chunkers.implementations.fixed_size_chunker import (
    FixedSizeChunker
)


text = "Hello world this is a test document."


chunker = FixedSizeChunker(
    chunk_size=12,
    overlap=3
)

chunks = chunker.chunk(text)


for chunk in chunks:

    print(
        chunk.chunk_index,
        repr(chunk.content),
        chunk.start_offset,
        chunk.end_offset
    )

    # Important correctness check
    assert chunk.content == text[
        chunk.start_offset:chunk.end_offset
    ]

print("\nAll offset tests passed!")