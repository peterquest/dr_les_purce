from botinator import *
import random, time

# Les Purce chat bot for great good.

## response functions

def generate_evergreen_class(matches, messenger):
	intros = ["Check out our new program: ", "Why don't you enroll in this upcoming program: ", "Your question will be answered in this program: ", "You can explore this further in this program: "]

	# lists of evergreen class words.
	# these must be gerunds of transitive verbs. for example 'looking' doesn't work ('looking social diversity').
	gerunds = ["Discovering", "Imagining", "Drawing", "Defending", "Writing", "Rewriting", "Interrogating", "Examining", "Reinterpreting", "Engaging", "Exploring", "Interpreting", "Improvising", "Envisioning", "Understanding", "Reinventing"]
	adjectives = ["Real", "Literary", "Imagined", "Cultural", "Evolutionary", "Social", "Forbidden", "Sustainable", "Emergent", "Dynamic", "Interdisciplinary", "Growth-based", "Sustainable", "Gothic", "An Introduction To", "Non-postmodern","Modern","Diverse"]
	nouns = ["Alternatives", "Foundations", "Representations", "Narratives", "Crafts", "Biodiversity", "Knowledge", "Abjection", "Art", "Time", "Argentina", "Plants", "People", "Ecoliteracy", "Change", "Mausoleums", "Systemizations", "Equality Speech", "Male Privelege", "Gender-Power", "Freewriting", "Media Studies", "Studies", "Afro-Brazilian Dance", "Approaches to Healing", "Ballet", "Art/Work", "Foundations of Change", "Form", "Function", "Dance Creations", "Power Dynamics", "Heteronormativity", "Inverted Sexuality", "Sexuality", "Polyamory", "Freestyle Deforestation","Yoga"]

	# random pop
	def popr(ls):
		if ls == []: return ''
		return ls.pop(random.randrange(len(ls)))

	# Grammar rules represented as functions returning formatted strings
	titles = lambda: random.choice([
		"%s %s %s" % (popr(gerunds), popr(adjectives), popr(nouns)),
		"%s %s"    % (popr(adjectives), popr(nouns)),
		"%s"       % popr(nouns)
	])
	formats = lambda: random.choice([
		"From %s Towards %s" % (titles(),titles()),
		"Between %s and %s"  % (titles(),titles()),
		"%s: %s"             % (titles(),titles()),
		"%s: %s and %s"      % (titles(),titles(),titles()),
		"%s and %s"          % (titles(),titles()),
		"%s"                 % titles()
	]) # you could abstract out the prepositions [and, of] if you wanted
	return random.choice(intros) + formats() # end generate_evergreen_class

# Response totally not driven by context. Placeholders until he gets smarter.
def generic(matches, messenger):
	return random.choice(["Let's all hold hands in red square.","You are the future.", "I have my own secret cave in the evergreen woods.", "I am immortal.","We can work through this together.","I wrote a song for you on my guitar.","This sounds like a good topic for a rap song.", "Beedoop badop bop", "As Martin Luther King Jr said 'everyone loves a good pie'", "I sleep in a lean-to in the woods. Bee bop badoobop.", "Good point. Let's have a seminar about it"])

def insulted(matches, messenger):
	return random.choice(["Talk to my mustache.","Let me console you with my guitar.","Check your pie plate. Did you grease it?","Talk to my secretary.","Art Constantino will handle this.", "Better grease yo pie plate", "You need more interdisciplinary education"])

# need to fix botinator.when method
# def is_420():
# 	return time.strftime("%H%M") == "1620"

bot = Bot('irc.freenode.net',6667,'DrLesPurce','les','Dr Les Purce (1.1)')
bot.join('#tesc')
bot.bind('DrLesPurce:.*fuck(ing)?|shit|dammit|damn|stupid|dumb|lame.*', insulted)
bot.bind('DrLesPurce: .*\?', generate_evergreen_class) # When asked a question, suggest to join a program
bot.bind('DrLesPurce: .*', generic) # fallback: say something random

bot.live()
