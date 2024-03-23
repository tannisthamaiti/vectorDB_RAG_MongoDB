import pymongo
import requests

client = pymongo.MongoClient("mongodb+srv://mtannistha:<password>@cluster0.xbgttui.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db= client.sample_mflix
collection = db.movies

hf_token = "<hf_token>"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


def generate_embedding(text: str) -> list[float]:

  response = requests.post(
    embedding_url,
    headers={"Authorization": f"Bearer {hf_token}"},
    json={"inputs": text})

  if response.status_code != 200:
    raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

  return response.json()

query = "Dinosaurus back to life"
### plot_embedding field generated for first 50 entries
# for doc in collection.find({'plot':{"$exists":True}}).limit(100):
#     doc['plot_embedding_hf']= generate_embedding(doc['plot']) #introduce a new field with plot_embedding and replace the old doc
#     collection.replace_one({'_id': doc['_id']}, doc)
### find documents in the collection using vectorSerch field where the plot_embedding_hf field is semantically similar to the 
#provided query, PlotSemanticSearch is the name of the search, numCandidated:how many candidates matches internally before returning 
#final result, top 4 matches
results = collection.aggregate([
  {"$vectorSearch": {
    "queryVector": generate_embedding(query),
    "path": "plot_embedding_hf",
    "numCandidates": 100,
    "limit": 4,
    "index": "PlotSemanticSearch",
      }}
])

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
