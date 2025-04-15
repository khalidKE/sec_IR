## 📘 README – Boolean Retrieval with Posting List (Inverted Index)

### 🧠 Overview
This project demonstrates a basic **Information Retrieval System** using the **Boolean Retrieval Model** and an **Inverted Index** (Posting List). It allows for efficient search of documents based on Boolean queries like `AND`.

### 📂 Project Structure
```
boolean_retrieval/
│
├── main.py         # Main script to build inverted index and perform queries
├── README.md       # Project documentation
```

### 📌 Features
- Build an **inverted index** from a set of documents.
- Support for **Boolean AND** query.
- Simple and clear console output for both the posting list and query result.

### 🔧 How It Works

1. **Preprocessing:**
   - Converts all text to lowercase.
   - Splits text into words (tokenization).

2. **Inverted Index:**
   - For each unique word (term), the index stores a list of document IDs where it appears.

3. **Boolean AND Query:**
   - Returns documents that contain **both** of the queried terms.

### 🚀 Usage

#### 📜 Sample Documents
```python
documents = {
    1: "data science study data",
    2: "machine learning subset data science"
}
```

#### 🧪 Running a Query
To find documents containing **both** "data" and "learning":
```python
result = boolean_and("data", "learning")
print(result)  # Output: [2]
```

### 🖥️ Example Output
```
Posting List:
data: [1, 2]
learning: [2]
machine: [2]
science: [1, 2]
study: [1]
subset: [2]

Result for query 'data AND learning': [2]
```

هل تحب أرسله لك كملف `.md` جاهز للتحميل؟
