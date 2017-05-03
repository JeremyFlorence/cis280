#!/usr/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 2
# Date: 4/17/17
use strict;
use warnings;

print "Calculating the max of the set {23, 12, 3, 58, 100, 34}...\n";
my $imax = iterativeMax(23, 12, 3, 58, 100, 34);
print "Max with iteration = $imax \n";
my $rmax = recursiveMax(23, 12, 3, 58, 100, 34);
print "Max with recursion = $rmax \n";


sub iterativeMax {
    my @values = @_;
    my $max = $values[0];
    foreach my $val (@values) {
        if ($val > $max) {
            $max = $val;
        }
    }
    return $max;
}

sub recursiveMax {
    my @values = @_;
    
    # if the length of the array is 1
    if(@values == 1) {
        return shift(@values);
    } else {
        my $first = shift(@values);
        my $max = recursiveMax(@values);
        return($first > $max)? $first : $max;
    }
}