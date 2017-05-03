#!/usr/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 2
# Date: 4/17/17
use strict;
use warnings;

print "Please enter a non-negative integer: ";
my $num = <STDIN>;
chomp $num;

my $num_factorial = 1;

if ($num < 0) {
    print "ERROR: You must enter a non-negative number.\n";
    exit;
} elsif ($num == 0) {
    $num_factorial = 1;
} else {
    foreach my $i (1 .. $num) {
        $num_factorial *= $i;
    }
}
print "\n";
print "$num! = $num_factorial\n";