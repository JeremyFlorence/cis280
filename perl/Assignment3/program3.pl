#!/usr/bin/perl
# Name: Jeremy Florence
# Course: CIS 280 - Perl
# Assignment: 3 - Program 3
# Date: 5/1/17

# This program checks if a string contains a valid number.
# A number can have any number of digits, but it can have only digits and a decimal
# point. The decimal point is optional, but if it appears in the number, there must be
# only one, and it must have digits on its left and its right. There should be
# whitespace or a beginning or end-of-line character on either side of a valid
# number. Negative numbers are preceded by a minus sign

use strict;
use warnings;

print "Enter a string with a valid number: ";
my $input = <STDIN>;
chomp($input);

if ($input =~ /^\s*[\-]?[0-9]+\.?[0-9]*\s*$/) {
    print "It has a valid number\n";
} else {
    print "Not a valid number\n";
}

