Using Commands =>
(1) condo info:- 
for getting condo information.

(2) conda env list: 
We can make different virtual enviroments using condo in also VS Code. For get to know all enviroment list in conda till now,
use command.

(3) condo create --name py310 python=3.10 
=> For creating virtual env. (here we installed 3.10 vesion of python, and 'py310' is just a name we can use any name.)

(4) condo activate py310 :
For Activate virtual enviroment of condo.

(5) condo install seaborn :
Now, for installing any library, seaborn is a library name.

(6) conda deactivate: 
For deactivate conda enviroment, use this command.

(7) conda activate: 
Now, for starting conda from starting.

(8) conda config --set auto_activate_base false :
By default 'condo' base enviroment always open. Even you opens terminal everytime. To prevent this,you have to use this command.

Important =>
(i) We shouldn't use 'pip' and 'conda' together. If we used then it's creates so many problems.
(ii) For working on 'fastAPI' or 'Django', you should use simple enviroment as 'pip'. And for Data science field or to explore something new then you should use Conda.

