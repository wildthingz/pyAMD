import numpy as np
import matplotlib.pyplot as plt

class AMD():

	def __init__(self,name="1D-DI30.dat"):
		self.name =name
		try:
			fromtec = open(name,'r')
		except IOError:
			raise Exception("Check your directory!")
		
		i=0
		j=-1
		self.X=np.array([])
		self.Y=np.array([])
		self.eut=np.array([])
		for line in fromtec:
			i+=1
			if i==2 and j<0:
				self.N=int(line.split()[1][2:-1])
				j=0
			elif j>=0 and j<self.N and i>3:
				self.X=np.append(self.X,float(line.split()[0]))
				self.Y=np.append(self.Y,float(line.split()[1]))
				self.eut=np.append(self.eut,float(line.split()[2]))
				j+=1
	
	def getAMD(self,kernelSize=50):
		tmp = np.ones((self.N,1))
		eut_vic = np.transpose(self.eut*tmp)
		X_vic = (np.transpose(self.X*tmp) - (self.X*tmp))**2
		Y_vic = (np.transpose(self.Y*tmp) - (self.Y*tmp))**2
		
		vic = np.sqrt(X_vic+Y_vic)
		return(np.sum(np.max(eut_vic*(vic<kernelSize),axis=0))/self.N)
	
	def plotLinGrad(self, (minComp,maxComp),dim="1D",mode="I"):
		
		ys = self.Y[(self.X>=459)*(self.X<=505)]
		euts = self.eut[(self.X>=459)*(self.X<=505)]
		plt.figure()
		plt.plot(1000-ys,euts,'ro')
		if dim=="1D":
			if mode=="I":
				gradx = [0,1000]
				grady = [minComp,maxComp]
			elif mode=="D":
				gradx = [1,1000]
				grady = [maxComp,minComp]
			elif mode=="ID":
				gradx = [1,500,1000]
				grady = [minComp,maxComp,minComp]
			elif mode=="DI":
				gradx = [1,500,1000]
				grady = [maxComp,minComp,maxComp]
			else:
				raise TypeError("Mode is not specified correctly")
		elif dim=="2D":
			if mode=="I":
				gradx = [1,500,1000]
				grady = [minComp,maxComp,minComp]
			elif mode=="D":
				gradx = [1,500,1000]
				grady = [maxComp,minComp,maxComp]
			elif mode=="ID":
				gradx = [1,250,500,750,1000]
				grady = [minComp,maxComp,minComp,maxComp,minComp]
			elif mode=="DI":
				gradx = [1,250,500,750,1000]
				grady = [maxComp,minComp,maxComp,minComp,maxComp]
			else:
				raise TypeError("Mode is not specified correctly")
		else:
			raise TypeError("Dimension is not specified correctly")
			
		plt.plot(gradx,grady,'--')
		plt.title("Gradient Comparison for "+self.name)
		plt.legend(["Calculated gradient","Actual gradient"])
		plt.xlabel("Position")
		plt.ylabel("Area fraction")
		plt.savefig("grad"+self.name[:-3]+"png")
		
#a=AMD()
#print(a.getAMD())
