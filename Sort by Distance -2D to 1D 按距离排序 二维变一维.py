# -*- coding: UTF-8 -*-
# 运行环境：Python 3.8（为兼容 Windows 7 及 Windows 2008 系统）
# 作者邮箱：chaoxian102@gmail.com
# 微信：chaoxian102（超弦102）
# 支付宝：abtrue@hotmail.com
# Paypal：https://paypal.me/abtruecom
# 感谢打赏


import math

# Original coordinates dictionary
locations = {
  "地点1": [-68.459749, 19.576036],
  "地点2": [-69.167916, 19.362475],
  "地点3": [-60.738679, 16.316532],
  "地点4": [-62.525037, 21.078188],
  "地点5": [-64.605443, 21.416567],
  "地点6": [-63.169815, 24.523393],
  "地点7": [-64.41642, 19.109507],
  "地点8": [-63.564409, 16.911858],
  "地点9": [-64.660603, 22.805564],
  "地点10": [-67.092302, 15.557957],
  "地点11": [-69.877539, 24.771631],
  "地点12": [-66.043768, 24.157635],
  "地点13": [-63.785934, 24.882358],
  "地点14": [-67.16295, 20.440024],
  "地点15": [-62.463291, 16.485193],
  "地点16": [-67.349724, 23.529065],
  "地点17": [-69.473104, 16.323893],
  "地点18": [-60.872603, 23.63704],
  "地点19": [-66.432864, 16.560613],
  "地点20": [-66.276541, 20.089615],
  "地点21": [-64.642048, 22.76146],
  "地点22": [-65.444098, 21.020842],
  "地点23": [-68.838206, 22.271088],
  "地点24": [-66.110144, 19.707402],
  "地点25": [-67.904399, 20.601145],
  "地点26": [-69.408112, 23.184495],
  "地点27": [-65.204302, 16.10161],
  "地点28": [-69.661051, 19.918369],
  "地点29": [-65.852651, 20.600034],
  "地点30": [-67.949139, 15.20352],
  "地点31": [-64.46682, 24.131603],
  "地点32": [-62.715425, 24.62582],
  "地点33": [-65.251322, 23.174911],
  "地点34": [-69.023764, 24.651643],
  "地点35": [-60.485425, 15.46967],
  "地点36": [-68.050306, 19.628681],
  "地点37": [-63.174517, 22.408413],
  "地点38": [-60.220738, 20.583994],
  "地点39": [-66.346656, 24.249041],
  "地点40": [-66.505658, 19.548011],
  "地点41": [-64.883601, 20.339122],
  "地点42": [-66.2112, 18.888687],
  "地点43": [-68.139639, 22.897146],
  "地点44": [-63.934343, 20.514796],
  "地点45": [-69.370405, 22.158745],
  "地点46": [-61.90352, 21.991869],
  "地点47": [-66.655881, 20.429115],
  "地点48": [-63.884195, 15.334594],
  "地点49": [-66.836308, 17.985883],
  "地点50": [-64.050411, 16.514338],
  "地点51": [-60.753917, 23.389033],
  "地点52": [-63.742849, 22.559517],
  "地点53": [-69.646072, 17.353622],
  "地点54": [-63.934737, 16.030823],
  "地点55": [-68.034475, 19.530267],
  "地点56": [-66.359887, 19.832951],
  "地点57": [-66.919095, 19.608425],
  "地点58": [-69.796203, 23.584133],
  "地点59": [-60.031392, 23.739774],
  "地点60": [-66.372463, 16.212805],
  "地点61": [-61.440249, 23.817013],
  "地点62": [-62.526613, 19.639224],
  "地点63": [-65.706282, 16.297979],
  "地点64": [-65.658638, 21.881637],
  "地点65": [-66.635597, 17.490133],
  "地点66": [-69.916388, 19.19721],
  "地点67": [-68.083933, 15.062933],
  "地点68": [-62.751556, 15.270219],
  "地点69": [-63.978633, 15.852757],
  "地点70": [-60.023206, 23.074867],
  "地点71": [-69.888121, 15.584965],
  "地点72": [-63.823232, 21.788843],
  "地点73": [-65.917832, 15.083654],
  "地点74": [-68.260235, 19.981674],
  "地点75": [-68.231156, 16.232318],
  "地点76": [-68.412385, 19.541695],
  "地点77": [-68.868334, 24.276744],
  "地点78": [-65.618842, 20.164826],
  "地点79": [-60.813819, 18.508526],
  "地点80": [-60.915121, 16.00948],
  "地点81": [-64.942503, 16.081177],
  "地点82": [-68.656158, 24.933636],
  "地点83": [-68.238848, 22.942898],
  "地点84": [-64.910336, 19.041055],
  "地点85": [-62.942926, 16.721975],
  "地点86": [-63.135612, 24.013294],
  "地点87": [-66.341812, 15.316193],
  "地点88": [-61.707276, 15.437768],
  "地点89": [-67.574214, 21.308215],
  "地点90": [-60.25377, 20.392803],
  "地点91": [-62.117515, 15.37494],
  "地点92": [-67.639957, 23.489429],
  "地点93": [-62.541293, 20.67313],
  "地点94": [-69.461099, 22.000301],
  "地点95": [-67.79733, 22.833951],
  "地点96": [-65.055215, 24.962566],
  "地点97": [-66.820404, 23.157713],
  "地点98": [-67.300932, 20.127233],
  "地点99": [-66.396036, 18.627518],
  "地点100": [-61.174656, 24.313125]
}


# Function to calculate distance between two points using Haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in kilometers
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    distance = R * c
    return min(distance, 2 * math.pi * R - distance)

# Process coordinates and create sorted list
processed_list = []
for name, (lon, lat) in locations.items():
    # Adjust longitude (+180) and latitude (90-) to ensure positive values
    adjusted_lon = lon + 180
    adjusted_lat = 90 - lat
    
    # Multiply by 10^6 and convert to integer
    lon_int = int(adjusted_lon * 1000000)
    lat_int = int(adjusted_lat * 1000000)
    
    # Convert to binary and pad to 29 digits
    lon_bin = bin(lon_int)[2:].zfill(29)
    lat_bin = bin(lat_int)[2:].zfill(29)
    
    # Interleave binary strings
    fused_bin = ''
    for i in range(29):
        fused_bin += lon_bin[i] + lat_bin[i]
    
    # Convert fused binary to decimal
    fused_decimal = int(fused_bin, 2)
    
    processed_list.append([fused_decimal, name, lon, lat])

# Sort list by fused decimal value
processed_list.sort()

# Main loop
while True:
    # Get input from user
    search_name = input("请输入地点名称（输入'退出'结束程序）: ")
    
    if search_name == '退出':
        print("程序结束")
        break
        
    if search_name not in locations:
        print("地点不存在，请重新输入")
        continue
    
    # Process search coordinates
    search_lon, search_lat = locations[search_name]
    adjusted_lon = search_lon + 180
    adjusted_lat = 90 - search_lat
    lon_int = int(adjusted_lon * 1000000)
    lat_int = int(adjusted_lat * 1000000)
    lon_bin = bin(lon_int)[2:].zfill(29)
    lat_bin = bin(lat_int)[2:].zfill(29)
    fused_bin = ''
    for i in range(29):
        fused_bin += lon_bin[i] + lat_bin[i]
    search_decimal = int(fused_bin, 2)
    
    # Find position in sorted list
    position = -1
    for i, (decimal, name, _, _) in enumerate(processed_list):
        if name == search_name:
            position = i
            break
    
    print(f"\n搜索地点: {search_name} ({search_lon}, {search_lat})")
    print("附近地点:")
    
    # Generate offset sequence: +1, -1, +2, -2, +3, -3, etc. until 10 results
    results = []
    offset = 1
    count = 0
    direction = 1  # 1 for right, -1 for left
    
    while count < 10 and offset <= len(processed_list):
        check_pos = position + (offset * direction)
        if 0 <= check_pos < len(processed_list):
            decimal, name, lon, lat = processed_list[check_pos]
            distance = calculate_distance(search_lat, search_lon, lat, lon)
            results.append((direction * offset, name, lon, lat, distance))
            count += 1
        
        # Switch direction after each offset
        if direction == 1:
            direction = -1
        else:
            direction = 1
            offset += 1  # Increase offset only after completing both right and left
    
    # Display results in the order they were found
    for offset, name, lon, lat, distance in results:
        print(f"位置 {offset}: {name} ({lon}, {lat}) - 距离: {distance:.2f} km")
    
    print()  # New line for next input
