from collections import defaultdict

documents = {
    1: "data science study data",
    2: "machine learning subset data science"
}

def preprocess(text):
    return text.lower().split()  

inverted_index = defaultdict(set)

for doc_id, text in documents.items():
    for term in preprocess(text):
        inverted_index[term].add(doc_id)

for term in inverted_index:
    inverted_index[term] = sorted(inverted_index[term])

print("Posting List:")
for term, postings in sorted(inverted_index.items()):
    print(f"{term}: {postings}")

def boolean_and(term1, term2):
    return list(set(inverted_index.get(term1, [])) & set(inverted_index.get(term2, [])))

query_result = boolean_and("data", "learning")
print("\nResult for query 'data AND learning':", query_result)
