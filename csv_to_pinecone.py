import pinecone
import pandas as pd
from sentence_transformers import SentenceTransformer

# Initialize Pinecone
pc = pinecone.Pinecone(api_key="65afc432-0159-43e7-92b9-d37f6bf1ce76")

# Create a new index with the specified dimension and metric
index_name = "quickstart"
dimension = 384  # Dimension for Sentence-BERT embeddings
metric = "cosine"  # Cosine similarity metric

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric=metric,
        spec=pinecone.ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# Connect to the index
index = pc.Index(index_name)

# Load your CSV file
df = pd.read_csv(r'UAE.csv')  # Replace with the path to your CSV file


# Combine 'desription' and 'inner-content' columns into a single text column
df['combined_text'] = df['desription'].fillna('') + ' ' + df['inner-content'].fillna('')

# Preprocess and embed your data
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df['combined_text'].tolist())

# Insert data into the vector database
for i, embedding in enumerate(embeddings):
    index.upsert([(str(i), embedding.tolist(), {'text': df['combined_text'].iloc[i]})])

print("Data has been successfully inserted into the Pinecone vector database.")
