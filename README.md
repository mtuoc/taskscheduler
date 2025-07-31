# taskscheduler
A simple script to schedule task to be processed sequentally (useful when sharing GPUs)

The tasks can be added in a text file while running the program.

The script reads a file taskQueue.txt that should contain one script to run in each line (use full path to scipt): For example:

```
/home/user/task1directory/task1.sh
/home/user/taskndirectory/taskn.sh
...
/home/user/taskn1directory/taskn.sh
```

Remember that the scritps to run should start with the following line to use the paths relatives to the script:

```
#! /bin/bash
cd $(dirname $0)
```

A typical situation would be control training of NMT system using Marian. Each training script should look like the following:

```
#! /bin/bash
cd $(dirname $0)

./marian -c config.yaml
```

Once the process has started, the user can add new tasks adding a line in the proces.txt file.

It is also possible to move the processes in the list to give them more or less priority.
