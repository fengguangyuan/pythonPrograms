#move files to another directory
import os
import shutil
import fetchImgsFromBaidu

def moveFileList(SrcDir, DstDir, ExtFilename=[]):
	fds = os.listdir(SrcDir)
	for file in fds :
		if len(file) > 0 :
			ext = os.path.splitext(file)[-1]
			name = os.path.splitext(file)[0]
			if len(ext) > 0 and ext in ExtFilename :
				moveFile(file, DstDir)
			
	print('move files to '+DstDir+' successfully!')
def moveFile(srcFile, dstDir):
	os.walk(srcFile)
	shutil.copy(srcFile,dstDir)
	os.remove(srcFile)
	print(os.walk(srcFile))
	
moveFileList("b:\\", etchImgsFromBaidu.gPath,['.jpg'])
