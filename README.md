# Water Diversion Measurement and Reporting
This repository contains scripts analyze, modify, and report water diversion data to comply with California SB88 (https://www.waterboards.ca.gov/waterrights/water_issues/programs/measurement_regulation/).  The code puts the data in the CUASHI format (https://www.cuahsi.org/data-models/publication/) for standardized reporting and sharing.
 
# Getting started

For use on windows machines, use the miniconda package manager.

## 1. Download and install Conda

Download Miniconda from https://conda.io/miniconda.html. Make sure to install the Python3 and 64-bit version. Installation instructions for windows is here https://conda.io/docs/user-guide/install/windows.html

After it is installed, click on the start menu on the lower left of the screen to see all programs installed.  You should see a "Anaconda3 (64 bit)" folder and inside that folder should be a program called "Anaconda Prompt".  Start that program.  A new code window will open up.  You can check the installation by typing ```conda --version```. It is also adviceable to run ```conda update conda``` before you start.

## 2. Downlaod and install Git 

Test whether Git is installed on your system by typing in the same Anaconda Prompt window:

```
git --version
```

If no version number is returned, install Git from https://git-scm.com/.

## 3. Create a project directory named ```diversion```

We need a directory where the project will live. On a windows machine, I have a folder located at "C:\ArcScratch" to hold my working files. You may use another directory like "C:\Users\USERNAME\Documents\workspace" where USERNAME is your user name for your computer.  I find working in that directory difficult because it changes for each user.  Either way, pick a location to store your files for this project.  Some of the files are quite large so make sure you have a several GB of free space.  I will refer to this location as PATH.  In the "Anaconda Prompt" window, navigate to this location by using the "cd" notation for "change directory".  Type in "cd" a space, and your PATH name.  For me it is 

```
cd C:\Users\kklausmeyer\Documents\workspace
```

For you it may be different.  Now the prompt should read "(base) PATH>" where PATH is your path.  

In order to create a new directory ```diversion```

```
mkdir diversion
```

mkdir stands for make directory.  Now navigate to that directory by using the cd notation.

```
cd diversion
```

Now the prompt should read "(base) PATH\diversion>" where PATH is your path.

## 4. Git clone or pull the project

From within the ```diversion``` directory run:

```
git clone https://github.com/tnc-ca-geo/diversion.git
```

This will create a new folder or directory with the same name "diversion" inside the "diversion" folder.  Moving forward, we will refer to the two folders as the outer flow-update directory and the inner flow-update directory.

If an (inner) diversion directory already exists within the (outer) diversion directory, you will get an error message. In this case change using into the (inner) ```diversion``` directory (```cd diversion```) and run

```
git pull origin master
```

**Repeat this whenever you start working with the project to get the latest version**.


## 5. Create a conda environment using the conda_environment.yml file

It should (hopefully) be very easy to create the environment from the ```conda_environment.yml``` file in the repository. Change into the (inner) diversion directory, make sure ```conda_environments.yml``` is there (use the ```dir``` command) and run.

```
conda env create --file conda_environment.yml
```

This will take awhile and download a bunch of dependencies, eventually it should exit wthout an error message.

If you want to learn how to create an environment manually and how to add depencies to that environment see https://conda.io/docs/.

Please keep the ```conda_environment.yml``` and ```requirements.txt``` files up to date if you introduce new dependencies into the project. As the project evolves other programmers might introduce new dependencies as well. You should update the environment after pulling a newer version of the project from Github

```
conda env update --file conda_environment.yml

```

## 5. Activate the environment

Type 

```
conda activate diversion
```

into a ```cmd``` shell in order to activate the environment.

**Note**: You need to do this whenever you open a new ```cmd``` shell. Environment activations are bound to the shell. Different shells may have different environments activated. If you use any integrated development environment such as IDLE, there are project-level settings that determine which environment will be used if you press the play button.

## 6. Activate the Jupyter kernal

This project uses Jupyter notebooks to review output in real time.  When you set up the environment, you need to create a new kernel associated with the environment.  This command will do that:

```
python -m ipykernel install --user --name diversion --display-name "Python (diversion)"
```

# Updating the Code

When returning to the project to update the code, folow these steps:
1. Launch the "Anaconda Prompt" from your start menu (on a windows machine)
2. Use the cd notation to navigate to the inner directory of your working folder
```
cd PATH\diversion\diversion
```
or
```
cd C:\Users\kklausmeyer\Documents\workspace\diversion\diversion
```
3. (optional) Update the environment:
```
conda env update --file conda_environment.yml
```
4. Activate the environment
```
conda activate diversion
```
5. Get the latest version of the code from GitHub
```
git pull origin master
```
6. Start Jupyter notebook
```
jupyter notebook
```



Here is a nice summary of the basic git commands to sync changes to the master repo
https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html
