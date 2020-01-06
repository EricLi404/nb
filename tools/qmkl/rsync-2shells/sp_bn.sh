username="yvyang.li"
boxip="j.ushow.media"
sourcedir="/Users/eric/work/sm/spider"

rsync -tavz --exclude="*.pyc" --exclude=".idea" --exclude=".git" --exclude="build" --exclude="project.egg-info" --exclude="venv" --exclude="setup.py" --exclude=".arcconfig" --exclude=".gitignore" --exclude="twistd.pid" --exclude="fabfile.py" --exclude="music/settings/__init__.py" ${sourcedir} -e "ssh -p 5822" ${username}@${boxip}:/home/yvyang.li

echo 'j2sl'
ssh jqcloud '/home/yvyang.li/.rsync/tosp_bn.sh';
echo 'done';

