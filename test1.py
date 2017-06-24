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
print "======"
print w,e
print "======"
print w
print e
print "----------------------------"

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print"""
With the three double-quotes
we will be able to type as much as we like.
Even 4 lines if we want
"""

print "How old are you?",      ##不输出换行符
#age = raw_input()
print "How tall are you"
#height = raw_input("How tall are yo")
#print " %s years old, %s tall" % (age , height)

from sys import argv

script_name, first_para, second_para, third_para = argv
print "the script name is ", script_name , "with first" , first_para ,"and second" , second_para
print "this is"

