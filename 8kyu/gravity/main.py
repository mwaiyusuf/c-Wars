def solution(arr_val, arr_unit) :
    # your code goes here
       arr_val = [m1,m2,d];
       arr_unit = [um1,um2,ud]
       G = 6.67e-11 ;
       conversion = {
          'kg':'1', 'g':'1e-3', 'mg':'1e-6', 'μg':'1e-9', 'lb':'.453592'
          , 'm':'1', 'cm':'1e-2', 'mm':'1e-3', 'μm':'1e-6', 'ft':'.3048'
       };
       return G * m1 * conversion[um1] * m2 * conversion[um2] / ( d * conversion[ud] ) ** 2 ;