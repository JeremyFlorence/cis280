#!/usr/bin/perl
# A soothsayer program.

use warnings;
use strict;
use CGI qw( :standard );

print( header(), start_html( "Soothsayer Program" ) );

	if ( param ) {
	 	my @array = ( "Signs point to yes", "No", "Yes",
					"Ask later", "Perhaps not", "Could be",
					"No chance", "Never!!!!" );

		print( h1( $array[ rand( 8 ) ] ) );
	}
	else {
		print( h1( "Soothsayer" ), br(),
				p( "Enter your question here: " ), start_form(),
				textfield( -name => "question" ), submit(),
				end_form() );
	}

print( end_html() );