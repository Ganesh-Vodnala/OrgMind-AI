from app.engines.processing.chunkers.implementations.fixed_size_chunker import FixedSizeChunker

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

chunker = FixedSizeChunker(chunk_size=5)

chunks = chunker.chunk(text)

for chunk in chunks:
    print(chunk)