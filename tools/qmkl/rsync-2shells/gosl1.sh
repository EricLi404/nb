username="yvyang.li"
boxip="j.ushow.media"
sourcedir="/Users/eric/work/sm/sm-songbook-go"

rsync -t -a -v -z --exclude=".idea" --exclude=".git" --exclude="tests" --exclude="runtime/*" ${sourcedir} -e "ssh -p 5822" ${username}@${boxip}:/home/yvyang.li

echo 'j2sl2'
ssh jqcloud '/home/yvyang.li/.rsync/togosl1.sh';
echo 'done';
