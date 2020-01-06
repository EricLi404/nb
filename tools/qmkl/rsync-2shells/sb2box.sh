username="liyvyang"
boxip="liyvyang.box.ushow.media"
sourcedir="/Users/eric/work/sm/sm-song-book"

rsync -t -a -v -z '-e ssh -p 5822' --exclude=".idea" --exclude=".git" --exclude="tests" --exclude="runtime/*" ${sourcedir} ${username}@${boxip}:/home/liyvyang

echo 'done';
