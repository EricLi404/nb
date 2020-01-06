# e.g.
# ./rs.sh sg f01
# ./rs.sh sb box
# ./rs.sh cl cw5


repo_s=$1
host=$2


if [[ ${repo_s} == "sg" ]]; then
  repo="sm-songbook-go"
elif [[ ${repo_s} == "sb" ]]; then
  repo="sm-song-book"
elif [[ ${repo_s} == "cl" ]]; then
  repo="cv-lib"
elif [[ ${repo_s} == "bn" ]]; then
  repo="starmaker-backend"
else
  echo "param repo_s error $1"
fi

if [[ ${host} == "box" ]]; then
  rsync -t -a -v -z --exclude=".idea" --exclude=".git" --exclude="vendor" --exclude="tests" --exclude="runtime/*" /Users/eric/work/sm/${repo} -e "ssh -p 5822" liyvyang@liyvyang.box.ushow.media:/home/liyvyang
else
  rsync -t -a -v -z --exclude=".idea" --exclude=".git" --exclude="vendor" --exclude="tests" --exclude="runtime/*" /Users/eric/work/sm/${repo} -e "ssh -p 5822" yvyang.li@j.ushow.media:/home/yvyang.li
  ssh jqcloud "rsync -t -a -v -z --exclude='.idea' --exclude='vendor' --exclude='.git' --exclude='tests' --exclude='runtime/*' /home/yvyang.li/${repo} -e 'ssh -p 5822' ${host}:/home/worker/yvyang.li"
fi