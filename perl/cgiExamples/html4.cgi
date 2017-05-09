#!/usr/bin/perl

# An interactive portal that compiles a shopping list
# based on user input.
use warnings;
use strict;
use CGI qw( :standard );

redirect( "html4html.cgi" )
	unless ( param( "CD" ) || param( "book" )
			|| param( "airplane" ) );

my $total;

print( header(), start_html( "Purchase" ) );

if ( my $CDs = param( "CD" ) ) {
	print( "You have bought $CDs CDs for \$", $CDs * 12 );
	print( ".", br() );
	$total += $CDs * 12;
}

if ( my $books = param( "book" ) ) {
	print( "You have bought $books books for \$",$books * 19.99, ".", br() );
	$total += $books * 19.99;
	}


if ( my $airplanes = param( "airplane" ) ) {
	print( "You have bought $airplanes airplanes for \$",
	$airplanes * 1000000, ".", br() );
	$total += $airplanes * 1000000;
}

print( "Your total purchase comes to \$$total.\n" );
print( end_html() );