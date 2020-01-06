username="yvyang.li"
boxip="j.ushow.media"
sourcedir="/Users/eric/work/sm/sm-song-book"

rsync -t -a -v -z --exclude=".idea" --exclude=".git" --exclude="tests" --exclude="runtime/*" ${sourcedir} -e "ssh -p 5822" ${username}@${boxip}:/home/yvyang.li

echo 'j2sl'
ssh jqcloud '/home/yvyang.li/.rsync/tosl.sh';
echo 'done';
