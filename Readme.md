# CTF Pédagogique

Ce repo permettra à ceux qui souhaitent apprendre la sécurité informatique de se lancer facilement.

## Installation :
first, be sure that you have go installed :

    sudo apt-get install golang

Then checkout the git repo and run the script *init.sh* :

    git clone https://github.com/HugoDelval/ctf_pedagogique
    cd ctf_pedagogique
    sudo ./init.sh
    
Please consider changing your umask to 0027 for more privacy :
    
    sudo vim /etc/login.defs
Change :

    #     UMASK 022
To :

    #     UMASK 027

Also add this line to **/etc/pam.d/common-session** (if it's not already there) :

    session optional pam_umask.so

You are now good to go(lang :p) !

    sudo ./run.sh

