username="yvyang.li"
boxip="j.ushow.media"
sourcedir="/Users/eric/work/sm/devops/scripts/airflow/research"

rsync -t -a -v -z --exclude=".idea" --exclude=".git" --exclude="tests" --exclude="runtime/*" ${sourcedir} -e "ssh -p 5822" ${username}@${boxip}:/home/yvyang.li

echo 'j2airflow'
ssh jqcloud '/home/yvyang.li/.rsync/toairflow-rs.sh';
echo 'done';
