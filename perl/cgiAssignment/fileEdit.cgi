#!/usr/bin/perl

use warnings;
use strict;
use CGI qw( :standard );

print( header() );
print( start_html( "File Editor" ) );

my $filename = param( "File Name");

if (param) {
    if (-e $filename) {
        print "Edit your file: ";
        fileEditForm();
    } else {
        print "No file with that name exists. Please enter the name of an existing file. You entered: $filename.";
        fileNameForm();
    }

} else {
    fileNameForm();
}



sub fileNameForm {
	print( start_form(),"File Name: ", textfield( -name => "File Name" ),
			br(), submit( "Edit" ),
			end_form() );
}

sub fileEditForm {
    print( start_form(), textarea( -name => 'File Edit'), -default => 'Enter your text here...', -rows => 200, -cols => 400,
                        br(),
                        submit( "Save changes" ),
			end_form() );
}

print( end_html() );