#!/usr/local/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 1
# Date: 4/2/17

print "Please enter in two integers\n";
print "Integer a = ";
$a = <STDIN>;
chomp $a;
print "Integer b = ";
$b = <STDIN>;
chomp $b;

if ($a % $b == 0) {
    print "Integer a is a multiple of integer b.\n";
} elsif ($b % $a == 0) {
    print "Integer b is a multiple of integer a.\n";
} else {
    print "Neither integer is a multiple of the other.\n";
}