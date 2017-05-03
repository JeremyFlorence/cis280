#!/usr/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 2
# Date: 4/17/17
use strict;
use warnings;

my @theArray = (1, 'a', 2, 'b', 3, 'c', 4, 'd');

print "Array: \n";

foreach my $element (@theArray) {
    print $element . " "
}
print "\n";

print "Hash: \n";

my %theHash = @theArray;

while((my $key, my $value) = each %theHash) {
    print "$key => $value \n";
}