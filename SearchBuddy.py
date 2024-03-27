import spacy
import numpy as np
import faiss

nlp = spacy.load("en_core_web_md")

def get_embeddings(texts):
    """Generate embeddings for a list of texts using spaCy."""
    embeddings = []
    for text in texts:
        doc = nlp(text)
        doc_embedding = np.mean([token.vector for token in doc if not token.is_stop], axis=0)
        embeddings.append(doc_embedding)
    return np.array(embeddings)

def similarity_search(query_embedding, data_embeddings, k=5):
    """Perform similarity search using FAISS."""
    index = faiss.IndexFlatL2(data_embeddings.shape[1])
    index.add(data_embeddings)
    _, neighbors = index.search(query_embedding.reshape(1, -1), k)
    return neighbors[0]

def main(keywords, array):
    keyword_embedding = get_embeddings([keywords])
    array_embeddings = get_embeddings(array)
    similar_indices = similarity_search(keyword_embedding, array_embeddings)
    similar_array = [array[i] for i in similar_indices]
    return similar_array


if __name__ == "__main__":
    keywords = "machine learning"
    array = ["Introduction to machine learning", "Deep learning for computer vision", "Natural language processing with Python", "Data visualization techniques", "Introduction to statistics"]
    similar_array = main(keywords, array)
    print("Array in the most similar order to the keywords:")
    print(similar_array)
