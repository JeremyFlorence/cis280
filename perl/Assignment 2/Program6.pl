#!/usr/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 2
# Date: 4/17/17
use strict;
use warnings;

my $currentTime = localtime;
my @currentTime = localtime;

print "The current time (as scalar) is: $currentTime. \n";
print "The current time (as list) is: $currentTime[2]:$currentTime[1]:$currentTime[0]. \n";