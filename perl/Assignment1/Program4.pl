#!/usr/local/bin/perl
# Name: Jeremy Florence
# Course: CIS 280
# Assignment: 1
# Date: 4/2/17


@names = qw(Nick Susan Chet Dolly Bill);
print "Array before changes:\n";
print "@names\n";

@others = qw(Ellie Beatrice Charles);
splice @names, 1, 2, @others;
print "Array after replacing Susan and Chet with Ellit, Beatrice, and Charles:\n";
print "@names\n";

push @names, "Lewis";
push @names, "Izzy";
print "Array after adding Lewis and Izzy to the end:\n";
print "@names\n";

splice @names, 0, 1;
print "Array after removing Nick from the beginning:\n";
print "@names\n";

@names = reverse @names;
print "Array after reversing:\n";
print "@names\n";

splice @names, 0, 0, "Archie";
print "Array after adding Archie to the beginning:\n";
print "@names\n";

@names = sort @names;
print "Array after sorting:\n";
print "@names\n";

splice @names, 3, 2, "Christian", "Daniel";
print "Array after replacing Charles and Dolly with Christian and Daniel:\n";
print "@names\n";