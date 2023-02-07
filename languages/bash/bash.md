# [Bash](https://www.gnu.org/software/bash/)

Bash is a Unix shell and command [[programming language|language]] [[interpreter]] that executes commands read from the standard input or from a file. 

## Usage
```bash
pwd  # Print Working Directory
ls  # list    -l details    -a hidden files   -la all
cd  # change dir    .. parent dir    ~ home dir    / root dir    - previous dir

# file management
mkdir  # make dir    -p create parent dirs
touch  # create file
mv  # move a file    -r recursive
rm  # remove file or dir    -f force    -i interactive    -r recursive
cp  # copy file    -r recursive

# file content
cat  # print file content    > redirect output    >> append output    -n line numbers    -s squeeze empty lines
head  # print first lines    -n number of lines
tail  # print last lines    -n number of lines

# file permissions
chmod  # change mode    -R recursive    -v verbose    -c changes only    -f silent    -u update
chown  # change owner    -R recursive    -v verbose    -c changes only    -f silent    -u update
chgrp  # change group    -R recursive    -v verbose    -c changes only    -f silent    -u update
```

----
## References
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)
