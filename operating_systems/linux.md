# [GNU Linux](https://en.wikipedia.org/wiki/Linux)

is a family of open-source [[unix-like|Unix-like]] [[operating system|operating systems]] based on the **Linux kernel**, an operating system kernel first released on September 17, 1991, by Linus Torvalds. Linux is typically packaged as a Linux distribution, which includes the kernel and supporting system software and libraries, many of which are provided by the GNU Project. Many Linux distributions use the word "Linux" in their name, but the Free Software Foundation uses the name $GNU/Linux$ to emphasize the importance of GNU software, causing some controversy.

## Linux Kernel

The Linux kernel is an **open-source operating system** released under the terms of the GNU General Public License version 2 (GPLv2) and is the main component of a Linux distribution. Linux is typically packaged in a Linux distribution. Linux distributions include the Linux kernel and supporting system software and libraries, many of which are provided by the GNU Project. Many Linux distributions use the word "Linux" in their name, but the Free Software Foundation uses the name "GNU/Linux" to emphasize the importance of GNU software, causing some controversy.

## [File System Hierarchy Standard (FHS)](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
Is a **standard for the organization of files on [[unix-like|Unix-like]] operating systems**. It **defines the directory structure and the contents of each directory**.

```bash
root/  # the home directory for your root or system administrator
├───bin/  # binary or executable files essential for the operating system to run
├───boot/  # boot loader and kernel activation files
├───proc/  # it's not necessarily part of the file system, but a virtual file system that provides access to kernel or system information 
├───dev/  # file pointers for character and block devices
├───lib/  # library files that are necessary for all programs to work
├───sbin/  # bin/ for root user
├───tmp/  # temporary files
├───etc/  # system configuration files and scripts
├───var/  # contains most of the frequently changing files (log and cache file and record locks)
│   ├───log/
│   └───bin/
├───usr/  # This is the largest directory on a Linux system. Programs, documentation and the kernel source code (pretty much everything that does not belong in the other directories)
│   ├───bin/  # non essential to OS
│   ├───local/  # local programs
│   │    └───bin/  # local program binaries
├───home/  # user profiles, desktops and user files
│   └───yrrrrrf/  # user profile
```

- `bin/` contains the binary or executable files that launch applications, all users have access to these applications. These represent the bare minimum set of programs required for a user to use the system.
- `boot/` contains the files necessary to boot up your computer including the boot loader and kernel activation files.
- `dev/` contains the file pointers for character and block devices, which means the pointers to hard drives, flash drives, multimedia cards, external devices and system ports.
- `etc/` contains the system configuration files and scripts.
- `home/` contains the user profiles, desktops and user files, it functionality is similar to the “Documents and Settings” directory in MS-Windows.
- `lib/` contains library files that are necessary for all programs to work.
- `media/` is used by hal, the Linux auto-mounter, to load external devices for navigation such as floppy disks, cd-roms, dvd-roms, flash drives, etc…
- `mnt/` is used to load external devices on system that do not use hal.
- `opt/` contains optional software packages. Usually the contents of X11 and your window manger and loaded into opt, but you can add whatever programs you wish to this directory.
- `proc/` is unique because it is not necessarily part of the file system, but a virtual file system that provides access to kernel or system information.
- `root/` the home directory for your root or system administrator. It is kept separate from the other users in case the partition that home is mounted on fails.
- `sbin/` has a functionality similar to bin, which means it contains application executables, but rather than allowing all users access to these programs it restricts access only to the root or administrator.
- `tmp/` the temporary storage location. All users have read and write rights to the contents of this directory.
- `usr/` the largest directory on a Linux system. Pretty much everything that does not belong in the other directories is placed here. The contents usually includes program, documentation and the kernel source code.
- `var/` contains most of the frequently changing files such as logging files, cache file and record locks


## Distributions (distros)
Is an operating system made from a software collection. It is based on the Linux kernel and, often, a package management system. Most distributions include at least the basic graphical user interface and some form of **window manager**.
- [ubuntu](https://ubuntu.com/) is the most popular Linux distribution for desktop (based on Debian).
- [debian](https://www.debian.org/) is the most popular Linux distribution for servers (based on GNU).
- [arch](https://www.archlinux.org/) is a **lightweight and flexible** Linux distribution that tries to Keep It Simple.
- [arco](arcolinux.md) is built on top of [arch](https://www.archlinux.org/) and is a **complete Linux distribution**.

## Window Managers
Is a system program that controls the placement and appearance of windows within a windowing system in a graphical user interface. It is a system which manages the windows, icons, menus, and other visual components of the desktop.

A **desktop environment** (DE) is a collection of software that provides a graphical user interface (GUI) for [[unix-like|Unix-like]] operating systems. It is a system which manages the windows, icons, menus, and other visual components of the desktop. The desktop environment is the primary user interface for most Linux distributions.

----
## Resources
- [directory structure](https://www.youtube.com/watch?v=HbgzrKJvDRw)
- [Linux File Structure](https://www.linux.com/training-tutorials/linux-file-structure/)
- [File System Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
