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
jovyan@0c694339d25c:~$ pip install tabulate
Collecting tabulate
  Downloading https://files.pythonhosted.org/packages/12/c2/11d6845db5edf1295bc08b2f488cf5937806586afe42936c3f34c097ebdc/tabulate-0.8.2.tar.gz (45kB)
    100% |████████████████████████████████| 51kB 1.9MB/s
Building wheels for collected packages: tabulate
  Running setup.py bdist_wheel for tabulate ... done
  Stored in directory: /home/jovyan/.cache/pip/wheels/2a/85/33/2f6da85d5f10614cbe5a625eab3b3aebfdf43e7b857f25f829
Successfully built tabulate
Installing collected packages: tabulate
Successfully installed tabulate-0.8.2
jovyan@0c694339d25c:~$ exit
$
```

