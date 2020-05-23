import json 
  
  
# the file to be converted 
filename = 'results_targetRNA1.txt'

with open(filename) as fh: 
    whole_file = fh.read()
    whole_array = whole_file.split('\n')
    print(whole_array)

node_1_array = []
node_2_array = []
edges_array = []
for i in range(0,len(whole_array),3):
    if(i == len(whole_array)-1 or i == len(whole_array)-2):
        break
    node_1_array.append(whole_array[i].replace('>',''))
    node_2_array.append(whole_array[i+1].replace('>',''))
    edges_array.append(whole_array[i+2])


final_array = []
single_whole_item = []
for j in range(len(node_1_array)):
    single_whole_item.append(node_1_array[j])
    single_whole_item.append(node_2_array[j])
    single_whole_item.append(edges_array[j])
    final_array.append(single_whole_item)
    single_whole_item = []

#here final array has things in good order 


output_array = []
temp_list = []
temp_dict ={}
source_node = {}
target_node = {}
an_edge ={}
for i in final_array:
    temp_dict = dict(id= i[0]+i[1],source = i[0], target = i[1], bonus_info = i[2])
    an_edge = dict(data = temp_dict)



    temp_dict = dict(id = i[0])
    source_node = dict(data = temp_dict)


    temp_dict = dict(id = i[1])
    target_node = dict(data = temp_dict)

    temp_list.append(source_node)
    temp_list.append(target_node)
    temp_list.append(an_edge)

    output_array.append(temp_list)
    temp_list = []



out_file = open("output.json", "w") 
json.dump(output_array, out_file, indent = 0, sort_keys = False) 
out_file.close() 

