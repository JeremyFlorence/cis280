#!/usr/local/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 1
# Date: 4/2/17

@numbers = (23, 12, 56, 45, 34, 90, 78, 89, 67);

$sum;

foreach $n (@numbers) {
    $sum += $n;
}

print "The size of the array is: " . ($#numbers+1) . "\n";
print "The sum of the elements is: " . $sum . "\n";
print "The average of the elements is: " . ($sum/($#numbers+1)) . "\n";
@sorted = sort @numbers;
print "The first largest element in the array is: " . $sorted[($#sorted)] . "\n";
print "The second largest element in the array is: " . $sorted[($#sorted-1)] . "\n";
print "The third largest element in the array is: " . $sorted[($#sorted-2)] . "\n";
print "The fourth largest element in the array is: " . $sorted[($#sorted-3)] . "\n";
print "The fifth largest element in the array is: " . $sorted[($#sorted-4)] . "\n";

