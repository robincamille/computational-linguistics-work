# -*- coding: utf-8 -*-

# Probability basics

# This code runs over basic probability calculations. It currently runs over 
# a small dataset (defined below) but could be adapted to other data.

#x variable: filipino, french, venezuelan
#y variable: asiangene, europeangene

#
#build and print a table, n=10 ---------------------------------------
#

joint = { 'filipino' : { 'asiangene' : 0, 'europeangene' : 0 }, 'french': { 'asiangene' : 0, 'europeangene' : 0 }, 'venezuelan': { 'asiangene' : 0, 'europeangene' : 0 }  }

def inc(event, x, y): #increments counts of x and y
    """(Table name, x variable, y variable)"""
    joint[x][y] = joint[x][y] + 1        

inc(joint, 'filipino', 'europeangene')
inc(joint, 'filipino', 'asiangene')
inc(joint, 'filipino', 'asiangene')
inc(joint, 'french', 'europeangene')
inc(joint, 'french', 'asiangene')
inc(joint, 'french', 'asiangene')
inc(joint, 'venezuelan', 'europeangene')
inc(joint, 'venezuelan', 'europeangene')
inc(joint, 'venezuelan', 'asiangene')
inc(joint, 'venezuelan', 'asiangene')

print 'Joint probability table:'
for k in joint:
	print k, joint[k]
print

#
#get different totals-------------------------------------------------
#

def gettotal(table): #count all occurrences of all events
    total = 0 
    for k in table:
        for i in table[k].values():
            total = total + i
    return total

def xtotal(table, x): #count all occurrences of x
    xtotal = 0
    for i in table[x].values():
        xtotal = xtotal + i
    return xtotal

def ytotal(table, y): #count all occurrences of y
    ytotal = 0
    for k in table:
        ytotal = ytotal + table[k][y]
    return ytotal

#
#get different kinds of probabilities---------------------------------
#

def prob(table, x, y):
    """Joint probability of x and y occurring together"""
    total = gettotal(table)
    jointprob = table[x][y] / float(total)
    print 'Joint probability of %s with %s: %f' %(x, y, jointprob)
    #print '(n = ', total, ')'
        
def marginalX(table, x):
    """Marginal probability of x"""
    total = gettotal(table)
    xtot = xtotal(table, x)
    margprob = xtot / float(total)
    print 'Marginal probability of %s (x): %f' %(x, margprob)
        
def marginalY(table, y):
    """Marginal probability of y"""
    total = gettotal(table)
    ytot = ytotal(table, y)
    margprob = ytot / float(total)
    print 'Marginal probability of %s (y): %f' %(y, margprob)

def condXY(table, y, x):
    """Conditional probability of p(y|x) (y given x)"""
    xtot = xtotal(table, x)
    condprob = table[x][y] / float(xtot)
    print 'Conditional probability of %s given %s: %f' %(y, x, condprob)
    

#
# run all probability calculations -----------------------------------
#

prob(joint,'french','asiangene')
marginalX(joint, 'filipino')
marginalY(joint, 'asiangene')
condXY(joint,'europeangene','french')

# Robin Camille Davis
# February 28, 2014
# Created for Methods in Computational Linguistics II (Andrew Rosenberg), Homework 1
