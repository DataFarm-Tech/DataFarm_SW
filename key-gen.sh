sudo apt install git ssh
echo "Creating SSH Key"
echo "What is your email?"
read email
ssh-keygen -t ed25519 -C $email
eval "$(ssh-agent -s)"
echo "root password: Yoplait4X\$#"
scp ~/.ssh/id_ed25519.pub root@172.105.191.145:/var/www/html/$USER
echo "Tell admin to create ssh key"
