import numpy as np
import math



class generate:

    srcfilename=""
    srcfilenamexy=""

    number=10
    coef=1
    size=90
    reso=12
    side=20

    def __init__(self,srcfilename="",number=10,coef=1) : 
        self.srcfilename=srcfilename 
        self.number=number
        self.coef=coef

    def set_srcfilename2(self,srcfnam2):
        self.srcfilenamexy=srcfnam2

    def set_srcfilename(self,srcfnam):
        self.srcfilename=srcfnam

    def set_number(self,number):
        self.number=number

    def set_coef(self,coef):
        self.coef=coef

    def set_reso(self,reso):
        self.reso=reso

    def create(self):
        #self.xupper=np.random.random_integers(low=0,high=self.size,size=self.number)
        #self.yupper=np.random.random_integers(low=0,high=self.size,size=self.number)
        #self.rasrc=np.random.uniform(low=0.,high=360.,size=self.number)
        #self.decsrc=np.random.uniform(low=85,high=90,size=self.number)
        self.Jansrc=self.coef*np.ones(self.number)
        #self.srclist=np.transpose((self.rasrc,self.decsrc,self.Jansrc))
        #self.xlower=self.yupper
        #self.ylower=self.size-self.xupper
        #self.xcenter=self.xlower-self.size/2 
        #self.ycenter=self.ylower-self.size/2
        self.xcenter=np.random.random_integers(low=-self.size/2+self.side,high=self.size/2-self.side,size=self.number)
        self.ycenter=np.random.random_integers(low=-self.size/2+self.side,high=self.size/2-self.side,size=self.number)
        self.srclistxy=np.transpose((self.xcenter,self.ycenter,self.Jansrc))


    def convert_xpixels_radeg(self):
        

        self.decrad_center=90*math.pi/180
        self.rarad_center=180*math.pi/180
        self.scale=60/self.reso
        #self.xrad=self.final_list[:,1]/(self.scale*180/math.pi)
        #self.yrad=self.final_list[:,2]/(self.scale*180/math.pi)
        self.xrad=self.xcenter/(self.scale*180/math.pi)
        self.yrad=self.ycenter/(self.scale*180/math.pi)
        self.D=np.arctan(np.sqrt((self.xrad**2+self.yrad**2)))
        self.B=np.arctan2(-self.xrad,self.yrad)
        self.xx=np.sin(self.decrad_center)*np.sin(self.D)*np.cos(self.B) + np.cos(self.decrad_center)*np.cos(self.D)
        self.yy=np.sin(self.D)*np.sin(self.B)
        
        self.rarad=self.rarad_center+np.arctan2(self.yy,self.xx)
        self.decrad=np.arcsin(np.sin(self.decrad_center)*np.cos(self.D)-np.cos(self.decrad_center)*np.sin(self.D)*np.cos(self.B))
        self.rasrc=self.rarad*180/math.pi
        self.decsrc=self.decrad*180/math.pi
        self.srclist=np.transpose((self.rasrc,self.decsrc,self.Jansrc))

    def convert2(self):
        self.rarad2=np.arctan2(self.xrad,self.yrad)
        self.thetarad=np.arctan(np.sqrt(self.xrad**2+self.yrad**2))
        self.thetaraddeg=self.thetarad*180/math.pi
        self.decrad2=(np.pi/2)-self.thetarad 
        self.rasrc2=self.rarad2*180/math.pi
        self.decsrc2=self.decrad2*180/math.pi
        self.srclist2=np.transpose((self.rasrc2,self.decsrc2,self.Jansrc))
        

    def export_txt(self):
        filetxt=open(self.srcfilename,'w')
        np.savetxt(filetxt,self.srclist,fmt='%.4f',delimiter='     ',header='generated sources number:{} \nra(deg)     dec(deg)  flux(Jansky)'.format(self.number))
        filetxt.close()
    def export_txt2(self):
        filetxt2=open(self.srcfilenamexy,'w')
        np.savetxt(filetxt2,self.srclistxy,fmt='%.4f',delimiter='     ',header='generated sources number:{} \nx     y  flux(Jansky)'.format(self.number))
        filetxt2.close()
        
    def run(self):
        self.create()
        self.convert_xpixels_radeg()
        self.convert2()
        self.export_txt()
        self.export_txt2()

