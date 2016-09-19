○ create a table named Books in that database 
○ the table will consist of the following fields: 
■ id (primary key) 
■ title  string that will hold the title of the book 
■ description  string that will hold a string with the book itself 
■ author  will be connected by foreign key to django user model 
○ create a model for the book table 
○ attach that model to a django admin interface 
○ create a CRUD (Create, Read, Update, Delete) rest resource for the table 
you created  - > find how to implement a rest server from django and and 
create a rest server service for your books model (we should be able to 
do a get request to read data, a post request to insert data, an put request 
to update data and a delete request to delete data) 
● Frontend 
○ Write the Frontend with angular 1
○ open screen should display a table with a list of all the books in the 
books database 
■ the table should have 2 columns: id and name 
■ each row is clickable 
■ a click routes you  to a book page 
○ the table page should  also have an insert form to insert  a new book to 
the database 
○ A book page should display the entire details of the book that was 
clicked from the table (id, name, description, author) 
○ the book page should allow editing of a new book and deleting a 
a book 
