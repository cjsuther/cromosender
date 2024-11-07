rsync -av -e "ssh" --exclude='front/node_modules' --exclude='.git' --exclude='error.log' --exclude='__pycache__' --exclude='env' . bot@200.41.170.123:/var/www/studies
