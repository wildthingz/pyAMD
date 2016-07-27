import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
from gradientGen import *
from MacrosegCont import *
from AMD import *

def main(dims,modes,meshes,(minComp, maxComp)):
	dims=np.array(dims)
	modes=np.array(modes)
	meshes=np.array(meshes)
	for dim in dims:
		for mode in modes:
			name = dim+"-"+mode+".png"
			print("Creating "+name+" ...")
			a=gradientGen((minComp,maxComp),dim,mode)
			im = (a.run()*(-100)+150)
			scipy.misc.toimage(im, cmin=0.0, cmax=255.0).save(name)
			img = ImgMesh(name)
			b=np.array([])
			print("Calculating AMD for "+dim+"-"+mode+" ...")
			contr=0
			for mesh in meshes :
				img.Mesh(mesh)
				#img.plotMesh()
				cont = ContOp(img,[20,100])
				fileID = dim+"-"+mode+str(mesh)+".dat"
				cont.Iterate(fileID)
			
				kernelSize= mesh*1.0
				a=AMD(fileID)
				b=np.append(b,a.getAMD(kernelSize))
				contr+=1.0
				print(str(round(contr*100/len(meshes),2))+" %")
				
			print("Saving results ...")
			minMesh= meshes[b==np.min(b)][0]
			opfileID = dim+"-"+mode+str(minMesh)+".dat"
			a=AMD(opfileID)
			a.plotLinGrad((minComp, maxComp),dim,mode)
			plt.figure()
			plt.plot(meshes,b)
			plt.title(dim+"-"+mode+", with min AMD of: "+str(minMesh))
			plt.savefig(dim+"-"+mode+"-AMD.png")

dims=["2D"]
modes=["I","D","ID","DI"]

#dims=["1D"]
#modes=["I"]
meshes=range(20,120)
(minComp,maxComp)=(0.05,0.15)

main(dims,modes,meshes,(minComp,maxComp))		
