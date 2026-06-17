from mode_loader import get_model

model = get_model()

def prepare_text(chunk):
    return f"""
TYPE: {chunk['type']}
FILE: {chunk['file']}

CONTENT:
{chunk['code']}
""".strip()


def create_embeddings(chunks, repo_url=None):
    import logging
    logger = logging.getLogger(__name__)

    texts = [prepare_text(c) for c in chunks]

    try:
        embeddings = model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True
        )
        logger.info(f"🧠 Embedding success | Repo: {repo_url} | Chunks: {len(chunks)}")

    except Exception as e:
        logger.error(f"❌ Embedding failed | Repo: {repo_url} | Error: {str(e)}")
        raise

    # attach embedding to each chunk so score_chunks can access chunk["embedding"]
    for chunk, emb in zip(chunks, embeddings):
        chunk["embedding"] = emb

    return chunks