username="yvyang.li"
boxip="j.ushow.media"
sourcedir="/Users/eric/www/sm/devops"

rsync -t -a -v -z --exclude=".idea" --exclude=".git" --exclude="tests" --exclude="runtime/*" ${sourcedir} -e "ssh -p 5822" ${username}@${boxip}:/home/yvyang.li

echo 'j2airflow'
ssh jqcloud '/home/yvyang.li/.rsync/toairflow2.sh';
echo 'done';
