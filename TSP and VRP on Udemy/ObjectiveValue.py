import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial.distance as ssd
import random as rd

# How to compute distances
def Complete_Distance_Not_Random(Dist_array,Dist_Dataframe):
    t = 0
    r = 1
    Every_Dist_Truck = []
    for i in Dist_array:
        if r < len(Dist_array):
            # For each location and the one next to it, find it on the distance dataframe
            Dist = Dist_Dataframe.loc[Dist_array[t],Dist_array[r]]
            Every_Dist_Truck = np.append(Every_Dist_Truck,Dist)
            t = t+1
            r = r+1
    return sum(Every_Dist_Truck)
    

# Assess penalities for trucks carrying more than 100
def Penalty_1(Array,Penalty_Value, Cap_Dataframe):
    Truck_Cap_1_M_1,Truck_Cap_2_M_1 = [],[]     
    for j in Array: # Only the values between 1 and 10 (warehouses)
        if 1 <= j <= 10:
            Truck_Cap_1_M_1 = np.append(Truck_Cap_1_M_1,j) # The warehouses
    for i in Truck_Cap_1_M_1: # The warehouses' indexes
        value_index = np.where(Array == i) # Index of the warehouse
        Truck_Cap_2_M_1 = np.append(Truck_Cap_2_M_1,value_index) # Take the indecies of all the warehouses
    t = 0
    Caps_Sum_One_By_One  = []
    for k in range(len(Truck_Cap_2_M_1)):
        if t < 9:
            Ind_1 = int(Truck_Cap_2_M_1[t])+1 # Index + 1
            Ind_2 = int(Truck_Cap_2_M_1[t+1]) # Index of second element
            if (Ind_2 - Ind_1) == 0: # If two warehouses were next to each other
                Truck_Cap_3_M_1_1 = 0 # There would be no truck capacity
            Truck_Cap_3_M_1_1 = Array[Ind_1:Ind_2] # Else, the truck would be from Ind_1 to Ind_2
            u = 0
            Caps_One_By_One = []
            for o in Truck_Cap_3_M_1_1: # For each item (location) in the truck
                Caps_Sum = 0
                Capacity_1 = Truck_Cap_3_M_1_1[u]
                Capacity_2 = Cap_Dataframe.loc[Capacity_1,'Capacity'] # How much the capacity is
                Caps_One_By_One = np.append(Caps_One_By_One,Capacity_2) # Append it
                u = u+1
            Caps_Sum = sum(Caps_One_By_One) # Add them up
            Caps_Sum_One_By_One = np.append(Caps_Sum_One_By_One,Caps_Sum) # Append all the sums   
        t = t+1
    Diff_Cap = []
    for i in Caps_Sum_One_By_One: # Capacity of each truck 
        if i > 100:
            Diff = i - 100 # Find the difference
            Diff_Cap = np.append(Diff_Cap,Diff)
        else:
            Diff = 0
            Diff_Cap = np.append(Diff_Cap,Diff)
    How_Much_Extra = sum(Diff_Cap)
    Penalty_M_1 = How_Much_Extra * Penalty_Value
    return Penalty_M_1


def Penalty_2(Array,Penalty_Value_1,Penalty_Value_2):
    
    Add_Penalties = []
    
    if Array[0] not in range(11): # If first element in array was not a warehouse
        Add_Penalties = np.append(Add_Penalties,Penalty_Value_1)
    
    if Array[-1] not in range(11): # If last element in array was not a warehouse
        Add_Penalties = np.append(Add_Penalties,Penalty_Value_1)
    
    if Array[1] in range(11): # If second element was warehouse    
        Add_Penalties = np.append(Add_Penalties,Penalty_Value_1)
    
    if Array[-2] in range(11): # If second to last was warehouse    
        Add_Penalties = np.append(Add_Penalties,Penalty_Value_1)
    
    t = 0
    for i in Array:
        if t < len(Array)-2: # If three cons. elements were warehouses
            A1 = Array[t]
            A2 = Array[t+1]
            A3 = Array[t+2]
            if A1 in range(11) and A2 in range(11) and A3 in range(11):
                Add_Penalties = np.append(Add_Penalties,Penalty_Value_2)
        t = t+1
    
    Sum_Add_Penalties = sum(Add_Penalties)
    
    return Sum_Add_Penalties


def Penalty_3(Array,Penalty_Value):
    Add_Penalties = []
    if Array[0] not in range(11): # If first element in array was not a warehouse
        Add_Penalties = np.append(Add_Penalties,Penalty_Value)
    if Array[-1] not in range(11): # If last element in array was not a warehouse
        Add_Penalties = np.append(Add_Penalties,Penalty_Value)
    Sum_Add_Penalties = sum(Add_Penalties)
    return Sum_Add_Penalties
        
        
        