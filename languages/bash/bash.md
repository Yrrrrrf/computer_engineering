# [Bash](https://www.gnu.org/software/bash/)

Bash is a command language interpreter that executes commands read from the standard input or from a file. Bash also incorporates useful features from the Korn and C shells (ksh and csh).

## [Bash Scripting](https://www.gnu.org/software/bash/manual/html_node/index.html)

Bash is a Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell. First released in 1989, it has been used widely as the default login shell for most Linux distributions.

Bash is a command language interpreter that executes commands read from the standard input or from a file. Bash also incorporates useful features from the Korn and C shells (ksh and csh).

## Usage
```bash
pwd  # Print the current directory

ls  # List the files in the current directory
ls -l  # List the files in the current directory with more details
ls -a  # List the files in the current directory including hidden files
ls -la  # List the files in the current directory with more details including hidden files

cd  # Change directory
cd ..  # Change directory to the parent directory
cd ~  # Change directory to the home directory
cd /  # Change directory to the root directory
cd -  # Change directory to the previous directory

mkdir  # Create a new directory
mkdir -p  # Create a new directory and all the parent directories if they don't exist
touch  # Create a new file

rm  # Remove a file
rm -r  # Remove a directory
rm -rf  # Remove a directory and all its contents

cp  # Copy a file
cp -r  # Copy a directory
mv  # Move a file
mv -r  # Move a directory

cat  # Print the contents of a file
cat >  # Create a new file and write to it
cat >>  # Append to a file

echo  # Print a string
echo -n  # Print a string without a newline
echo -e  # Print a string with escape characters
echo -e "\033[0;31m"  # Print a string with escape characters
```


