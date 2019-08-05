# Tamizh
Machine/Deep Learning with the  Tamil (Oldest Language)

The aim is to create ML specific applications and enhancements with Tamil Language. 

## Code Usage
### tawiki_convert_bz2_to_xml.ipynb
Extracts the bz2 compressed article to xml file. Mainly created to avoid large transactions to cloud. 
Upload the compressed file and extract in the cloud. 
Download the article page from [WikiMedia Tamil Data](http://dumps.wikimedia.org/tawiki/latest/)

### tawiki_data_extraction_cleaning.ipynb
Extracts each articles "Title" and clean "Content" from the XML tree and exports to Tabular Data for easy use. 
Used many `regex` rules to clean the data. 


### Tamizh_Word2Vec.ipynb
Word embeddings for Tamil words using `gensim` library. 
This creates the similarity metrics between the words. 

Training model parameter can be adjusted to extend its usage.


# NEXT 
1. DL based Language Modelling
2. Document Similarity Model
3. NER 
4. Sentiment detection
5. ETC.... 
