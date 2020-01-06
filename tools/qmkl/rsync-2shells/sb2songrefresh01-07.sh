username="yvyang.li"
boxip="j.ushow.media"
sourcedir="/Users/EricLi/www/sm/sm-song-book"

rsync -t -a -v -z --exclude=".idea" --exclude=".git" --exclude="tests" --exclude="runtime/*" ${sourcedir} -e "ssh -p 5822" ${username}@${boxip}:/home/yvyang.li

echo 'j2toworker'
ssh jqcloud '/home/yvyang.li/.rsync/toworker1.sh';
ssh jqcloud '/home/yvyang.li/.rsync/toworker2.sh';
ssh jqcloud '/home/yvyang.li/.rsync/toworker3.sh';
ssh jqcloud '/home/yvyang.li/.rsync/toworker4.sh';
ssh jqcloud '/home/yvyang.li/.rsync/toworker5.sh';
ssh jqcloud '/home/yvyang.li/.rsync/toworker6.sh';
ssh jqcloud '/home/yvyang.li/.rsync/toworker7.sh';

echo 'done';
