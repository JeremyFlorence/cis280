#!/usr/local/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 1
# Date: 4/2/17

print "Please enter your five favorite foods (separated by commas)\n";
$foodstr = <STDIN>;
@foodarray = split(",", $foodstr);

print "@foodarray\n";
print "The first element in the array is: " . @foodarray[0] . "\n";
print "The last element in the array is: " . @foodarray[$#foodarray] . "\n";

@slice = splice @foodarray, 0, 3;
print "@slice\n"