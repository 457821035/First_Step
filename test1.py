# -*- coding:utf-8 -*-

print "Hello World!"
print "Hello Again"
print 'yay! Printing.'
print "i'd much rather you 'not'."
#print 'I "Said" do not touch this.'
print "世界是如此的大"


for i in range(0,5):
	print "*"

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary , do_not)

print x
print y

print "I said %r. " % x
print "I also said %s." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e