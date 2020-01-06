username="yvyang.li"
boxip="j.ushow.media"
sourcedir="/Users/EricLi/www/sm/sm-song-book"

rsync -t -a -v -z --exclude=".idea" --exclude=".git" --exclude="tests" --exclude="runtime/*" ${sourcedir} -e "ssh -p 5822" ${username}@${boxip}:/home/yvyang.li

echo 'to f-ids'
ssh jqcloud '/home/yvyang.li/ansible/f-ids-rs.yml.sh';

echo 'done';
