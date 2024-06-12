'''
 create a class car showroom
 1- create fun named car company which will allow user to select car company out display companys
 if user enters any random car company he or she should be asked to reenter 
 2- according to the car company selected the user should be redirected to selecting the models of that company of the given list.
    if any other car is entered again reenter 
 3- after selecting the model the uder should be redirected to selecting the variant(petrol/diesel).
 4- according to the car company model and variant a price should be calculated to which sgst and cgst are added
    to make it the total price.
    note--
         sgst and cgst are common for all the cars. 

 '''
cars = {
    "tata": {
        "nexon": 1000000,
        "harrier": 2000000,
        "punch": 700000
    },
    "audi": {
        "a6": 3000000,
        "a8": 6000000
    },
    "bmw": {
        "m1": 4000000,
        "q2": 8000000
    },
    "mercedes": {
        "c-class": 3500000,
        "e-class": 5000000,
        "s-class": 9000000
    },
    "toyota": {
        "corolla": 1500000,
        "camry": 2500000,
        "fortuner": 3500000
    },
    "honda": {
        "city": 1300000,
        "civic": 1800000,
        "accord": 2800000
    },
    "hyundai": {
        "i20": 800000,
        "verna": 1000000,
        "creta": 1200000
    },
    "ford": {
        "figo": 700000,
        "ecosport": 900000,
        "endeavour": 3000000
    },
    "kia": {
        "seltos": 1100000,
        "sonet": 900000,
        "carnival": 2500000
    },
    "volkswagen": {
        "polo": 800000,
        "vento": 1000000,
        "tiguan": 2500000
    },
    "renault": {
        "kwid": 500000,
        "duster": 900000,
        "kiger": 700000
    },
    "chevrolet": {
        "beat": 600000,
        "cruze": 1500000,
        "trailblazer": 2500000
    },
    "nissan": {
        "micra": 700000,
        "kicks": 1000000,
        "terrano": 1200000
    },
    "jaguar": {
        "xf": 5000000,
        "f-type": 8000000,
        "i-pace": 10000000
    },
    "lexus": {
        "es": 6000000,
        "rx": 7000000,
        "lx": 10000000
    },
    "mahindra": {
        "xuv300": 900000,
        "scorpio": 1200000,
        "alturas": 3000000
    },
    "fiat": {
        "punto": 700000,
        "linea": 900000,
        "urban cross": 1000000
    },
    "skoda": {
        "rapid": 1000000,
        "superb": 2500000,
        "kodiaq": 3000000
    },
    "tesla": {
        "model 3": 5000000,
        "model S": 8000000,
        "model X": 9000000
    },
    "porsche": {
        "911": 10000000,
        "cayenne": 15000000,
        "panamera": 20000000
    },
    "mclaren": {
        "570S": 12000000,
        "720S": 18000000,
        "sennterra": 25000000
    },
    "aston martin": {
        "vantage": 15000000,
        "db11": 20000000,
        "dbx": 25000000
    },
    "lotus": {
        "evora": 12000000,
        "exige": 18000000,
        "elise": 15000000
    },
    "rolls-royce": {
        "ghost": 30000000,
        "phantom": 40000000,
        "cullinan": 50000000
    },
    "bentley": {
        "continental": 25000000,
        "bentayga": 30000000,
        "mulsanne": 35000000
    },
    "mini": {
        "cooper": 3500000,
        "countryman": 4000000,
        "clubman": 4500000
    },
    "land rover": {
        "defender": 6000000,
        "discovery": 8000000,
        "range rover": 12000000
    },
    "volvo": {
        "s60": 5000000,
        "xc40": 6000000,
        "xc90": 8000000
    },
    "infiniti": {
        "q50": 3500000,
        "qx60": 4500000,
        "q80": 6000000
    },
    "alfa romeo": {
        "giulia": 4000000,
        "stelvio": 4500000,
        "4C": 5000000
    },
    "maserati": {
        "ghibli": 8000000,
        "levante": 10000000,
        "quattroporte": 12000000
    },
    "bugatti": {
        "chiron": 200000000,
        "divo": 250000000,
        "centodieci": 300000000
    }
}


class CarShowroom:
    def company(self):
        while True:
            for i in cars.keys():
                print(i)
            self.ch = input("Choose company: ")
            if self.ch in cars.keys():
                self.models(self.ch)
                break
            else:
                print("Enter valid car company")
    def models(self,ch):
        # print(cars[ch]["models"].keys())
        print(f"Welcome to {ch}")
        while True:
            for i in cars[ch]:
                print(i)
            self.model= input("Choose model: ")
            if self.model in cars[ch].keys():
                self.bill(cars[ch][self.model])
                break
            else:
                print("Enter valid model")
    def bill(self,ch):
        self.cgst = 0.09
        self.sgst = 0.09
        self.fprice = ch+(ch*self.cgst*2)
        print("------------------------------------------")
        print("Car Price:\t\t", ch)
        print("Car price inc gst: \t\t",self.fprice)
        print("Happy Shopping...")
obj = CarShowroom()
obj.company()
        

