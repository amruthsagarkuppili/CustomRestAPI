

Follow the execution steps as listed 
Open the command prompt from any folder and proceed to below steps
1) mkdir restapi

2) cd restapi

3) python3 -m venv apicode (creating python virtual environment with name apicode).

4) . apicode/bin/activate

5) Pip install flask

7) copy & paste the wsgi.py file in the current directory, that is, in repustate directory. (wsgi.py file will be found in extracted files)

8) copy & paste the entire jsonapi folder in the folder where wsgi.py is present. (In other words, it should be in repustate folder)

9) export  FLASK_APP=wsgi.

10) flask run. (Running the server. Server automatically starts on http://127.0.0.1:5000)

11) To run the testclass, execute "Python TestCall.py" on command prompt.


versions used:
==================
Python : 3.8.0
Flask : 1.1.2
pip :   19.2.3


Tasks Performed:
===================
1. Fetched response from the url, merged them and deleted the duplicates (This process is performed in sendrequest.py). Also, designed a parallel processing
request hit method to parallely hit the requests for multiple tag values. This is addressed using multi-threading
2. Handled all the edge cases like checking for tag parameter, validating sortBy and direction parameter in routes.py file
3. Test class is written to check the correctness of the code in TestCall.py file.
4. To avoid redundant hits to the server, an efficient approach, Session cookies are used to store the fetched data on client location. Whenever a repeated
url is hit, it looks for that combination in session and straight aways brings the result instead of hotting the server.
5. Session cookies are encrypted, so there is no way to interpret the data stored on the browser.