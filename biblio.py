class document():
    __count=0
    def __init__(self , reference=0 , titre="" , auteur="" , page=0 ):
        self.__reference = reference
        self.__titre = titre
        self.__auteur = auteur 
        self.__page = page
        document.__count = document.__count+1

    #getters
    @property
    def getreference(self):
        return self.__reference
    
    @property
    def gettitre(self):
        return self.__titre 
    
    @property
    def getauteur(self):
        return self.__auteur
    
    @property
    def getpage(self):
        return self.__page
    
    @property
    def getcount(self):
        return document.__count
    
    #setters
    
    def setreference(self,new):
        self.__reference = new
    
    def settitre(self, n):
        self.__titre = n
    
    def setauteur(self,n):
        self.__auteur = n

    def setpage(self , n):
        self.__page = n

    #methodes
   
    def Equals(self , D):
        if self.getreference == D.getreference:
            return True
        else:
            return False
    
    def calculcout(self):
        T=2.3* self.getpage
        return f"{T} DH"
    
    def ToString(self):
        return f"la reference du document est: {self.getreference}\nson titre est {self.gettitre}\nson Auteur est:{self.getauteur} \net son nombre de pages est:{self.getpage} \nson nombre est:{self.getcount} \nson prix total est :{self.calculcout()}DH "
    
class roman(document):
    def __init__(self , reference=0 , titre="" ,auteur="", page=0, editeur="" , anne=0):
        super().__init__(reference , titre, auteur, page)
        self.__editeur = editeur
        self.__anne = anne

    #getters
    @property
    def getedit(self):
        return self.__editeur
    
    @property
    def getanne(self):
        return self.__anne
    
    #setters

    def setedit(self, n):
        self.__editeur = n
    
    def setanne(self , n):
        self.__anne = n
    
    #overriding
    
    def ToString(self):
        return  f"{super().ToString() }\nl'editeur du Roman est :{self.getedit}, et sa date de publication {self.getanne}"
    
class revue(document):
    def __init__(self,reference=0, titre="", auteur="",page=0,mois="",anne=0):
        super().__init__(reference , titre, auteur, page)
        self.__mois = mois
        self.__anne = anne

    #getters
    @property
    def getmois(self):
        return self.__mois
    @property
    def getanne(self):
        return self.__anne 

    #setters
    def setmois(self, n):
        self.__mois = n
    def setanne(self, n):
        self.__anne = n
    
    #overridding
    def ToString(self):
        return f"{super().ToString()}\nle mois de publication est:{self.getmois} et son anne de publication est :{self.getanne}"
    
class biblio():
    def __init__(self, nom , adresse , listdoc):
        self.__nom = nom 
        self.__adresse = adresse
        self.__listdoc = listdoc

    #getters
    @property
    def getnom(self):
        return self.__nom
    @property
    def getadresse(self):
        return self.__adresse
    @property
    def getlistdoc(self):
        return self.__listdoc
    
    #setters

    def setnom(self, n):
        self.__nom = n
    
    def setadress(self, n):
        self.__adresse = n
    
    def setlistdoc(self, n):
        self.__listdoc = n

    #method
        
    def ToString(self):
        print (f"la bibliotheque {self.getnom} , se trouve a {self.getadresse} , les produits existants a la biblio sont :")
        i=0
        for x in self.getlistdoc:
            list={"reference":[] , "titre":[] , "Auteur":[], "nbre de page":[],"prix":[]}

            list["reference"].append(x.getreference)
            list["titre"].append(x.gettitre)
            list["Auteur"].append(x.getauteur)
            list["nbre de page"].append(x.getpage)
            list["prix"].append(x.calculcout())
            i=i+1
            print("le produit numero" , i, "est: ",list)
        
    
            
            

    def add(self , p):
        self.getlistdoc.append(p)

    def check(self,r):
        list=[]
        for x in self.getlistdoc:
            if x.getreference == r:
               print("le produits existe dans la bibliotheque:",x.ToString())
               list.append(x)
        
        if list==[]:
            print("ce document n'existe pas")

         
    def listroman(self):
        print("les roman existant dans la bibliotheque sont :")
        for x in self.getlistdoc:
            if type(x) == roman:
                print (x.ToString())

    def supprimer(self , r):
        for x in self.getlistdoc:
            if x.getreference == r :
                self.getlistdoc.remove(x)
                print("document est supprime")












#main programm
D1=document(527365, "the miracle morning" , "frah" ,4984)
D2=roman(489, "tsag" , "mariam" , 123,"iud",2004)
D3=document(394, "the miracle morning" , "wissal" , 1230)

b=biblio("farah" , "marrakech" , [D1,D2,D3])

D4=roman(35 , "the miracle morning" , "hassna" , 392 , "sdcj" , 2016)
b.add(D4)
# b.supprimer(394)
# b.ToString()
b.check(350)



