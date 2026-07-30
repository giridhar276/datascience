# NLP and Text Analytics Notebook Pack

This pack contains separate Jupyter notebooks for major Python text-processing libraries.

## Notebooks
1. NLTK – tokenization, cleaning, POS tagging, NER, n-grams, VADER sentiment
2. spaCy – industrial NLP pipeline, entities, Matcher, noun chunks, custom component
3. TextBlob – sentiment, subjectivity, noun phrases, spelling correction
4. scikit-learn – TF-IDF, text classification, similarity search, clustering
5. Gensim – LDA topic modelling, Word2Vec, document similarity
6. Hugging Face Transformers – sentiment, zero-shot classification, NER, summarization, QA
7. Regular Expressions – extraction, masking, normalization, log parsing
8. WordCloud and visualization – word clouds, frequencies, bigrams, distributions
9. RapidFuzz – typo-tolerant matching, deduplication, standardization

## Recommended order
Start with Regular Expressions and NLTK, then spaCy and TextBlob. Continue with
scikit-learn and Gensim, and finish with Transformers.

## Running the notebooks
1. Create and activate a Python virtual environment.
2. Install the packages in `requirements.txt`.
3. Start Jupyter Notebook:
   `jupyter notebook`
4. Open notebooks in numerical order.

Some notebooks require one-time downloads of NLTK resources, spaCy models,
or Hugging Face models.
