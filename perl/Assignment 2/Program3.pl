#!/usr/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 2
# Date: 4/17/17
use strict;
use warnings;

theSub('a', 'b', 'c');

sub theSub {
    my $numParams = @_;
    print "Number of parameters: $numParams\n";
}