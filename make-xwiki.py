#####################
## IMPORTS
#####################
import os
import os.path
import shutil
import zipfile
import sys
import xml.etree.ElementTree as ET
#####################
## GLOBALS
#####################
home = os.path.expanduser("~")
cmd = "mvn clean install -Pdistribution -pl xwiki-platform-distribution/xwiki-platform-distribution-flavor/xwiki-platform-distribution-flavor-jetty-hsqldb"
xe_sources = home + "/xwiki/platform"
xe_target = xe_sources+ "/xwiki-platform-distribution/xwiki-platform-distribution-flavor/xwiki-platform-distribution-flavor-jetty-hsqldb/target"
instance_path = home + "/xwiki/instance"
#####################
## PRINT LOG SECTION
#####################
def log_section(title):
  nb = 120
  color = '\033[95m'
  normal_color = '\033[0m'
  print color + "-" * nb
  print title
  print "-" * nb + normal_color
#####################
## BUILD
#####################
def build():
  global cmd
  for arg in sys.argv:
    if arg == "-U":
      cmd = cmd + " -U"
    elif arg == "-am":
      cmd = cmd + " -am"
    elif arg == "nobuild":
      log_section("1. NO BUILD")
      return
  log_section("1. Build XWiki (" + cmd + ")")
  current_path = os.getcwd()
  os.chdir(xe_sources)
  os.system(cmd)
  os.chdir(current_path)
#####################
## CLEAN
#####################
def clean():
  log_section("2. Remove old build (" + instance_path + ")")
  if os.path.exists(instance_path):
    shutil.rmtree(instance_path)
#####################
## DETECT THE VERSION
#####################
def detectVersion():
  tree = ET.parse(xe_sources + "/pom.xml")
  return tree.getroot().find("{http://maven.apache.org/POM/4.0.0}version").text
#####################
## UNZIP
#####################
def unzip():
  version = detectVersion()
  log_section("3. Uncompressing the new build")
  zfile = zipfile.ZipFile(xe_target + "/xwiki-platform-distribution-flavor-jetty-hsqldb-"+version+".zip")
  for name in zfile.namelist():
    (dirname, filename) = os.path.split(name)
    if dirname.startswith("xwiki-platform-distribution-flavor-jetty-hsqldb-" + version):
      dirname = dirname[len("xwiki-platform-distribution-flavor-jetty-hsqldb-" + version)+1:len(dirname)]
    dirname = instance_path + "/" + dirname
    #print "Decompressing " + filename + " on " + dirname
    if not os.path.exists(dirname):
      os.makedirs(dirname)
    if filename <> '':
      ## not a directory
      fd = open(dirname + "/" + filename, 'w')
      fd.write(zfile.read(name))
      fd.close()
  zfile.close()
  os.system("echo " + version + " > " + instance_path + "/VERSION")
  os.system("ln -s " + instance_path + "/webapps/xwiki/WEB-INF/lib/ " + instance_path + "/lib")
#####################
## SCRIPT
#####################
## 1. Build
build()
## 2. Remove old build
clean()
## 3. Uncompressing the new build
unzip()
## 4. End
log_section("Done")
