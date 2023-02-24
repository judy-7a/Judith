#6936521
#judith ESSEL




#car brands and their prices in cedis
cars={'2012 Merceredes-Benz C250':163450,
      '2004 Toyota corolla':31500,
      '2007 Kia sorento':50000,
      '2013 Ford Escape SEL':75000,
'2006 Porsche cayenne':120000,
' 2017 Hyundai Elantra':110000,
'2020 Nissan Navara':456250,
'2022 Suzuki Alto GLX':126412,
'2022 Lexus LX 570':345000,
'Toyota RAV4':457800,
'Mahindra Thar':900000,
'Tata Nexon':56000,
'Maruti Brezza':40900,
'Hyundai Creta':87000,
'BMW i3':87800,
'Chevy volt':66480,
'Ford Fusion Energi':86990,
'Lamborghini':70890,
'2020 Toyota corolla':889000,
'2014 Hyundai Elantra':88000,
'kankatanka car':890400,
'Toyota Vitz':22000
 ,'Totota Hilux':42000,
 'RollsRoyce':230000,
 'Landcrusier':110000,
 'Honda Civic':22000,
 'Highlander XLE':36000,
 'Honda CRV':32000,
 'Toyota Avalon':32000,
 'Tucson':26000}
 #get user input for the car_ brand
carbrand= input('Enter a car brand').strip()
#check if car brand is in the list of available cars
if carbrand in cars:
    print('yes, carbrand is available')
#if carbrand in cars is present,get its price
car_price=input(cars)
print('the price of {carbrand} is ${car_price}.')
#if carbrand is unavailable
print('sorry, car is not available')
