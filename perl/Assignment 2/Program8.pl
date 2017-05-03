#!/usr/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 2
# Date: 4/17/17
use strict;
use warnings;
use File::ReadBackwards;
 
my $fh = File::ReadBackwards->new('forwards.txt') or
die "can't read file: $!\n";

open(FILEWRITE, ">backwards.txt");
 
while ( defined(my $line = $fh->readline) )
{
  print FILEWRITE $line ;
}