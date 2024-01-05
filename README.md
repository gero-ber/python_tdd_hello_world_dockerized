### Building and running your application

When you're ready, start your application by running:
`docker compose up --build`.

### Install Docker when it throws an error###
It's just a Hello World and a testclass, you probably did not install docker, eh?

###Why is there an empty requirements.txt###
UnitTest is part of the Python Core Module and thereby there's no need to additionally load it over requirements (I think it's not even possible)
However, I left the file + the reference in the dockerfile in case people want to play around. 
