#!/usr/bin/python

import os, glob
import shutil, errno
import sys

# --------------------------------------------------------------
# Change this to the location of a blank/empty Lightroom catalog
# --------------------------------------------------------------
_LRTEMPLATE = "/Users/mcgraths/Pictures/Workflow/_LRTEMPLATE"
# --------------------------------------------------------------

def copyfolder(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def create_directory(directory):
	if not os.path.exists(os.getcwd() + "/" + directory):
		os.makedirs(os.getcwd() + "/" + directory)
		print "Folder created: " + directory 
		
def rename(dir, pattern, find, replace):
	#print os.path.join(dir, pattern)
	for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
		title, ext = os.path.splitext(os.path.basename(pathAndFilename))
		os.rename(pathAndFilename, os.path.join(dir, title.replace(find, replace) + ext))
		#print pathAndFilename
		#print title.replace(find, replace) + ext

def init():
	create_directory('Throwaways')
	create_directory('USB')

	folder = os.path.basename(os.getcwd())
	dest = os.getcwd() + "/" + folder + " Catalog"


	#copy Lightroom catalog template
	if not os.path.exists(dest):
		copyfolder(_LRTEMPLATE, dest)
		rename(dest, "_LRTEMPLATE*", "_LRTEMPLATE", folder)
		print "Lightroom catalog created"
	
	print "[Session Initialized]"


def init_wedding():
	create_directory('Throwaways')
	create_directory('USB')
	create_directory('Book')
	create_directory('Prints')
	

	folder = os.path.basename(os.getcwd())
	dest = os.getcwd() + "/" + folder + " Catalog"


	#copy Lightroom catalog template
	if not os.path.exists(dest):
		copyfolder("/Users/mcgraths/Pictures/Workflow/_LRTEMPLATE", dest)
		rename(dest, "_LRTEMPLATE*", "_LRTEMPLATE", folder)
		print "Lightroom catalog created"
	
	print "[Wedding Initialized]"
	
if len(sys.argv) < 2:
	print "ERROR: Please supply at least two arguments"
	print "Available commands:"
	print "- init"
	print "- init wedding"

elif len(sys.argv) == 2:
	init()
else:
	init_wedding()
	