def tower_of_hanoi(disk, start, auxiliary, end):  
    if(disk == 1):  
        print('Move disk 1 from rod {} to rod {}'.format(start, end))  
        return
    tower_of_hanoi(disk - 1, start, end, auxiliary)  
    print('Move disk {} from rod {} to rod {}'.format(disk, start, end))  
    tower_of_hanoi(disk- 1, auxiliary, start, end)  
  
disk =  int(input('Enter the number of disks: '))
tower_of_hanoi(disk, 'A', 'B', 'C')