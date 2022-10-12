import os
import pandas as pd
import spacy
from itertools import combinations

dir = "C://Users//IJ//Desktop//research2//triples"
nlp = spacy.load('en_core_web_md')

#the code was modified from https://towardsdatascience.com/how-to-filter-out-similar-texts-in-python-c7e7c5f7620e and my partner contributed to it
def pre_process(triples):
    triple_docs = [nlp(x) for x in triples]
    preprocessed_triple_docs = []
    lemmatized_tokens = []

    for triple_doc in triple_docs:
        for token in triple_doc:
            if not token.is_stop:
                lemmatized_tokens.append(token.lemma_)
            
        preprocessed_triple_docs.append(" ".join(lemmatized_tokens))
        del lemmatized_tokens[:]
    
    return preprocessed_triple_docs

def similarity_filter(triples):
    preprocessed_triple_docs = pre_process(triples)

    all_summary_pairs = list(combinations(preprocessed_triple_docs, 2))
    print(len(all_summary_pairs))
    similar_triples = []
    for pair in all_summary_pairs:
        triple1 = nlp(pair[0])
        triple2 = nlp(pair[1])
        similarity = triple1.similarity(triple2)
        if similarity > 0.8:
            similar_triples.append(pair)

    triples_to_remove = []
    for a_triple in similar_triples:
        triple1 = a_triple[0]
        triple2 = a_triple[1]
        if len(triple1) < len(triple2):
            index_for_removal = preprocessed_triple_docs.index(triple1)
        else:
            index_for_removal = preprocessed_triple_docs.index(triple2)
        triples_to_remove.append(index_for_removal)

    similar_triples_counts = set(triples_to_remove)
    similar_triples = [x[1] for x in enumerate(triples) if x[0] in similar_triples_counts]

    if len(similar_triples_counts) == 0:
        return triples
    else:
        for triple in similar_triples:
            idx = triples.index(triple)
            triples.pop(idx)
            
        
        return similarity_filter(triples)


def get_data():
    triples = []

    for file in os.listdir(dir):

        data_file = open(os.path.join(dir, file), 'r')

        

        for line in data_file.readlines():
            data = line.split()
            triple = ""
            for i in range(0, len(data)):
                triple += data[i] + " "
            triples.append(triple)
    
    return triples

def main():
    triples = get_data()
    triples = similarity_filter(triples)

    #data = pd.DataFrame([triples, labels]).T.to_csv("data.csv", header=False, index=False)
    story2_triples = open("filtered_triples/story16_triples.txt",'w')
    for el in triples:
        story2_triples.write(el+"\n")
    story2_triples.close()

if __name__ == '__main__':
    main()
