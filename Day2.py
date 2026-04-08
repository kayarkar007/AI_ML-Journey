#list
nums=[4,5,6,7,7,8,9,10,11]
print(nums)

nums.append(12)
print(nums)
nums.remove(7)
print(nums)
print(nums[0])
nums.pop()
print(nums)
print(len(nums))


# tuples

point=(20,30,50)
print(point[2])


student = {
    "name": "Pavan",
    "marks": 90
}

print(student["name"])
print(student.get("name"))
print(student.keys())
print(student.values())

#Sets

numbers={1,4,6,6,5,5,7,7}
numbers2={9,8,9,0,7,6,8,9}
print(numbers|numbers2)
print(numbers&numbers2)


data = {
    "Pavan": [80, 90, 85],
    "Rahul": [70, 60, 75],
    "Amit": [90, 95, 92]
}

topper="";
highest_avg=0;
avgData={}
for name,marks in data.items():
    avg = sum(marks)/len(marks)
    print(f"{name}, average:{avg}")
    avgData[name] = avg

    if(avg>highest_avg):
        highest_avg=avg
        topper=name

print(f"Topper is:{topper},Highest_avg:{highest_avg}")
print(avgData)
sorted_data = sorted(avgData.items(), key=lambda x: x[1], reverse=True)
print(sorted_data)


