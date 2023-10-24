import csv

class Row():
  def __init__(self, country, year, status, life_expec, adult_mort, infant_death, alcohol, percent_exp, hepatitis, measels, BMI, under_five, polio, total_expend, diphteria, hiv, gdp, pop, thinness1, thinness2, income_comp, school):
    self.country = country
    self.year = year
    self.status = status
    self.life_expec = life_expec
    self.adult_mort = adult_mort
    self.infant_death = infant_death
    self.alcohol = alcohol
    self.percent_exp = percent_exp
    self.hepatitis = hepatitis
    self.measels = measels
    self.BMI = BMI
    self.under_five = under_five
    self.polio = polio
    self.total_expend = total_expend
    self.diphteria = diphteria
    self.hiv = hiv
    self.gdp = gdp
    self.pop = pop
    self.thinness1= thinness1
    self.thinness2 = thinness2
    self.income_comp = income_comp
    self.school = school

class Tree():
  rows = []
  def __init__(self):
    with open("Life Expectancy Data.csv") as file:
      temp = 0
      reader = csv.reader(file, delimiter=',')
      for row in reader:
        if(temp != 0):
          row = Row(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21])
          print(temp)
          print(row.gdp)
          self.rows.append(row)
        temp = temp + 1
           
      


  