#!/usr/bin/perl
# Name: Jeremy Florence
# Course: CIS 280 - Perl
# Assignment: 3 - Program 1
# Date: 5/1/17

use strict;
use warnings;

print "Enter a string: ";
$_ = <STDIN>;
chomp($_);
s/([\w']+)/\u\L$1/g;
print;
print "\n"; 