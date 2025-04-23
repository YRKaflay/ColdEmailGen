import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self,filepath=r'C:\Users\USER\Projects\RAG\ColdEmailGen\app\res\my_portfolio.csv'):
        self.file_path = filepath
        self.data = pd.read_csv(filepath)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collect = self.chroma_client.get_or_create_collection(name='portfolio')


    def load_portfolio(self):
        if not self.collect.count():
            for _, row in self.data.iterrows():
                self.collect.add(documents=row["Techstack"],
                            metadatas={'links':row["Links"]},
                            ids=[str(uuid.uuid4())])
                
    def query_links(self, skills):
        return self.collect.query(query_texts=skills, n_results=2).get('metadatas',[])