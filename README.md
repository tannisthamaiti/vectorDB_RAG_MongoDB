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
type:"movie"

tomatoes:Object
num_mflix_comments
0
plot_embedding_hf
Array (384)

