# Line Server Problem

## How does this system work?

This system exposes a REST API that return a line given its index inside a given text file. 
The API endpoint `/lines/<line index>` accepts a line index and returns the corresponding line from the text file.
The system will consider all the lines (even blank ones).
The line index starts with 0. This means that the first line of file corresponds to the index 0.

## Building the system

For building the system you simply need to run the following command in your terminal:

`
./run.sh <name_of_text_file>.txt
`

You might need to add sudo to the command.

The text file needs to be located in the root of project. Please take a look at the location of sample_file.txt file.

For making the requests, you can use Swagger and access it through `http://localhost:8000/docs`.

## How will this system perform with a 1 GB file? a 10 GB file? a 100 GB file?

The system is designed to perform well with files of varying sizes, including large files. 
The approach being used does not fit all the file content in memory at once so memory won't be as heavily compromised.

## How will this system perform with 100 users? 10,000 users? 1,000,000 users?

The system is built to support multiple simultaneous clients and should scale well to deal with a large number of users. 
The performance may degrade under heavy load, especially with a high number of concurrent users. 
To handle increased traffic and infrastructure concerns, the system should be deployed into a cloud-based service, and optimizations such as load balancing can be implemented.

## Documentation, websites, papers, etc used for this assignment

In completing this assignment, I consulted the following documentation, websites, and resources:
- Implementing DDD in python: https://www.w3computing.com/articles/implementing-domain-driven-design-in-python-projects/#google_vignette
- Iterating through file lines in python: https://stackoverflow.com/questions/48124206/iterate-through-a-file-lines-in-python
- ChatGPT: It helped writing the skeleton for the readme file and writing the code for the run.sh script

## Third-party libraries or other tools used by the system

The system uses the following third-party libraries and tools:
- FastAPI: chosen for its high performance, asynchronous capabilities, and easy-to-use API declaration syntax.
- uvicorn: ASGI server implementation chosen for its compatibility with FastAPI and performance.

These libraries and tools were chosen based on their popularity, community support, performance, and suitability for building REST APIs in Python.


## Time spent and system solution critique

I've spent about 3h in this exercise.
Some of the time was used deciding about the file line reading approach and whether blank lines should be consider and line indexes preserved.

If I would spend more time I would do the following:
- Add unit tests. I know I could use TDD approach here but I'm not yet still 100% confortable with it so I didn't want to take much time on it for this specific situation.
- Add api tests. Add a test that explicitly makes a request to the `/lines/<line index>` endpoint to see if it behaves as expected
- Take a better look at the project structure. I aimed to use a DDD approach but it has not quite the "ideal" design for it.
I would for example assess if an entity folder could be created inside the domain layer to hold the line entity structure.
- I would try to improve my approach for reading the lines of the file. I decided to go not for the memory-heavy approach 
because of the larger files but having a loop can affect the performance.

