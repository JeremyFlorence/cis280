#!/usr/bin/perl
#<!-- An interactive portal that compiles a shopping list -->
#<!-- based on user input. -->

print("<html><head><title>Buy Something</title></head>");

print("<body>");
print("<h1>Clearance!</h1>");
print("<p>Please enter how many of each product you wolld like to
	order into the box in the right-hand column.</p>");

 print("<form method = \"POST\" action = \"http://localhost/cgi-bin/html4.cgi\">");

print("<table width = \"100%\"\" border = \"3\">");
	print("<tr>");
		print("<th>Product Name</th>");
		print("<th>Description</th>");
		print("<th>Price</th>");
		print("<th>Order</th>");
	print("</tr>");
	print("<tr>");
		print("<td>CD</td>");
 		print("<td>Buy this really cool CD</td>");
 		print("<td>$12.00</td>");
		print("<td><input type = \"text\" name = \"CD\" size = \"5\"></td>");
 	print("</tr>");
	print("<tr>");
		print("<td>Book</td>");
 		print("<td>Buy this really cool book</td>");
 		print("<td>$19.99</td>");
 		print("<td><input type = \"text\" name = \"book\" size = \"5\"></td>");
 	print("</tr>");
 	print("<tr>");
 		print("<td>Airplane</td>");
		print("<td>Buy this really cool airplane</td>");
		print("<td>$1,000,000</td>");
		print("<td><input type = \"text\" name = \"airplane\" size = \"5\"></td>");
	 print("</tr>");

print("</table>");
print("<input type = \"submit\" value = \"submit\">");
print("</form>");

print("</body></html>");