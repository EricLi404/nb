username="yvyang.li"
boxip="j.ushow.media"
sourcedir="/Users/eric/work/sm/cv-lib"

rsync -t -a -v -z --exclude=".idea" --exclude=".git" --exclude="tests" --exclude="*.hdf5" --exclude="runtime/*" ${sourcedir} -e "ssh -p 5822" ${username}@${boxip}:/home/yvyang.li

echo 'j2sl'
ssh jqcloud '/home/yvyang.li/.rsync/tocvw1-3.sh';
echo 'done';
