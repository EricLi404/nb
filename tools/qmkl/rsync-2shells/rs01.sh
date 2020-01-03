username="yvyang.li"
boxip="j.ushow.media"
sourcedir="/Users/eric/www/sm/starmaker-research"

rsync -t -a -v -z --exclude=".idea" --exclude=".git" --exclude="tests" --exclude="runtime/*" ${sourcedir} -e "ssh -p 5822" ${username}@${boxip}:/home/yvyang.li

echo 'j2rs'
ssh jqcloud '/home/yvyang.li/.rsync/tors-worker01.sh';
echo 'done';
