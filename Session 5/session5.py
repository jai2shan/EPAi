import time

def time_it(fn, *args, repetitions= 1, **kwargs):
    if repetitions<=0:
        raise ValueError('Repetitions cannot be 0 or less than 0')
    # assert repetitions>0, 'Repetitions cannot be 0 or less than 0'
    start = time.time()
    for i in range(0,repetitions):
        fn(*args, **kwargs)
    timetaken = (time.time()-start)
    return timetaken

def squared_power_list(n,start=0,end=5):
    ## Assertions
    if start<0:
        raise ValueError('Start cannot be less than 0')
    # assert start>=0, 'Start cannot be less than 0'
    assert end>0,'End cannot be less than 1'
    assert type(start)!=float, 'Start cannot be a float'
    assert type(end)!=float,'End cannot be a float'
    return [n**i for i in list(range(start,end+1))]

def polygon_area(n, sides=3):
    ## Assertions
    assert type(sides)!=float,"#sides cannot be of float data type" 
    assert (n>0),'# length of side cannot be less than or equal to zero'
    assert sides>0,'Sides cannot be less than 0'
    assert (sides!=1) and (sides!=2), "Sides cannot be less than 3 for a polygon"
    assert (sides<=6), "polygon_area is programmed only for eq. triangle, square, pentagon, hexagon"

    ## Area of Polygon
    area = {3:(3**0.5)*(1/4)*n*n,
            4:(n*n),
            5:(1/4)*((5*(5+(2*(5)**0.5)))**0.5)*n*n,
            6:((3)**0.5)*(3/2)*n*n}
    # print(area[sides])
    return area[sides]

def temp_converter(temp,temp_given_in = 'f'):
    assert temp_given_in in ['f','c'], 'Temperature given in can be Celsius or Fahrenheit'
    converted = {'f':((temp - 32) * (5/9) ),
                 'c':((temp * 9/5) + 32)}
    # print(converted[temp_given_in])
    return converted[temp_given_in]  

def speed_converter(speed,dist = 'km',time='min'):
    assert dist in 'km/m/ft/yrd'.split('/'), 'Distance is not in km/m/ft/yrd. Only km/m/ft/yrd types are allowed'
    assert time in 'ms/s/min/hr/day'.split('/'), 'Time not in ms/s/min/hr/day. Only ms/s/m/hr/day allowed'

    dist_map = {'km':1,
                'm':1000,
                'ft':3280.84,
                'yrd':1093.6133333333}
    time_map = {'ms':3.6*10**6,
                's':3600,
                'min':60,
                'hr':1,
                'day':0.0416667}
    return speed*(dist_map[dist]/time_map[time])