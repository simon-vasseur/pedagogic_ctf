# CTF Pédagogique

Ce repo permettra à ceux qui souhaitent apprendre la sécurité informatique de se lancer facilement.

First things first :

    git clone https://github.com/HugoDelval/ctf_pedagogique

## Configure Bower :

Install nodejs && npm && bower :

    apt-get update && apt-get upgrade
    apt-get install nodejs
If you can't do :

    node -v
Consider doing a :

    ln -s /usr/bin/nodejs /usr/bin/node # (on some distribs you have to do that)
Now you should be able to launch :

    npm -v
If not, please refer to official documentation : https://docs.npmjs.com/getting-started/installing-node .

Pulling the nedeed files will be done by a script when needed. If, one day, you have to do it manually run:
`npm install bower && bower install && bower install [package]`
    
## Installation :
first, be sure that you have go installed :

    sudo apt-get install golang

Then run the script *init.sh* :

    cd ctf_pedagogique
    sudo ./init.sh
    
You are now good to go(lang :p) !

    sudo -u ctf_interne ./run.sh
