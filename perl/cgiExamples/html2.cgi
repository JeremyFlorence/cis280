#!/usr/bin/perl
# Ex. 7.7: Ex07_07.pl
# Using CGI.pm to determine the properties of a triangle.

use warnings;
use strict;
use CGI qw( :standard );

print( header() );
print( start_html( "Triangles" ) );

my $hypotenuse = param( "Hypotenuse" );
my $shorter = param( "Short" );
my $longer = param( "Long" );

	if ( $hypotenuse && $shorter && $longer ) {

		if ( $hypotenuse < $shorter || $hypotenuse < $longer || $longer < $shorter ) {

			print( "Please re-enter the three sides ", "in the correct places: " );
			ourform();
 		}
		elsif ( $hypotenuse >= $shorter + $longer ) {
			print( "Those three sides do not make a triangle, ", "please reenter: " );
 			ourform();
		}
 		else {
 			print( "The triangle with the sides $hypotenuse, ","$shorter, and $longer is " );

 				if ( $hypotenuse == $shorter && $hypotenuse == $longer ) {
 					print( "an equilateral triangle." );
 				}
				else {

					if ( $hypotenuse == $longer || $shorter == $longer ) {
						print( "an isocolese " );

						if ( $hypotenuse ** 2 == $longer ** 2 + $shorter ** 2 ) {
							print( "and a right triangle." );
						}
 						else {
 							print( "triangle." );
						}
					 }
					elsif ( $hypotenuse ** 2 == $longer ** 2 + $shorter ** 2 ) {
						print( "a right triangle." );
					}
					else {
						print( "not special." );
					}
				}
			}	
		}
 		else {
			print( "Please enter the three sides of a triangle:\n" );
			ourform();
		}

print( end_html() );

sub ourform {
	print( start_form(),"Hypotenuse ", textfield( -name => "Hypotenuse" ),
			br(), "Longer side ", textfield( -name => "Long" ),
			br(), "Shorter side ", textfield( -name => "Short" ),
			br(), submit( "Submit" ),
			end_form() );
}