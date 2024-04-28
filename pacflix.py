!pip install tabulate

from tabulate import tabulate
# isilah titik - titik di bawah ini
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

#cek plan yang tersedia
tables = [["Bisa Stream", True, True, True], 
          ["Bisa Download", True, True, True],
          ["Kualitas Penayangan SD", True, True, True],
          ["Kualitas Penayangan HD", False, True, True],
          ["Kualitas Penayangan UHD", False, False, True],
          ["Jumlah Device Terhubung", 1, 2, 4],
          ["Konten", "3rd party movie only", "Basic Plan Content + Sports F1, Football, Basketball)","Basic Plan + Standard Plan + PacFlix Original Series or Movie"],
          ["Harga", 120_000, 160_000, 200_000]
         ]
headers = ["Layanan", "Basic Plan", "Standard Plan", "Premium Plan"]

print(tabulate(tables, headers, tablefmt = "github"))

#buat kelas untuk User
class User: 
    
    def __init__(self, username, duration_plan, current_plan ):
        self.username = username
        self.duration_plan = duration_plan
        self.current_plan = current_plan
        
#buat fungsi untuk cek current plan       
    def check_current_plan(self, username):
        
        #iterate vkeys dan values based on data
         for keys, values in data.items():
                
            #buat branching untuk filter username    
            if username == keys:
                
                #buat variabel untuk store value (opsional -- tidak saya lakukan kali ini)
                get_duration_plan = values[1]
                get_current_plan = values[0]
                
                print(f"Username : {username}")
                print(f"Current plan {values[0]}")
                print(f"{values[1]} bulan")
                      
                      
#upgrade plan
    def upgrade_plan(self, username: str, upgrade_plan: str):

        DISCOUNT = 0.05

        for keys, values in data.items():

                          try:

                              if username == keys:

                                  get_duration_plan = values[1]
                                  get_current_plan = values[0]

                                  if upgrade_plan != get_current_plan:

                                      if get_duration_plan > 12:

                                          #branching untuk menentukan biaya setelah diskon
                                          if upgrade_plan == "Basic Plan":
                                              total_biaya = 120_000 - (DISCOUNT * 120_000)
                                              return total_biaya

                                          elif upgrade_plan == "Standard Plan":
                                              total_biaya = 160_000 - (DISCOUNT * 160_000)
                                              return total_biaya

                                          elif upgrade_plan == "Premium Plan":
                                              total_biaya = 200_000 - (DISCOUNT * 200_000)
                                              return total_biaya

                                          else:
                                              raise Exception("Unknown plan")
                                      else:
                                          #branching biaya kalau tidak diskon
                                          if upgrade_plan == "Basic Plan":
                                              total_biaya = 120_000 
                                              return total_biaya

                                          elif upgrade_plan == "Standard Plan":
                                              total_biaya = 160_000 
                                              return total_biaya

                                          elif upgrade_plan == "Premium Plan":
                                              total_biaya = 200_000 
                                              return total_biaya

                                          else:
                                              raise Exception("Unknown plan")


                                  else:
                                      raise Exception("Plan tidak boleh sama!")
                          except:
                              raise Exception("Unknown process!")
                          
# test case daftar dengan referral code
class NewUser:
    
    referral_code = []
    
    def __init__(self, username= str):
        self.username = username
    
    #method untk ekstrak referral code dari dictionary
    def get_referral_code(self, data):

        #iterasi ke data
        for values in data.values():
            ref_code = values[2]

            #append ke empty list
            self.referral_code.append(ref_code)
            
        return self.referral_code
    
    
    #method untuk new user pick plan
    def pick_plan(self, username, new_plan, kode_referal):
        
        DISCOUNT = 0.04
        
        if kode_referal in self.referral_code:
            
            if new_plan == "Basic Plan":
                total_biaya = 120_000 - (DISCOUNT * 120_000)
                return total_biaya
            
            elif new_plan == "Standard Plan":
                total_biaya = 160_000 - (DISCOUNT * 160_000)
                return total_biaya
            
            elif new_plan == "Premium Plan":
                total_biaya == 200_000 - (DISCOUNT * 200_000)
                return total_biaya
            else:
                raise Exception("Unknown plan")
            
        else:
            raise Exception("Referral code tidak ada!")
