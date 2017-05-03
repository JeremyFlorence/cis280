#!/usr/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 2
# Date: 4/17/17
use strict;
use warnings;

my $PI = 3.14159;





print "Radius = 4\n";
print "Calling subroutine in scalar context...\n";
my $area = calculate(4);
print "Area = $area\n\n";

print "Calling subroutine in list context...\n";
my @dimensions = calculate(4);
print "Dimensions:\n";
print "Area = $dimensions[0] \n";
print "Diameter = $dimensions[1] \n";
print "Circumference = $dimensions[2] \n";

sub calculate {
    if (wantarray) {
        # List context
        my $radius = shift;
        my $area = $PI * $radius * $radius;
        my $diameter = 2 * $radius;
        my $circumference = 2 * $PI * $radius;
        my @dims = ($area, $diameter, $circumference);
        return @dims;
    } elsif (defined wantarray) {
        # Scalar context
        my $radius = shift;
        return $PI * $radius * $radius;
    }
}