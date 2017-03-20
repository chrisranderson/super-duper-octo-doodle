import scholar.scholar as sch
import penseur.penseur as pens
import topic_generation
import random
import time
import nltk.data
import pickle
from punch_lines import *
import numpy as np
import skipthought_decode_helper
import censor

#import sys
#sys.setrecursionlimit(10000)

#EVALUATION FUNCTIONS

def wildly_exaggerate(joke):
    pass

def alliterize(joke):
    pass


#JOKE MAXIMIZERS



class Comedian:
#not sure whether joke should be just a 
#string of text or a class with its oen
#properties and functions.

    def __init__(self):
        #print "Initializing scholar..."
        self.scholar = sch.Scholar()

	print "loading penseur data structure (this will take about 90 seconds...)"
	#with open('Wikipedia_first_10000_lines.pkl', 'rb') as handle:
	#    self.penseur = pickle.load(handle)
	self.penseur = pens.Penseur()
        self.decode_helper = skipthought_decode_helper.decode_helper('larry_king_50000_lines', self.penseur)
#
    #GENERATION FUNCTIONS


    def score_match(self, match):
	#score word pairs based on interest level...
	score = 0
        word1 = match[0] + '_' +  self.scholar.get_most_common_tag(match[0])
        word2 = match[1] + '_' + self.scholar.get_most_common_tag(match[1])

	#low score for synonyms - we want words with different connotations
	print self.scholar.get_cosine_similarity(word1, word2)
	dist = self.scholar.get_cosine_similarity(word1,word2)
	print "COSINE SIMILARITY: %f" % (dist)
	score += (1-dist)

	#high score if one of the words is a proper noun?

	#high score if one or both words has an emotional connotation

	#high score if it's a verb/noun or adj/noun pair?

	#high score if both words are common
	#(Common words tend to appear near the mean of the vector space)
#	mean_vector = np.mean(self.scholar.model.vectors)
#	diff = abs(self.scholar.model[word1].dot(mean_vector)) + abs(self.scholar.model[word2].dot( mean_vector))
#	print "NOVELTY SCORE: %f" % (diff)
#	score += diff

	#high score if the words have a high difference in length
	length_diff = abs(len(match[0]) - len(match[1])) / max(len(match[0]), len(match[1]))
	print "LENGTH DISTANCE: %i" % (length_diff)
        score += length_diff


	#print "match %i" % score
	return score

    def find_a_random_match(self, association_lists):
	#randomly match items from different lists
    
        if len(association_lists) == 0:
            return None

        #only one list, so we match it with itself
        word1 = 'empty'
        word2 = 'empty'
        counter = 0
	MAX_ITERATIONS = 100

        while ((word1 == word2) or word1 == 'empty' or word2 == 'empty') and counter < MAX_ITERATIONS:
	    assoc_list1 = random.choice(association_lists)
	    assoc_list2 = random.choice(association_lists)
	    if len(assoc_list1) != 0:
		word1 = random.choice(assoc_list1)
	    if len(assoc_list2) != 0:
		word2 = random.choice(assoc_list2)
            counter += 1
        return (word1, word2)

    def filterAssociations(self, associations):
        #prune any associations that aren't in the word2vec listings
	#also prune options that are too short

	filtered_associations = []
        for word in associations:
            tagged_word = word + '_' +  self.scholar.get_most_common_tag(word)
            if self.scholar.exists_in_model(tagged_word) and len(word) >= 3:

		if censor.is_english_word(word):
                    filtered_associations.append(word)
	return filtered_associations

    def find_a_match(self, assoc_list):
        #for now, randomly match items from different lists
        #BUT WE WILL MAKE THIS SMARTER LATER!
        return self.find_a_random_match(assoc_list)

    def getAssociations(self,handle):
        associations = []
        for h in handle:
            if type(h) == unicode:
		word = h
	    else:
		word = h.lower_
	    tags = ['_JJ', '_JJR', '_JJS', '_NN', '_VB', '_NNP', '_NNPS', 'NNS', 'UH']
            for tag in tags:
                if self.scholar.exists_in_model(word+tag):
                    indexes, metrics = self.scholar.model.cosine(word + tag)
                    response = self.scholar.model.generate_response(indexes, metrics, 5)
                    for r in response:
                        #strip tags and append to list
                        associations.append(r[0][:r[0].index('_')])
        return associations


    def getTopic(self):
        topics = topic_generation.get_topics()
        return random.choice(topics)

    def buildBasicJoke(self, topic):
	handles = identify_handles(topic)
	if len(handles) < 1:
            print "\nNot enough handles found. switching to get_words_by_rarity"
            handles = self.scholar.get_words_by_rarity(topic)
	print "\nHANDLES:"
	print handles

	associations = {}
	association_lists = []
        for h in handles:
            associations = self.getAssociations(h)
	    association_lists.append(self.filterAssociations(associations))
            print association_lists[-1]


	print "\n MATCHED ASSOCIATIONS:"
	matched = self.find_a_match(association_lists)
	#matched = self.find_a_match(association_lists)
	print matched
        word1 = matched[0] + '_' +  self.scholar.get_most_common_tag(matched[0])
        word2 = matched[1] + '_' + self.scholar.get_most_common_tag(matched[1])
	print self.scholar.get_cosine_similarity(word1, word2)
        print self.score_match(matched)

	#primitive_joke_structure = Topic + matched[0] + matched[1]

	#find the embedded location of primitive_joke
	#decode that location to form a grammatically complete sentence (?)

	
	input1 = matched[0] + ' ' + matched[1]
        target_vector = self.penseur.get_vector(input1)
	output1 = self.decode_helper.decode(target_vector)
        print "\nINPUT1: " + input1
        print "OUTPUT: " + output1
	
	input2 = matched[1] + ' ' + matched[0]
        target_vector = self.penseur.get_vector(input2)
	output2 = self.decode_helper.decode(target_vector)
        print "\nINPUT2: " + input2
        print "OUTPUT: " + output2
	
	input3 = matched[0] + ' ' + matched[1] + ' ' +  matched[0] + ' ' + matched[1] + ' ' + matched[0] + ' ' + matched[1] + '.'
        target_vector = self.penseur.get_vector(input3)
	output3 = self.decode_helper.decode(target_vector)
        print "\nINPUT3: " + input3
        print "OUTPUT: " + output3
	
        input4 = topic
        target_vector = self.penseur.get_vector(input4)
	output4 = self.decode_helper.decode(target_vector)
        print "\nINPUT4: " + input4
        print "OUTPUT: " + output4
        
        input5 = matched[0] + ' ' + matched[1] + ' ' + topic
        target_vector = self.penseur.get_vector(input5)
	output5 = self.decode_helper.decode(target_vector)
        print "\nINPUT5: " + input5
        print "OUTPUT: " + output5
        
	input6 = topic + ' ' + matched[0] + ' ' + matched[1]
        target_vector = self.penseur.get_vector(input6)
	output6 = self.decode_helper.decode(target_vector)
        print "\nINPUT6: " + input6
        print "OUTPUT: " + output6

	if len(association_lists) > 0 and len(association_lists[0]) > 2:
            input7 = " ".join(association_lists[0]) #first set of associations...
            target_vector = self.penseur.get_vector(input7)
	    output7 = self.decode_helper.decode(target_vector)
            print "\nINPUT7: " + input7
            print "OUTPUT: " + output7

        if len(handles) > 2:
	    adjusted_topic = topic.replace(handles[0].lower(), matched[0])
            adjusted_topic = adjusted_topic.replace(handles[1].lower(), matched[1])
            input8 = adjusted_topic
            target_vector = self.penseur.get_vector(input8)
	    output8 = self.decode_helper.decode(target_vector)
            print "\nINPUT8: " + input8
            print "OUTPUT: " + output8

        print "\n"
	
	return topic + ': ' + output5

    def optimizeJoke(self, joke):
        #executes one or more optimisers on
        #the joke, then returns the new version
        return joke

    def createJoke(self, topic):
        joke = self.buildBasicJoke(topic)
        joke = self.optimizeJoke(joke)

        return joke


    def begin(self):
        print "\nI'm going to tell you a joke:"
        time.sleep(1)

        response = 'y'
        while response == 'y':
           topic = self.getTopic()
           print "\nTopic is '" + topic + "'"

	   joke = self.createJoke(topic)

           print joke
           #(pass the joke to espeak?)
           time.sleep(1)

           response = raw_input("Want to hear another one?(y/n): ")
           
        "Okay, bye!"

c = Comedian()
c.begin()
