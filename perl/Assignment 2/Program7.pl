#!/usr/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 2
# Date: 4/17/17
use strict;
use warnings;

open(FILEREAD, "<data.txt");

open(FILEWRITE, ">output.txt");

while(<FILEREAD>){
  print FILEWRITE ((1 == $. % 3) ? $_ : "");
}

close(FILEREAD);
close(FILEWRITE);