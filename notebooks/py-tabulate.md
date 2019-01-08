Run a Jupyter Notebook server via the docker container, mounting the code directory that resides outside the container.


jupyter/datascience-notebook:latest worked, there might be a smaller one available that also works.


```
$ docker run -p 8888:8888 -v /path/to/notebooks/folder:/home/jovyan/notebooks jupyter/datascience-notebook
```

Then visit http://localhost:8888 and supply the generated token.



Will probably need to install dependencies to run some codes.


One way is to start a bash shell running inside the container, then issueing pip commands:

```
$ docker exec -it <container_id or name> bash
```

