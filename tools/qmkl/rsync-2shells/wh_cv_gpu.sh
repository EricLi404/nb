username="yvyang.li"
boxip="j.ushow.media"
sourcedir="/Users/eric/work/sm/wheel"

rsync -t -a -v -z --exclude=".idea" --exclude="no_rc" --exclude=".git" --exclude=".DS_Store" --exclude="MNIST_data" --exclude="cmake*" --exclude="*.hdf5"  --exclude="*.h5"  --exclude="__pycache__" --exclude=".ipynb_checkpoints" --exclude="*.m"   --exclude="tests" --exclude="runtime/*" ${sourcedir} -e "ssh -p 5822" ${username}@${boxip}:/home/yvyang.li

echo 'j2gpu_cv'
ssh jqcloud '/home/yvyang.li/.rsync/towh_gpu_cv.sh';
echo 'done';
