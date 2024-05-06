#!/bin/bash

num_runs=10

total_moves=0

for ((i=1; i<=$num_runs; i++))
do
    echo "Running iteration $i..."
    
    output=$(python3 src/main.py "U") 
    moves=$(echo "$output" | grep -oP 'Final \K\d+')

    total_moves=$(( $total_moves + $moves ))
    echo "Number of moves for iteration $i: $moves"
done

# Calculate average number of moves
average_moves=$(( $total_moves / $num_runs ))
echo "Average number of moves: $average_moves"
