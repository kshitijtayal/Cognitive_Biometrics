Cognitive-Biometric Recognition from weblogs : A feasibility study
==================

Code made available to reproduce results reported in the paper: "Cognitive-Biometric Recognition from weblogs : A feasibility study", Neeti Pokhriyal, Kshitij Tayal ,Ifeoma Nwogu, Venugopal Govindaraju

- SyntacticFeatureExtractor.java - to extract stylistic features from the blogs description (https://github.com/neetip/languagebiometrics)
- stemmer.java - Used within SyntacticFeatureExtractor
- Blog.java - Used within SyntacticFeatureExtractor
- csv2arff.py - Converts csv file into arff, to fed into weka
- mallet_command.txt - command to extract 50 topics from the dataset
- pca.py - code to check the variance and calculate principal components
- Syntactic_pair_generator.py - extracts syntactic_pair for the blogs description
- row_normalization - row normalizes the matrix, used for output for syntactic_pair_generator
- author_fingerprint.py - average all the featurevalue written by the same author to get unique signature
- topic.py - outputs topic matrix, inputs mallet output
- visualize_author.m - non_classical multidimension scaling of authors
- visualize_genimp - non_classical multidimension scaling of genuine/Imposter class
- get_tier.py - generates subset of tier1 according to syntactic_pair_generator
- count_blog - counts the number of blog written by same author
- Avg_sen.py - calculates the average length of sentence in a blog




DESCRIPTION:

- Syntactic_pair_generator.py - For extracting pairs enter range of blog written by an author.Eg. For Data 5 range will be 5 to 10.It will take countblog.txt file as input which contains number of blogs written by a particular author.Also  Enter the number of datapoints per thread.There are three files that are outputted.
- Run row_normalization to normaize the features
- get_tier.py - Generates the subset of tier1 according to the author list of Syntactic_pair_generator.  
- After that Stylistic Feature can be extracted from SyntacticFeatureExtractor.java.
- Extract features from mallet software (http://mallet.cs.umass.edu) file.Delete 1st row and run topic.py
- Combine all the three feature set into combinedmatrix.csv
- Run pdist2.java on  combinedmatrix.csv.(Code for pdist2 avilable on https://github.com/neetip/languagebiometrics)
- Run csv2arff.py on the output given by pdist2.java to convert csv file  to arff format.
- Run Weka's logistic regression on the arff file to get the desired output.

-------
Data: Data can be accessed from http://www.icwsm.org/data/
To extract personal stories from the dataset, refer to: http://people.ict.usc.edu/~gordon/srp.html
