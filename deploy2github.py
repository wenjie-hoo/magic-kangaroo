import os
import subprocess
import sys
# usage
# python deploy2github msg

git_msg = r' '.join(sys.argv[1:])
hexo_path = os.getcwd()
# print("current hexo path: %s" % hexo_path)
github_io_path =os.path.abspath(os.path.join(os.getcwd(), ".."))+'/wenjie-hoo.github.io'
# print("github.io path: %s " % github_io_path)

os.chdir(hexo_path)
retval = os.getcwd()
print ("cd %s" % retval)

print('hexo clean')
subprocess.call('hexo clean', shell=True)
print('hexo g')
subprocess.call('hexo g', shell=True)

os.chdir(github_io_path)
retval = os.getcwd()
print ("cd %s" % retval)
print('rm -rf *')
subprocess.call('rm -rf 2022 2023 2024 404 about about archives categories css gallery images js lib tags',shell=True)
print('cp -r ../magic-kangaroo/public/* ./')
subprocess.call(['cp -r ../magic-kangaroo/public/* ./'],shell=True)

print('git pull')
subprocess.call(['git pull'], shell=True)
print('git add .')
subprocess.call(['git add .'], shell=True)
print('git commit -m '+ git_msg)
os.system('git commit -m'+'"'+git_msg+'"')
print('git push')
subprocess.call(['git push'],shell=True)


os.chdir(hexo_path)
retval = os.getcwd()
print ("cd %s" % retval)
print('hexo clean')
subprocess.call('hexo clean', shell=True)

print('done!')