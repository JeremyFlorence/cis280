#!/usr/bin/perl
# Name: Jeremy Florence
# Course: CIS 280 - Perl
# Assignment: 3 - Program 2
# Date: 5/1/17

# This program counts the number of digits, whitespace characters, and words in an
# input string.

use strict;
use warnings;

print "Enter a string: ";
my $input = <STDIN>;

my $digit_count = ($input =~ tr/[0-9]//);
my $white_count;
while ($input =~ m/\s/g) { $white_count++; }
my $word_count;
while ($input =~ m/\w+/g) { $word_count++; }

print "It has $digit_count digits, $white_count whitespaces, and $word_count words.\n"