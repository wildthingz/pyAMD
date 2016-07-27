import numpy as np
import matplotlib.pyplot as plt
import random
import math
import scipy.misc

class microGen():
	
	def __init__(self, width,length,fraction):
		self.phi = fraction
		self.img = np.zeros((width,length))
	
	def randInd(self):
		w,l=np.shape(self.img)
		# Empirical formula
		try:
			emp = ((math.exp(self.phi)/(1.0-self.phi))**0.3) - (self.phi/10.0)
		except ValueError:
			print("Error in fraction")
			print(self.phi)
		size = int(emp*w*l*self.phi)
		widthInds = np.int_(np.random.rand(1,size)*w)
		lengthInds = np.int_(np.random.rand(1,size)*l)
		return (np.int_(widthInds[0]),np.int_(lengthInds[0]))
		
	def generate(self):
		w,l=np.shape(self.img)
		frac = 0.0
		if self.phi == 0:
			return self.img
		elif self.phi >= 1:
			return (np.ones((w,l)))
		else:
			cnt=0
			while (abs(frac-self.phi)/self.phi)>0.02:
				self.img = np.zeros((w,l))
				tmpw,tmpl = self.randInd()
				self.img[tmpw,tmpl] = 1.0
				frac = np.sum(self.img)/(w*l)
				cnt+=1
				if cnt>10000:
					print("Warning: Results not accurate")
					break
					#raise ValueError("The two bound are too close to each other.")
				#print(frac)
		return self.img
		
class gradientGen(microGen):
	
	def __init__(self,(minPhi,maxPhi),dim="1D",mode="I",size=1000):
		self.dim = dim
		self.mode = mode
		self.size=size
		if minPhi>maxPhi:
			tmp = minPhi
			minPhi = maxPhi
			maxPhi = tmp
		self.range = [minPhi,maxPhi]
		if self.range[1]>1.0 or self.range[0]<0:
			raise ValueError("The specified fraction is not between 0 and 1.")
		
	def grad1D(self):
		self.img = np.zeros((self.size/100,self.size))
		if self.mode == "I":
			self.phi=self.range[0]
			self.IM = self.generate()		
			for i in range(1,100):
				self.phi = ((self.range[1] - self.range[0])/99.0)*i + self.range[0]
				tmp = self.generate()
				self.IM = np.concatenate((self.IM,tmp))	
		elif self.mode == "D":
			self.phi=self.range[1]
			self.IM = self.generate()
			for i in range(1,100):
				self.phi = self.range[1] - ((self.range[1] - self.range[0])/99.0)*i
				tmp = self.generate()
				self.IM = np.concatenate((self.IM,tmp))
		elif self.mode == "ID":
			self.phi=self.range[0]
			self.IM = self.generate()	
			for i in range(1,50):
				self.phi = ((self.range[1] - self.range[0])/49.0)*i + self.range[0]
				tmp = self.generate()
				self.IM = np.concatenate((self.IM,tmp))
			for i in range(1,50):
				self.phi = self.range[1] - ((self.range[1] - self.range[0])/49.0)*i
				tmp = self.generate()
				self.IM = np.concatenate((self.IM,tmp))	
		elif self.mode == "DI":
			self.phi=self.range[1]
			self.IM = self.generate()		
			for i in range(1,50):
				self.phi = self.range[1] - ((self.range[1] - self.range[0])/49.0)*i
				tmp = self.generate()
				self.IM = np.concatenate((self.IM,tmp))
			for i in range(1,50):
				self.phi = ((self.range[1] - self.range[0])/49.0)*i + self.range[0]
				tmp = self.generate()
				self.IM = np.concatenate((self.IM,tmp))	
		return self.IM
	
	def grad2D(self):
		self.img = np.zeros((self.size,self.size))
		if self.mode == "I":
			self.phi=self.range[0]
			self.IM = self.generate()
			for i in range(1,100):
				self.img = np.zeros((self.size-self.size*i/100,self.size-self.size*i/100))
				self.phi = ((self.range[1] - self.range[0])/99.0)*i + self.range[0]
				tmp = self.generate()
				self.IM[self.size*i/200:-self.size*i/200,self.size*i/200:-self.size*i/200] = tmp
		elif self.mode == "D":
			self.phi=self.range[1]
			self.IM = self.generate()
			for i in range(1,100):
				self.img = np.zeros((self.size-self.size*i/100,self.size-self.size*i/100))
				self.phi = self.range[1] - ((self.range[1] - self.range[0])/99.0)*i
				tmp = self.generate()
				self.IM[self.size*i/200:-self.size*i/200,self.size*i/200:-self.size*i/200] = tmp
		elif self.mode == "ID":
			self.phi=self.range[0]
			self.IM = self.generate()
			for i in range(1,50):
				self.img = np.zeros((self.size-self.size*i/100,self.size-self.size*i/100))
				self.phi = ((self.range[1] - self.range[0])/49.0)*i + self.range[0]
				tmp = self.generate()
				self.IM[self.size*i/200:-self.size*i/200,self.size*i/200:-self.size*i/200] = tmp
			for i in range(51,100):
				self.img = np.zeros((self.size-self.size*i/100,self.size-self.size*i/100))
				self.phi = self.range[1] - ((self.range[1] - self.range[0])/49.0)*(i-50)
				tmp = self.generate()
				self.IM[self.size*i/200:-self.size*i/200,self.size*i/200:-self.size*i/200] = tmp
		elif self.mode == "DI":
			self.phi=self.range[1]
			self.IM = self.generate()
			for i in range(1,50):
				self.img = np.zeros((self.size-self.size*i/100,self.size-self.size*i/100))
				self.phi = self.range[1] - ((self.range[1] - self.range[0])/49.0)*i
				tmp = self.generate()
				self.IM[self.size*i/200:-self.size*i/200,self.size*i/200:-self.size*i/200] = tmp
			for i in range(51,100):
				self.img = np.zeros((self.size-self.size*i/100,self.size-self.size*i/100))
				self.phi = ((self.range[1] - self.range[0])/49.0)*(i-50) + self.range[0]
				tmp = self.generate()
				self.IM[self.size*i/200:-self.size*i/200,self.size*i/200:-self.size*i/200] = tmp
		return self.IM
		
	def run(self):
		if self.dim == "1D":
			return self.grad1D()
		elif self.dim == "2D":
			return self.grad2D()
		else:
			raise ValueError("Specify a correct dimension") 
			
				
#for dim in ["1D","2D"]:
#	for mode in ["I","D","ID","DI"]:
#		a=gradientGen((0.05,0.15),dim,mode)
#		im = (a.run()*(-100)+150)
#		name = dim+"-"+mode+".png"
#		scipy.misc.toimage(im, cmin=0.0, cmax=255.0).save(name)
#print(im)
