# vectorDB_RAG_MongoDB

### Original Sample Movie Data

{"_id":{"$oid":"65fe08ff62a48c85b235846a"},
<br>
"fullplot":"Huge advancements in scientific technology have enabled a mogul to create an island full of living dinosaurs. John Hammond has invited four individuals .....",
<br>
"imdb":{"rating":{"$numberDouble":"8.1"},"votes":{"$numberInt":"527998"},
<br>
"id":{"$numberInt":"107290"}},
<br>
"year":{"$numberInt":"1993"},
<br>
"plot":"During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.",
<br>
"genres":["Adventure","Sci-Fi","Thriller"],
<br>
"rated":"PG-13","metacritic":{"$numberInt":"68"},
<br>
"title":"Jurassic Park",
<br>
"lastupdated":"2015-08-31 00:04:50.280000000",
<br>
"languages":["English","Spanish"],
<br>
etc ...
### After adding embedding field plot_embedding_hf from hugging face all-MiniLM-L6-v2
countries:Array (1)
<br>
type:"movie"
<br>
tomatoes:Object
<br>
num_mflix_comments:0
<br>
plot_embedding_hf:Array (384)
### JSON edits for search index
```
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "plot_embedding_hf": [
        {
          "dimensions": 384,
          "similarity": "dotProduct",
          "type": "knnVector"
        }
      ]
    }
  }
}
```
### Search Result
'''
Movie Name: Gertie the Dinosaur,
Movie Plot: The cartoonist, Winsor McCay, brings the Dinosaurus back to life in the figure of his latest creation, Gertie the Dinosaur.

Movie Name: Regeneration,
Movie Plot: At 10 years old, Owens becomes a ragged orphan when his sainted mother dies. The Conways, who are next door neighbors, take Owen in, but the constant drinking by Jim soon puts Owen on the ...

Movie Name: Tabu: A Story of the South Seas,
Movie Plot: In his final film, F.W. Murnau presents the tale of two young lovers on the idyllic island of Bora Bora in the South Pacific. Their life is shattered when the old warrior declares the girl ...

Movie Name: Dr. Jekyll and Mr. Hyde,
Movie Plot: Dr. Jekyll faces horrible consequences when he lets his dark side run wild with a potion that changes him into the animalistic Mr. Hyde.
'''

